from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUser(SuccessMessageMixin, CreateView):
    """
        Рендерит шаблон с формой регистрации нового пользователя
    """
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'
    success_message = "Вы успешно зарегистрировались! Авторизуйтесь, чтобы продолжить."

    def get_success_url(self):
        """
        Возвращает тэг шаблона.
        :return: reverse_lazy
        """
        return reverse_lazy('main')
