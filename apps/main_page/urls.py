from django.urls import path
from django.views.generic import TemplateView

from .views import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
]
