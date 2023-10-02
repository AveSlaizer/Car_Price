from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

DEFAULT_GROUP_NAME = 'common user'  # Группа, в которую по умолчанию попадает новый пользователь


class RegisterUser(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'
    success_message = "Вы успешно зарегистрировались! Авторизуйтесь, чтобы продолжить."

# FIXME убрать добавление нового пользователя в группу.
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        user_group = Group.objects.get(name=DEFAULT_GROUP_NAME)
        user.groups.add(user_group)
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('main')

