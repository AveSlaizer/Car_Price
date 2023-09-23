from django.urls import path
from django.views.generic import TemplateView
from apps.accounts.views import RegisterUser
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
]
