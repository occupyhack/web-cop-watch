from django.conf.urls.defaults import patterns, include, url
from django.views.generic.create_update import create_object, update_object
from incident_report.models import *
from incident_report.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(?P<role>\w+)$', create),
	url(r'^$', create),
)