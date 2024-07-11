from django.contrib import admin
from .models import Organization, Event, Donation


admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Donation)

