from .models import dailyreportdb
from django import forms

class DailyForm(forms.ModelForm):
    operationdate = forms.DateField(label="Date",input_formats=['%Y-%m-%d'])

    class Meta:
        model = dailyreportdb
        fields = '__all__'
        labels = {
            'lastdayops' : "Last Day Operation",
            'nextdayops' : "Next Day Operation",
            'jobid' : "Job ID",
            'h2s' :"H2S",
            'co2' : "CO2",
            'oilrate' :"Oil Rate",
            'waterrate' :"Water rate",
            'dp' :"Diff Pressure",
            'staticp' :"Static pressure",
            'gasrate' :"Gas Rate",
            'orifice' :"Orifice Size",
            'cmf' :"CMF",
            'whp' :"WHP",
            'todayproduced' :"Daily Production",
            'totalproduction' :"Total Production",
            'wht' :"WHT",
            'bsw' :"BSW",
            'flowduration' :"Flow Durtion",
            'chokesize' :'Choke Size 1/64"',
            'supervisorname' :"Superviosr Name",
        }
        widgets = {
            'lastdayops': forms.Textarea(attrs={'rows': 3}),
            'nextdayops': forms.Textarea(attrs={'rows': 3}),
        }


