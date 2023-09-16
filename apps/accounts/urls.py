from django.urls import path
from apps.accounts.views import Accounts

urlpatterns = [
    path('registration/', Accounts.registration, name='registration'),
    path('registration_done/', Accounts.registration_done, name='registration_done'),
]
