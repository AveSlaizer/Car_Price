from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUser(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'
    success_message = "Вы успешно зарегистрировались! Авторизуйтесь, чтобы продолжить."

    def get_success_url(self):
        return reverse_lazy('main')
