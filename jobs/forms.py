from .models import equipment_job_activitiesdb, jobsdb
from django import forms
from django.conf import settings

from django.forms import DateTimeInput, DateInput

class JobsForm(forms.ModelForm):
    startDate = forms.DateField(label="Start Date", input_formats=['%Y-%m-%d'])
    endDate = forms.DateField(label="End Date",input_formats=['%Y-%m-%d'])
    class Meta:
        model = jobsdb
        fields = '__all__'
        labels = {
            'jobid' :'Job ID',
            'client' :'Client',
            'field' :'Field',
            'well' :'Well',
            'country' :'Country',
            'description' :'Description',
            'departmenet' :'Department',
        }
        widgets  = {
            'description' : forms.Textarea(attrs={'rows':3 }),
            'departmenet' : forms.Select(choices=settings.BL),
            'service' : forms.Select(choices=settings.SERVICE),
        }


class EquipmentJobsForm(forms.ModelForm):
    class Meta:
        model = equipment_job_activitiesdb
        fields = '__all__'
        labels = {
            'jobidnew' :'Job ID',
            'assetnew' :'Asset',
            'battery'  :'Battery',
        }
        widgets  = {
            'battery' : forms.CheckboxSelectMultiple
        }
