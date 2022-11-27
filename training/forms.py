from django import forms
from .models import trainingdb

# from .widgets import FengyuanChenDatePickerInput
from django.forms import  DateInput

class trainingForm (forms.ModelForm):
   training_date_start = forms.DateField(label="Training Date", input_formats=['%d-%m-%Y'], )
   training_date_expire = forms.DateField(label="Expiry",  input_formats=['%d-%m-%Y'], )

   class Meta:
      model = trainingdb
      fields = '__all__'

