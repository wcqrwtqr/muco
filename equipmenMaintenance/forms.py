from django import forms
from .models import Maintenancedb, Batterymaintenancedb
from django.conf import settings


class MaintenanceForm(forms.ModelForm):
    main_date_start = forms.DateField(input_formats=["%Y-%m-%d"])
    main_date_end = forms.DateField(input_formats=["%Y-%m-%d"])
    expiry_date = forms.DateField(
        label="Expiry Date",
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = Maintenancedb
        fields = "__all__"
        widgets = {
            "ms_type": forms.Select(choices=settings.MS),
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class BatteryMaintenanceForm(forms.ModelForm, forms.Form):
    check_date = forms.DateField(
        label="Check Date",
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = Batterymaintenancedb
        fields = "__all__"
        ms = [
            ("Voltage", "Voltage"),
            ("Visutal Check", "Visutal Check"),
            ("Junked", "Junked"),
        ]
        widgets = {
            "ms_type": forms.Select(choices=settings.MS),
        }
