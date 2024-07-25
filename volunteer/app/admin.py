from django.contrib import admin
from .models import Organization, Event, Donation, VolunteerHours

admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Donation)

@admin.register(VolunteerHours)
class VolunteerHoursAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'hours', 'date_from', 'date_to')
    list_filter = ('user', 'organization', 'date_from', 'date_to')
    search_fields = ('user__username', 'organization')
    actions = ['log_volunteer_hours']

    def log_volunteer_hours(self, request, queryset):
        for record in queryset:
            record.user.total_service_hours += record.hours
            record.user.save()
        self.message_user(request, "Volunteer hours logged successfully.")

