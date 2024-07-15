from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login  # Renamed to avoid conflict
from django.contrib.auth import authenticate
from .forms import UserRegistrationForm
from .models import Organization


def index(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Use auth_login to avoid conflict
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'index.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')

def donations(request):
    return render(request, 'donations.html')

def contact(request):
    return render(request, 'contact.html')

def events(request):
    return render(request, 'events.html')

def opportunityvolunteer(request):
    return render(request, 'opportunityvolunteer.html')

def organization_type(request, organization_type):
    organizations = Organization.objects.filter(type=organization_type)
    context = {'organizations': organizations, 'organization_type': organization_type}
    return render(request, 'organizationtype.html', context)

def volunteerform(request):
    return render(request, 'volunteerform.html')

def signin(request):
    return render(request, 'sign-in.html')