from registration.backends.default import DefaultBackend

import forms

class EmailAsUsernameBackend (DefaultBackend):

    def get_form_class(self, request):
        return forms.RegistrationFormArbitraryUsername
