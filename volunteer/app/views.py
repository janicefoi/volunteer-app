from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login  # Renamed to avoid conflict
from django.contrib.auth import authenticate,  login
from .forms import UserRegistrationForm, VolunteeringRecordForm, VolunteerForm
from .models import Organization, Event, UserEvent, VolunteeringRecord, VolunteerHours, Donation, UserDonation
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required
import base64
import datetime
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Max



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



@login_required
@csrf_exempt
@require_POST
def initiate_mpesa_payment(request):
    try:
        json_data = json.loads(request.body)
        amount = json_data.get('amount')
        phone_number = json_data.get('phone_number')
        donation_id = json_data.get('donation_id')
        donation = get_object_or_404(Donation, id=donation_id)
        
        mpesa_api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        business_short_code = "174379"
        lipa_na_mpesa_online_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        password = base64.b64encode(
            (business_short_code + lipa_na_mpesa_online_passkey + timestamp).encode('utf-8')
        ).decode('utf-8')
        
        payload = {
            "BusinessShortCode": int(business_short_code),
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(amount),
            "PartyA": int(phone_number),
            "PartyB": int(business_short_code),
            "PhoneNumber": int(phone_number),
            "CallBackURL": "https://yourcallbackurl.com/mpesa-callback",
            "AccountReference": "Donation",
            "TransactionDesc": f"Donation to {donation.name}",
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer VxXaYtyFX1LRJ9s01tsiUsLl6L5k'
        }

        print("Mpesa Request Body:", json.dumps(payload))

        response = requests.post(mpesa_api_url, json=payload, headers=headers)
        print("Mpesa Response:", response.text)

        response_data = response.json()

        if response_data.get('ResponseCode') == '0':
            # Create a UserDonation instance only if payment initiation is successful
            UserDonation.objects.create(
                user=request.user,
                donation=donation,
                amount=amount,
                date=datetime.datetime.now()
            )
            donation.funds_raised += amount
            donation.supporters += 1
            donation.save()
            return JsonResponse({'status': 'success', 'message': 'Please complete the payment on your phone.'})
        else:
            return JsonResponse({'status': 'error', 'message': response_data.get('errorMessage', 'Payment initiation failed.')})

    except Exception as e:
        return JsonResponse({"error": str(e)})


@login_required
def user_profile(request):
    user = request.user
    user_events = UserEvent.objects.filter(user=user)
    volunteer_hours = VolunteerHours.objects.filter(user=user, verified=True)  # Only include verified hours
    total_volunteer_hours = volunteer_hours.aggregate(Sum('hours'))['hours__sum'] or 0
    
    # Group donations by the cause and aggregate amounts
    donations = (
        UserDonation.objects.filter(user=user)
        .values('donation__name')
        .annotate(total_amount=Sum('amount'), latest_date=Max('date'))
    )
    total_donated_amount = donations.aggregate(total=Sum('total_amount'))['total'] or 0

    context = {
        'user': user,
        'user_events': user_events,
        'volunteer_hours': volunteer_hours,
        'total_volunteer_hours': total_volunteer_hours,
        'donations': donations,
        'total_donated_amount': total_donated_amount,
    }

    return render(request, 'profile.html', context)




