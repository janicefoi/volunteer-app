# forms.py
from django import forms
from .models import User, VolunteeringRecord, VolunteerHours, Organization


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class VolunteeringRecordForm(forms.ModelForm):
    class Meta:
        model = VolunteeringRecord
        fields = ['organization', 'event', 'donations', 'hours']


class VolunteerForm(forms.ModelForm):
    name = forms.CharField(max_length=100, initial='')
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    is_adult = forms.BooleanField(required=False, label="Are you older than 18?")
    group_size = forms.IntegerField(required=False, label="How many members are in your group?")
    organization = forms.ModelChoiceField(queryset=Organization.objects.all(), empty_label="Select an organization")

    class Meta:
        model = VolunteerHours
        fields = ['organization', 'date_from', 'date_to']
        widgets = {
            'date_from': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_to': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(VolunteerForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['name'].initial = user.get_full_name()
            self.fields['email'].initial = user.email



