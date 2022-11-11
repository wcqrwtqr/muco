from .models import equipmentdb
from django import forms
# from .widgets import FengyuanChenDatePickerInput
from django.forms import  DateInput

class EquipmentForm(forms.ModelForm):
    # acquisition_date = forms.DateField(input_formats=['%d-%m-%Y'], widget=FengyuanChenDatePickerInput())
    acquisition_date = forms.DateField(input_formats=['%d-%m-%Y'] )
    class Meta:
        # bu = [('KIU', 'KIU'), ('SIU', 'SIU'), ('AGU', 'AGU'), ('NAU', 'NAU'),
        #       ('ADU', 'ADU')]
        # bl = [('SWT', 'SWT'), ('SLS', 'SLS'), ('WHM', 'WHM'), ('DST', 'DST')]
        model = equipmentdb
        fields = '__all__'
        labels = {
            'part_num': 'Part No',
            'serial_num': 'Serial No',
            'description': 'Description',
            'asset_life': 'Asset Life',
            'acquisition_cost': 'Purchase Cost',
            'acquisition_date ': 'Purchase Date',
            'file_link': 'Link',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            # 'BU': forms.Select(choices=bu),
            # 'BL': forms.Select(choices=bl),
        }
