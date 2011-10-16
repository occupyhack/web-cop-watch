from django.conf.urls.defaults import *

import registration.views

urlpatterns = patterns('',
    url(r'^register/$',
        registration.views.register,
        {'backend': 'registration_backends.email_as_username.EmailAsUsernameBackend'},
        name='registration_register'),

    url(r'^',
        include('registration.backends.default.urls')),
)
