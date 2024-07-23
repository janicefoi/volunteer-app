from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('profile/', views.profile, name='profile'),
    path('opportunityvolunteer/', views.opportunityvolunteer, name='opportunityvolunteer'),  
    path('donations/', views.donations, name='donations'),
    path('volunteerform/', views.volunteerform, name='volunteerform'),
    path('organization-type/<str:organization_type>/', views.organization_type, name='organization_type'),
    path('signup/<int:event_id>/', views.signup_for_event, name='signup_for_event'),
    path('add_hours/', views.profile, name='add_hours'),
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

