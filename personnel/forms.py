from .models import personneldb
from django import forms
from django.forms import ClearableFileInput


class personnelForm(forms.ModelForm):
    senionrty_date = forms.DateTimeField(
        input_formats=["%d-%m-%Y"],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker1",
            }
        ),
    )

    birth_date = forms.DateField(input_formats=["%Y-%m-%d"])

    class Meta:
        model = personneldb
        fields = "__all__"
        labels = {
            "seniorty_date": "Jion Date",
            "birth_date": "Birth Date",
            "first_name": "First Name",
            "last_name": "Last Name",
            "pdf_file": "upload file",
        }
        widgets = {
            # "pdf_file": ClearableFileInput(attrs={"multiple": True}),
        }
        # class MyForm(forms.Form):
        #     files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
