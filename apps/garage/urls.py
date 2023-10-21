from django.urls import path

from .views import AddTransportView, GarageView, DeleteTransportView

urlpatterns = [
    path('', GarageView.as_view(), name='garage'),
    path('add_transport/', AddTransportView.as_view(), name='add_transport'),
    path('delete_transport/', DeleteTransportView.as_view(), name='delete_transport')
]
