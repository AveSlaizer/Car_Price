from django.urls import path
from apps.accounts.views import registration

urlpatterns = [
    path('registration/', registration, name='registration'),
]
