from django.urls import path, re_path
from views import Garage

urlpatterns = [
    path('', Garage.show_garage_page, kwargs={'page': 'garage'}, name='garage'),
    re_path(r'\w+', Garage.show_garage_page, kwargs={'page': 'garage'}, name='garage'),
]
