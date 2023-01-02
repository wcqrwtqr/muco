from .models import marketingdb
from django import forms
from django.conf import settings

from django.forms import DateTimeInput, DateInput

class marketingForm(forms.ModelForm):
    # meeting_date = forms.DateField(label="Meeting Date", input_formats=['%d-%m-%Y'])
    meeting_date = forms.DateField(label="Meeting Date", input_formats=['%Y-%m-%d'])
    class Meta:
        model = marketingdb
        fields = '__all__'
        # departmenet = [('WSS','WSS'),('H2S','H2S'), ('else','else')]
        type = [('Visit','Visit'),('Call','Call'), ('Confernce Call','Confernce Call')]

        labels = {
            'meeting_type':'Meeting',
            'meeting_description':'Description',
            'departement':'Department',
            'client':'Client',
            'attendance':'Attendees',
        }
        widgets  = {
            'description' : forms.Textarea(attrs={'rows':3 }),
            # 'departement' : forms.Select(choices=departmenet),
            'departement' : forms.Select(choices=settings.BL),
            'meeting_type': forms.Select(choices=type),
        }
