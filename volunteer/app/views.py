from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login  # Renamed to avoid conflict
from django.contrib.auth import authenticate,  login
from .forms import UserRegistrationForm, VolunteeringRecordForm, VolunteerForm
from .models import Organization, Event, UserEvent, VolunteeringRecord, VolunteerHours, Donation
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required



@login_required
def dashboard(request):
    user = request.user
    volunteer_hours = VolunteerHours.objects.filter(user=user)
    
    data = {
        'labels': [],
        'data': [],
    }

    for entry in volunteer_hours:
        data['labels'].append(entry.organization)
        data['data'].append(entry.hours)
    
    return render(request, 'dashboard.html', {'chart_data': data})

def profile(request):
    if request.method == 'POST':
        form = VolunteeringRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = VolunteeringRecordForm()
    
    records = VolunteeringRecord.objects.all()
    return render(request, 'profile.html', {'form': form, 'records': records})

def index(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'index.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Attempting login with username: {username}")

        # Print the received username and password for debugging
        print(f"Received username: {username}, password: {password}")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Authentication successful for user: {username}")
            login(request, user)
            return redirect('home')  # Replace with your desired redirect URL after login
        else:
            print(f"Authentication failed for user: {username}")
            messages.error(request, 'Invalid username or password.')

            # Additional debugging: Check if the user exists in the database
            try:
                from .models import User
                user_exists = User.objects.filter(username=username).exists()
                if not user_exists:
                    print(f"User {username} does not exist in the database.")
                else:
                    print(f"User {username} exists in the database but authentication failed.")
            except Exception as e:
                print(f"Error checking user existence: {e}")

    # If method is not POST or authentication fails, render the login form
    return render(request, 'login.html')




def home(request):
    return render(request, 'home.html')


def profile(request):
    return render(request, 'profile.html')


def events(request):
    now = timezone.now()
    events = Event.objects.filter(date_time__gt=now)
    
    context = {
        'events': events,
    }
    
    return render(request, 'events.html', context)

@require_POST
def signup_for_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    user = request.user

    # Create UserEvent instance
    user_event, created = UserEvent.objects.get_or_create(user=user, event=event)

    if created:
        # Count attendees dynamically
        attendees_count = UserEvent.objects.filter(event=event).count()

        # Update event attendees count (if needed)
        event.attendees_count = attendees_count
        event.save()

        # Update user's events attended count
        user.events_attended += 1
        user.save()

        return JsonResponse({'message': 'Successfully signed up for the event.'})
    else:
        return JsonResponse({'message': 'You are already signed up for this event.'}, status=400)



def opportunityvolunteer(request):
    children_homes = Organization.objects.filter(type='Children Homes').order_by('?')[:3]
    hospitals = Organization.objects.filter(type='Hospitals & Clinics').order_by('?')[:3]
    elderly_homes = Organization.objects.filter(type='Elderly Homes').order_by('?')[:3]
    
    context = {
        'childrenhomes': children_homes,
        'hospitals': hospitals,
        'elderlyhomes': elderly_homes,
    }
    
    return render(request, 'opportunityvolunteer.html', context)



def organization_type(request, organization_type):
    organizations = Organization.objects.filter(type=organization_type)
    context = {'organizations': organizations, 'organization_type': organization_type}
    return render(request, 'organizationtype.html', context)


@login_required
def volunteerform(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST, user=request.user)
        if form.is_valid():
            volunteer_hours = form.save(commit=False)
            volunteer_hours.user = request.user
            # Calculate hours
            time_difference = volunteer_hours.date_to - volunteer_hours.date_from
            volunteer_hours.hours = time_difference.total_seconds() / 3600
            volunteer_hours.save()
            # Respond with a success message
            return JsonResponse({'message': 'Thank you for volunteering! Your information has been submitted.'})
    else:
        form = VolunteerForm(user=request.user)
    return render(request, 'volunteerform.html', {'form': form})


def signin(request):
    return render(request, 'sign-in.html')


def donations(request):
    donations = Donation.objects.all()
    return render(request, 'donations.html', {'donations': donations})


def donate(request):
    return render(request, 'donate.html')