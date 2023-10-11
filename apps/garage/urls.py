from django.urls import path
from .views import AddTransport, GarageView

urlpatterns = [
    path('', GarageView.as_view(), name='garage'),
    path('add_transport/', AddTransport.as_view(), name='add_transport'),
]
