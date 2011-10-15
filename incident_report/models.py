from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class Person(models.Model):
    name 		= models.CharField(max_length=256)
    withhold	= models.BooleanField()
    class Meta:
        abstract = True

class Cop(Person):
    badge_num	= models.CharField(max_length=128, blank=True, null=True)
    cert_num	= models.CharField(max_length=128, blank=True, null=True)
    license_num	= models.CharField(max_length=10)
    agency		= models.ForeignKey('Agency')

class Witness(Person):
    contact_phone	= PhoneNumberField()
    contact_email	= models.EmailField()
    contact_other	= models.TextField()
    statement		= models.TextField()

class Victim(Person):
    arrested		= models.BooleanField()
    complaint		= models.BooleanField()
    lawyer			= models.BooleanField()
    charge			= models.CharField(max_length=128)
    injuries		= models.TextField()
    contact_phone	= PhoneNumberField()
    contact_email	= models.EmailField()
    contact_other	= models.TextField()

class Agency(models.Model):
    """Agencies will be presented as a dropdown and shouldn't be editable from the user-facing side"""
    state			= USStateField()
    name			= models.CharField(max_length=256)
    jurisdiction	= models.CharField(max_length=256)

class Evidence(models.Model):
    title		= models.CharField(max_length=128, blank=True, null=True)
    photo		= models.ImageField(upload_to="evidence")
    vid_link	= models.URLField()
    incident	= models.ForeignKey('Incident')
    private		= models.BooleanField()
	

class Incident(models.Model):
    date		= models.DateField()
    time		= models.TimeField()
    filed		= models.DateTimeField(auto_now=True,auto_now_add=True)
    loc_lat	    = models.FloatField()
    loc_lon     = models.FloatField()
    loc_text	= models.CharField(max_length=128, blank=True, null=True)
    loc_state	= models.CharField(max_length=128, blank=True, null=True)
    loc_city	= models.CharField(max_length=128, blank=True, null=True)
    cop			= models.ManyToManyField('Cop')	
    witness		= models.ManyToManyField('Witness')
    victim		= models.ManyToManyField('Victim')
    nature		= models.CharField(max_length=128, blank=True, null=True)
    private		= models.BooleanField()
    
    def _unicode_(self):
        return "buh"
        
# Create your models here.
