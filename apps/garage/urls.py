from django.urls import path, re_path
from apps.garage.views import Garage

urlpatterns = [
    path('', Garage.show_garage_page, kwargs={'page': 'garage'}, name='garage'),
]
