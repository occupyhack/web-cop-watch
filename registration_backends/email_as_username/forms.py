import random
import string

from django import forms
from django.contrib.auth.models import User
import registration.forms


class RegistrationFormArbitraryUsername (registration.forms.RegistrationFormUniqueEmail):
    """
    Subclass of ``RegistrationFormUniqueEmail`` which generates a unique user
    name is none is supplied.

    """

    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                required=False,
                                widget=forms.HiddenInput(attrs=registration.forms.attrs_dict),
                                error_messages={'invalid': registration.forms._("This value must contain only letters, numbers and underscores.")})

    def _get_random_unique_username(self):
        """
        Make an arbitrary and unique username

        """
        while True:
            try:
                # Use the first 15 characters of the email_user, concatenated
                # with 15 random letters/numbers.
                username = ''.join(random.choice(string.letters + string.digits)
                                   for i in xrange(30))
                user = User.objects.get(username__iexact=username)
            except User.DoesNotExist:
                return username

    def clean_username(self):
        """
        Provide an arbitrary username based off of the email address if no
        username is provided.

        """
        if self.cleaned_data['username'] in ('', None):
            self.cleaned_data['username'] = \
                self._get_random_unique_username()

        return super(RegistrationFormArbitraryUsername, self).clean_username()
