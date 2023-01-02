from django import forms
from .models import trainingdb
from django.forms import  DateInput

class trainingForm (forms.ModelForm):
   training_date_start = forms.DateField(label="Training Date", input_formats=['%Y-%m-%d'], )
   training_date_expire = forms.DateField(label="Expiry",  input_formats=['%Y-%m-%d'], )

   class Meta:
      model = trainingdb
      fields = '__all__'

