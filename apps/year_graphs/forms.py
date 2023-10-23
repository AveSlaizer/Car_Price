from django import forms
from django.utils import timezone

from apps.year_graphs.utils.year_graphs_settings import year_graphs_choice


class YearGraphSelectForm(forms.Form):
    """
    Форма выбора вида графика за год.
    """
    username = forms.CharField(
        widget=forms.HiddenInput,
    )
    transport_id = forms.IntegerField(
        widget=forms.HiddenInput,
    )
    graph_type = forms.CharField(
        widget=forms.Select(choices=year_graphs_choice),
        label='Тип графика',
        help_text='Выберите тип графика',
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 1950, 'max': timezone.now().year, 'default': timezone.now().year}),
        label='Год',
        help_text='Выберите год'
    )
