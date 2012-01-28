from django.forms.models import modelformset_factory
from incident_report.forms import *
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

def create(request, role = None):
    IncidentFormset = modelformset_factory(Incident, form=IncidentForm)
    EvidenceFormset = modelformset_factory(Evidence, form=EvidenceForm, extra=2)
    f = {}
    if request.method == "POST":
            messages.success(request, request.POST.get('role'))
            f["incident"] = IncidentFormset(request.POST, prefix='incident', queryset=None)
    else:
        f = {
    		"incident" 	: IncidentFormset(prefix='incident', queryset=Incident.objects.none()),
			"evidence"	: EvidenceFormset(prefix='evidence', queryset=Evidence.objects.none())
    	}
	d = {
		'forms' : f,
		'role' : role
	}
	c = RequestContext(request, d)

	return render_to_response("incident_report/incident_form.html", c)	