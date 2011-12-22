from django.forms.formsets import formset_factory
from incident_report.forms import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def create(request):
	IncidentFormset = formset_factory(IncidentForm)
	VictimFormset = formset_factory(VictimForm)
	CopFormset = formset_factory(CopForm)
	WitnessFormset = formset_factory(WitnessForm, extra=2)
	
	forms = {
		"incident" 	: IncidentFormset(),
		"victim" 	: VictimFormset(),
		"cop" 		: CopFormset(),
		"witness" 	: WitnessFormset()	
	}
	
	return render_to_response("incident_report/incident_form.html", {"forms":forms})
	