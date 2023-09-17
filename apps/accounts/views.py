from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'

    def get_success_url(self):
        return reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('main')
