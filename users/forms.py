from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields["username"].help_text = ''
        self.fields["password1"].help_text = ''
        self.fields["password2"].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
