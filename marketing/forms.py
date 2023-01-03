from .models import marketingdb
from django import forms
from django.conf import settings

from django.forms import DateTimeInput, DateInput

sorted_clients = sorted(settings.CLINET, key=lambda x : x[0])
sorted_type = sorted(settings.TYPE, key=lambda x : x[0])
sorted_bl = sorted(settings.BL, key=lambda x : x[0])


class marketingForm(forms.ModelForm):
    # meeting_date = forms.DateField(label="Meeting Date", input_formats=['%d-%m-%Y'])
    meeting_date = forms.DateField(label="Meeting Date", input_formats=['%Y-%m-%d'])
    class Meta:
        model = marketingdb
        fields = '__all__'

        labels = {
            'meeting_type':'Meeting',
            'meeting_description':'Description',
            'departement':'Department',
            'client':'Client',
            'attendance':'Attendees',
        }
        widgets  = {
            'description' : forms.Textarea(attrs={'rows':3 }),
            'departement' : forms.Select(choices=sorted_bl),
            'meeting_type': forms.Select(choices=sorted_type),
            'client': forms.Select(choices=sorted_clients),
        }
