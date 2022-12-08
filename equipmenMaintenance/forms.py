from django import forms
from .models import Maintenancedb, Batterymaintenancedb

class MaintenanceForm (forms.ModelForm):
   main_date_start = forms.DateField(input_formats=['%d-%m-%Y'])
   main_date_end = forms.DateField(input_formats=['%d-%m-%Y'] )
   expiry_date = forms.DateField(input_formats=['%d-%m-%Y'])

   class Meta:
      model = Maintenancedb
      fields = '__all__'
      ms = [('MS-1','MS-1'),('MS-2','MS-2'), ('MS-3','MS-3'), ('MS-4','MS-4'),
            ('Repair','Repair'),('Down','Down'), ('Waiting on Spares','Waiting on Spares'),
            ('Junked','Junked'),]
      widgets  = {
         'ms_type' : forms.Select(choices=ms),
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
