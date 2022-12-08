from .models import personneldb
from django import forms
from django.forms import  DateInput
from django.forms import ClearableFileInput

class personnelForm(forms.ModelForm):
    # senionrty_date = forms.DateField(input_formats=['%d-%m-%Y'] )
    senionrty_date =forms.DateTimeField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

    birth_date = forms.DateField(input_formats=['%d-%m-%Y'] )
    class Meta:
        model = personneldb
        fields = '__all__'
        labels = {
            'seniorty_date': 'Jion Date',
            'birth_date': 'Birth Date',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'pdf_file': 'upload file',
            # 'acquisition_date ': 'Purchase Date',
            # 'file_link': 'Link',
        }
        widgets = {
            # 'description': forms.Textarea(attrs={'rows': 3}),
            'pdf_file': ClearableFileInput(attrs={'multiple': True}),
        }
