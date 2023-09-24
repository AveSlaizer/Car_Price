from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import AddTransport

urlpatterns = [
    path('', TemplateView.as_view(template_name='garage/garage.html'), name='garage'),
    path('add_transport/', AddTransport.as_view(), name='add_transport'),
]
