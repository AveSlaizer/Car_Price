from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import AddTransport, GarageView

urlpatterns = [
    path('', GarageView.as_view(), name='garage'),
    path('add_transport/', AddTransport.as_view(), name='add_transport'),
]
