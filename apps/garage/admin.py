from django.contrib import admin
from .models import FuelType, TransmissionType, DriveType, Transport, TransportCategory


class AdminTransportCategory(admin.ModelAdmin):
    list_display = ('category', 'image')


class AdminTransport(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'year', 'odometer', 'add_date',)
    search_fields = ('model', 'brand', 'year', 'odometer',)
    list_filter = ('brand', 'model', 'year', 'engine_volume', 'engine_power', 'odometer', 'fuel_type',
                   'transmission_type', 'drive_type', 'category', 'add_date',)
    ordering = ('brand', 'model', 'year',)


admin.site.register(FuelType)
admin.site.register(TransmissionType)
admin.site.register(DriveType)
admin.site.register(TransportCategory, AdminTransportCategory)
admin.site.register(Transport, AdminTransport)
