from django.apps import AppConfig


class MainPageConfig(AppConfig):
    """
    Настройки приложения main_page.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.main_page'
    verbose_name = 'Главная страница'
