from django.forms.models import modelformset_factory
from incident_report.forms import *
from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages

def create(request):
    IncidentFormset = modelformset_factory(Incident, form=IncidentForm)
    EvidenceFormset = modelformset_factory(Evidence, form=EvidenceForm, extra=2)
    
    if request.method == "POST":
        if request.POST.get('role'):
            messages.success(request, request.POST.get('role'))
        forms = {
    		"incident" 	: IncidentFormset(request.POST, prefix='incident', queryset=None),
    	}
    	"""if all(x.is_valid() for x in forms.values()):
    	    i = forms["incident"].save()
    	    
    	    for x in ["victim","cop","witness"]:
    	        y = forms[x].save()
    	        if y:
    	            getattr(i[0],x).add(y[0])
                    
    	    if i:
    	        messages.success(request, "Shit added succesfully bitch")
    	    else:
    	        messages.error(request, "you broke it")
    	    
    	else:
    	    messages.error(request, 'Didnt validate, asshole')"""
    else:
        forms = {
    		"incident" 	: IncidentFormset(prefix='incident', queryset=Incident.objects.none()),
    	}
    
    c = RequestContext(request, {
        'forms' : forms,
    })
	
    return render_to_response("incident_report/incident_form.html", c)	