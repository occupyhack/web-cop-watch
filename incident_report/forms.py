from django.forms import ModelForm, ModelMultipleChoiceField
from incident_report.models import *

class IncidentForm(ModelForm):
    class Meta:
        model = Incident