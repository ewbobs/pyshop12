from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('home') #используем на классах как атрибута просто реверсс в функциях используется


class SigninView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')
