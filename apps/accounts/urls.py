from django.urls import path
from apps.accounts.views import LoginUser, RegisterUser

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    #path('profile/', )
]
