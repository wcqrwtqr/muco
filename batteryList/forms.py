from .models import batterydb
from django import forms
from django.forms import  DateInput

class BatteryForm(forms.ModelForm):
    in_service_date = forms.DateField(input_formats=['%Y-%m-%d'] )
    purchase_date = forms.DateField(input_formats=['%Y-%m-%d'] )
    class Meta:
        model = batterydb
        fields = '__all__'
        labels = {
            'part_num': 'Part No',
            'serial_num': 'Serial No',
            'description': 'Description',
            'purchase_date': 'Purchase Date',
            'acquisition_cost': 'Asset Life',
            'in_service_date ': 'Put in Service',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
