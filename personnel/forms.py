from .models import personneldb
from django import forms
from django.forms import  DateInput

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
            # 'acquisition_cost': 'Purchase Cost',
            # 'acquisition_date ': 'Purchase Date',
            # 'file_link': 'Link',
        }
        # widgets = {
        #     'description': forms.Textarea(attrs={'rows': 3}),
        #     # 'BU': forms.Select(choices=bu),
        #     # 'BL': forms.Select(choices=bl),
        # }
