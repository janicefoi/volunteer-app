import json
import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Organization, Event, Donation, VolunteerHours, UserDonation, UserEvent

User = get_user_model()

class VolunteerAppTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.organization = Organization.objects.create(
            name="Test Organization",
            description="Test Description",
            location="Test Location",
            type="Children Homes"
        )
        self.event = Event.objects.create(
            name="Test Event",
            description="Test Event Description",
            location="Test Location",
            date_time=timezone.now() + datetime.timedelta(days=1),
            organization=self.organization
        )
        self.donation = Donation.objects.create(
            name="Test Donation",
            description="Test Donation Description",
            goal=1000,
            organization=self.organization
        )
        self.volunteer_hours = VolunteerHours.objects.create(
            user=self.user,
            organization=self.organization,
            date_from=timezone.now() - datetime.timedelta(hours=2),
            date_to=timezone.now(),
            hours=2,
            verified=True
        )

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to home
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to home

    def test_events_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Event')

    def test_signup_for_event(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('signup_for_event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(UserEvent.objects.filter(user=self.user, event=self.event).exists())

    def test_volunteerform_submission(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('volunteerform'), {
            'organization': self.organization.id,
            'date_from': timezone.now() - datetime.timedelta(hours=2),
            'date_to': timezone.now()
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(VolunteerHours.objects.filter(user=self.user, organization=self.organization).exists())

    def test_initiate_mpesa_payment(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('initiate_mpesa_payment'), json.dumps({
            'amount': 100,
            'phone_number': '254700000000',
            'donation_id': self.donation.id
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # Assuming payment initiation success
        self.assertTrue(UserDonation.objects.filter(user=self.user, donation=self.donation, amount=100).exists())



