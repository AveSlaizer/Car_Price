from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

DEFAULT_GROUP_NAME = 'common user'


class RegisterUser(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'
    success_message = "all_ok"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        user_group = Group.objects.get(name=DEFAULT_GROUP_NAME)
        user.groups.add(user_group)
        mess = self.get_success_message(form.cleaned_data)
        print(mess)
        # messages.success(request, 'Form submission successful')
        return redirect(self.get_success_url())

    def get_success_url(self):
        return 'login'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('main')

# TODO попробовать разобраться с всплывающими сообщениями
