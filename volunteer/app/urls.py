from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('opportunityvolunteer/', views.opportunityvolunteer, name='opportunityvolunteer'),  
    path('donations/', views.donations, name='donations'),
    path('contact/', views.contact, name='contact'),
    path('volunteerform', views.volunteerform, name='volunteerform'),
    path('organization-type/<str:organization_type>/', views.organization_type, name='organization_type'),
]

