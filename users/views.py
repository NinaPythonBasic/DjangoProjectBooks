from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import RegistrationForm


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/registration_form.html'


class UserLoginView(LoginView):
    template_name = 'users/login_form.html'


class UserLogoutView(LogoutView):
    pass
