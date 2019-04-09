from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import UsernameField
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

from django.utils.text import capfirst
from django.contrib.auth.forms import UserModel
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


# class LoginForm(forms.Form):
#     email = forms.CharField(
#         widget=forms.EmailInput,
#         label='email',
#         max_length=100
#         )
#     password = forms.CharField(
#         widget=forms.PasswordInput,
#         label='password',
#         max_length=100)


class AuthenticationFormEmail(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    # username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    email = forms.EmailField()
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        # 'invalid_login': _(
        #     "Please enter a correct %(email)s and password. Note that both "
        #     "fields may be case-sensitive."
        # ),
        'invalid_login': _(
            "Saisissez une addresse email et un mot de passe valides. "
            "Remarquez que chacun de ces champs est sensible à la casse "
            "(différenciation des majuscules/minuscules)."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "email" field.
        self.email_field = UserModel._meta.get_field(UserModel.EMAIL_FIELD)
        self.fields['email'].max_length = self.email_field.max_length or 254
        if self.fields['email'].label is None:
            self.fields['email'].label = capfirst(self.email_field.verbose_name)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'email': self.email_field.verbose_name},
        )


class LoginForm(AuthenticationFormEmail):

    class Meta:
        model = User
        fields = ('email', 'password')
