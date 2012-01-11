from django.db import models
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class Person(models.Model):
    name 		= models.CharField(max_length=256)
    withhold	= models.BooleanField()

class PersonMeta(models.Model):
    TYPE_CHOICES = (
        ('cop','Cop'), 
        ('witness','Witness'), 
        ('victim','Victim'),
    )
    person_type     = models.TextField(choices=TYPE_CHOICES, max_length=50, null=False)
    arrested		= models.BooleanField()
    complaint		= models.BooleanField()
    lawyer			= models.BooleanField()
    charge			= models.CharField(max_length=128)
    injuries		= models.TextField(blank=True, null=True)
    contact_phone	= PhoneNumberField(blank=True, null=True)
    contact_email	= models.EmailField(blank=True, null=True)
    contact_other	= models.TextField(blank=True, null=True)
    statement		= models.TextField(blank=True, null=True)
    person          = models.ForeignKey('Person')
    incident        = models.ForeignKey('Incident')

class Agency(models.Model):
    """Agencies will be presented as a dropdown and shouldn't be editable from the user-facing side"""
    state			= USStateField()
    name			= models.CharField(max_length=256)
    jurisdiction	= models.CharField(max_length=256)

class Evidence(models.Model):
    title		= models.CharField(max_length=128, blank=True, null=True)
    statement	= models.TextField(max_length=128, blank=True, null=True)
    photo		= models.ImageField(upload_to="evidence",blank=True, null=True)
    vid_link	= models.URLField(blank=True, null=True)
    incident	= models.ForeignKey('Incident')
    person		= models.ForeignKey('Person')
    private		= models.BooleanField()

class Incident(models.Model):
    datetime	= models.DateTimeField(help_text="This works??")
    filed		= models.DateTimeField(auto_now=True,auto_now_add=True)
    loc_lat	    = models.FloatField()
    loc_lon     = models.FloatField()
    loc_text	= models.CharField(max_length=128, blank=True, null=True)
    loc_state	= models.CharField(max_length=128, blank=True, null=True)
    loc_city	= models.CharField(max_length=128, blank=True, null=True)
    person      = models.ManyToManyField("Person", through="PersonMeta")
    nature		= models.CharField(max_length=128, blank=True, null=True)
    private		= models.BooleanField()
    def _unicode_(self):
        return "buh"
