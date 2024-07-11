from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'), 
    path('events/', views.events, name='events'),
    path('opportunityvolunteer/', views.opportunityvolunteer, name='opportunityvolunteer'),  
    path('donations/', views.donations, name='donations'),
    
]

