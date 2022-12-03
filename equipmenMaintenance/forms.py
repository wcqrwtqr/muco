from django import forms
from .models import Maintenancedb, Batterymaintenancedb
# from templates.widgets import FengyuanChenDatePickerInput
from django.forms import  DateInput

class MaintenanceForm (forms.ModelForm):
   # expiry_date = forms.DateField(label="Expiry Date",  input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput())
   main_date_start = forms.DateField(label="Start Date", input_formats=['%d-%m-%Y'], )
   main_date_end = forms.DateField(label="End Date",  input_formats=['%d-%m-%Y'], )
   expiry_date = forms.DateField(label="Expiry Date",  input_formats=['%d-%m-%Y'],)

   class Meta:
      model = Maintenancedb
      fields = '__all__'

      ms = [('MS-1','MS-1'),('MS-2','MS-2'), ('MS-3','MS-3'), ('MS-4','MS-4'),
            ('Repair','Repair'),('Down','Down'), ('Waiting on Spares','Waiting on Spares'),
            ('Junked','Junked'),]

      # labels = {
      #    'main_date_start' :'Start Date',
      #    'ms_type' :'Maintenance Date',
      #    'main_date_end' :'End Date',
      #    'main_cost' :'Maintenance Cost',
      #    'expiry_date' :'Expiry Date',
      #    'asset' :'Asset',
      #    'description' :'Description',
      #    'file_link':'Link',
      # }
      widgets  = {
         'main_date_start' : forms.SelectDateWidget(years=[x for x in range(2020,2025)]),
         'ms_type' : forms.Select(choices=ms),
         'main_date_end' : forms.SelectDateWidget(years=[x for x in range(2020,2025)]),
         'expiry_date' : forms.SelectDateWidget(years=[x for x in range(2020,2025)]),
         'description' : forms.Textarea(attrs={'rows':3 }),

      }


class BatteryMaintenanceForm (forms.ModelForm):
   check_date = forms.DateField(label="Check Date", input_formats=['%d-%m-%Y'], )

   class Meta:
      model = Batterymaintenancedb
      fields = '__all__'

      ms = [('Voltage','Voltage'),('Visutal Check','Visutal Check'), ('Junked','Junked'),]

      widgets  = {
         'ms_type' : forms.Select(choices=ms),
      }
