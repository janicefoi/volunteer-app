from django.shortcuts import render
from .models import Organization


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

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