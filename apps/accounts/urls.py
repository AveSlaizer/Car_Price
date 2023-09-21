from django.urls import path
from apps.accounts.views import LoginUser, RegisterUser, LogoutUser
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
]
