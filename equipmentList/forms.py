from .models import equipmentdb
from django import forms
from django.conf import settings

sorted_bl = sorted(settings.BL, key=lambda x: x[0])


class EquipmentForm(forms.ModelForm):
    acquisition_date = forms.DateField(input_formats=["%Y-%m-%d"])

    class Meta:
        model = equipmentdb
        fields = "__all__"
        labels = {
            "part_num": "Part No",
            "serial_num": "Serial No",
            "description": "Description",
            "asset_life": "Asset Life",
            "departement": "Departmenet",
            "acquisition_cost": "Purchase Cost",
            "acquisition_date ": "Purchase Date",
            "file_link": "Link",
        }
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "departement": forms.Select(choices=sorted_bl),
        }
