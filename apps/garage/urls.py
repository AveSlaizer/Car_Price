from django.conf.urls.static import static
from django.urls import path
from config import settings
from .views import AddTransport, GarageView

urlpatterns = [
    path('', GarageView.as_view(), name='garage'),
    path('add_transport/', AddTransport.as_view(), name='add_transport'),
]
