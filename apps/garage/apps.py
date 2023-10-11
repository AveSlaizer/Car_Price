from django.apps import AppConfig


class GarageConfig(AppConfig):
    """
        Настройки приложения garage.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.garage'
    verbose_name = 'Гараж'
