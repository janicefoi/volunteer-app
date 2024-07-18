from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    total_service_hours = models.PositiveIntegerField(default=0)
    events_attended = models.PositiveIntegerField(default=0)

    # Add related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_set', blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_set', blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Organization(models.Model):
    ORGANIZATION_TYPES = [
        ('Elderly Homes', 'Elderly Homes'),
        ('Hospitals & Clinics', 'Hospitals & Clinics'),
        ('Children Homes', 'Children Homes'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='organization_images/')
    type = models.CharField(max_length=25, choices=ORGANIZATION_TYPES)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/')
    organization = models.ForeignKey(Organization, related_name='events', on_delete=models.CASCADE, blank=True, null=True)
    attendees_count = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.name



class Donation(models.Model):
    DONATION_TYPES = [
        ('money', 'Money'),
        ('food', 'Food'),
        ('clothing', 'Clothing'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=DONATION_TYPES)
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    funds_raised = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    supporters = models.PositiveIntegerField(default=0)
    deadline = models.DateField()
    organization = models.ForeignKey(Organization, related_name='donations', null=True, blank=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, related_name='donations', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def percentage_collected(self):
        if self.goal > 0:
            return (self.funds_raised / self.goal) * 100
        return 0

class UserDonation(models.Model):
    user = models.ForeignKey(User, related_name='donations', on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, related_name='user_donations', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.donation.name}"

class UserEvent(models.Model):
    user = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='user_events', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

