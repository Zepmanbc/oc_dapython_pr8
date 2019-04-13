from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2')
