from django.conf.urls.defaults import *

import registration.views as reg_views
import django.contrib.auth.views as auth_views
import forms

urlpatterns = patterns('',
    url(r'^register/$',
        reg_views.register,
        {'backend': 'registration_backends.email_as_username.EmailAsUsernameBackend'},
        name='registration_register'),

    url(r'^login/$',
        auth_views.login,
        {'template_name': 'registration/login.html',
         'authentication_form': forms.AuthenticationFormByEmail},
        name='auth_login'),

    url(r'^',
        include('registration.backends.default.urls')),
)
