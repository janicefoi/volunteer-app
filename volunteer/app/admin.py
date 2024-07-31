from django.contrib import admin
from .models import Organization, Event, Donation, VolunteerHours

admin.site.register(Organization)
admin.site.register(Event)
admin.site.register(Donation)

@admin.register(VolunteerHours)
class VolunteerHoursAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'hours', 'date_from', 'date_to', 'verified')
    list_filter = ('user', 'organization', 'date_from', 'date_to', 'verified')
    search_fields = ('user__username', 'organization')
    actions = ['log_volunteer_hours']

    def log_volunteer_hours(self, request, queryset):
        for record in queryset:
            record.verified = True  # Mark as verified
            record.user.total_service_hours += record.hours
            record.user.save()
            record.save()  # Save the updated record
        self.message_user(request, "Volunteer hours logged and marked as verified successfully.")



