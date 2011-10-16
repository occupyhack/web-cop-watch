import random
import string

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
import registration.forms
import django.contrib.auth.forms


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


class AuthenticationFormByEmail(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    email = forms.CharField(label=_("Email"), max_length=30)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super(AuthenticationFormByEmail, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            raise forms.ValidationError(_("Could not find a user with the email address."))

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(_("Please enter a correct email and password. Note that both fields are case-sensitive."))
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("This account is inactive."))
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(
                _("Your Web browser doesn't appear to have cookies enabled. "
                  "Cookies are required for logging in."))

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

#class AuthenticationFormByEmail (django.contrib.auth.forms.AuthenticationForm):

#    username = forms.HiddenInput()
#    email = forms.CharField(label=_("Email"))

#    def clean(self):
#        email = self.cleaned_data.get('email')
#        try:
#            user = User.objects.get(email=email)
#            self.cleaned_data['username'] = user.username
#        except User.DoesNotExist:
#            raise forms.ValidationError(_("Could not find a user with the email address."))

#        return super(AuthenticationFormByEmail, self).clean()
