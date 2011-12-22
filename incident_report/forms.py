from django.forms import ModelForm, ModelMultipleChoiceField
from incident_report.models import *

class IncidentForm(ModelForm):
    class Meta:
        model = Incident

class CopForm(ModelForm):
  class Meta:
      model = Cop

class VictimForm(ModelForm):
    class Meta:
		model = Victim

class WitnessForm(ModelForm):
    class Meta:
		model = Witness