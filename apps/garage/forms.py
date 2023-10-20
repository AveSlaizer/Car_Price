from datetime import datetime
from django import forms
from .models import Transport


class AddTransportForm(forms.ModelForm):
    """
    Форма добавления записи в таблицу Transport.
    """
    class Meta:
        model = Transport
        fields = ['brand', 'model', 'year', 'engine_volume', 'engine_power', 'odometer', 'fuel_type',
                  'transmission_type', 'drive_type', 'category', 'description']
        widgets = {
            'year': forms.NumberInput(attrs={'max': datetime.now().year, 'min': 1900}),
        }
        description = forms.CharField(required=False)


class DeleteTransportForm(forms.Form):
    """
    Форма для удаления ТС из БД
    """
    transport = forms.CharField(
        widget=forms.HiddenInput,
    )
    check_box = forms.BooleanField(
        widget=forms.CheckboxInput,
        label='Я уверен, что хочу удалить {% transport %} и все связанные с ним записи.'
    )

