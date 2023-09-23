from datetime import datetime
from django import forms
from .models import Transport


class AddTransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['brand', 'model', 'year', 'engine_volume', 'engine_power', 'odometer', 'fuel_type',
                  'transmission_type', 'drive_type', 'category']
        widgets = {
            'year': forms.NumberInput(attrs={'max': datetime.now().year, 'min': 1900}),
        }
