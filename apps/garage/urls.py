from django.urls import path

from .views import AddTransport, GarageView, DeleteTransport

urlpatterns = [
    path('', GarageView.as_view(), name='garage'),
    path('add_transport/', AddTransport.as_view(), name='add_transport'),
    path('delete_transport/', DeleteTransport.as_view(), name='delete_transport')
]
