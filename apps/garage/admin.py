from django.contrib import admin
from .models import FuelType, TransmissionType, DriveType, Transport

admin.site.register(FuelType)
admin.site.register(TransmissionType)
admin.site.register(DriveType)
admin.site.register(Transport)
