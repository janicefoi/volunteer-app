from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def donations(request):
    return render(request, 'donations.html')

def events(request):
    return render(request, 'events.html')

def opportunityvolunteer(request):
    return render(request, 'opportunityvolunteer.html')

def signin(request):
    return render(request, 'sign-in.html')