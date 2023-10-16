from django import forms
from django.utils import timezone

from apps.month_graphs.utils.month_graphs_settings import MONTH_GRAPH_CHOICES, MONTHS_NAMES


class MonthGraphSelectForm(forms.Form):
    """
    Форма выбора вида графика за месяц.
    """
    username = forms.CharField(
        widget=forms.HiddenInput,
    )
    transport = forms.IntegerField(
        widget=forms.HiddenInput,
    )
    graph_type = forms.CharField(
        widget=forms.Select(choices=MONTH_GRAPH_CHOICES),
        label='Тип графика',
        help_text='Выберите тип графика',
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'min': 1950, 'max': timezone.now().year, 'default': timezone.now().year}),
        label='Год',
        help_text='Выберите год'
    )
    month_number = forms.IntegerField(
        widget=forms.Select(choices=MONTHS_NAMES, attrs={'default': 1}),
        label='Месяц',
        help_text='Выберите месяц',
    )
