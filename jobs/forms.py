from .models import equipment_job_activitiesdb, jobsdb
from django import forms

from django.forms import DateTimeInput, DateInput

class JobsForm(forms.ModelForm):
    startDate = forms.DateField(label="Start Date", input_formats=['%d-%m-%Y'])
    endDate = forms.DateField(label="End Date",input_formats=['%d-%m-%Y'])
    class Meta:
        model = jobsdb
        fields = '__all__'
        departmenet = [('WSS','WSS'),('H2S','H2S'), ('Other','Other')]
        service = [('DH Camera','DH Camera'),('Eco meter','Eco meter'), ('BossPac','BossPac'), ('Xmile','Xmile'),]

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
            'departmenet' : forms.Select(choices=departmenet),
            'service' : forms.Select(choices=service),
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
