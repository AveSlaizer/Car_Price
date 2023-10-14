from django import forms

from apps.month_graphs.utils.month_graphs_settings import MONTH_GRAPH_CHOICES, MONTHS_NAMES


class MonthGraphSelectForm(forms.Form):
    transport = forms.CharField(
        widget=forms.HiddenInput,
    )
    graph_type = forms.CharField(
        widget=forms.Select(choices=MONTH_GRAPH_CHOICES),
        label='Тип графика',
        help_text='Выберите тип графика',
    )
    month_number = forms.CharField(
        widget=forms.Select(choices=MONTHS_NAMES, attrs={'default': 1}),
        label='Месяц',
        help_text='Выберите месяц',
    )