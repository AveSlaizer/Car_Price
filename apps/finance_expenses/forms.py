from django import forms
from config.settings import MONTHS_NAMES
from .graphs_utils.graph_builder import MONTH_GRAPH_CHOICES
from .models import FinanceExpense


class AddFinanceExpensesForm(forms.ModelForm):
    class Meta:
        model = FinanceExpense
        fields = ['transport', 'summ', 'date', 'odometer', 'expense_type', 'description']
        widgets = {
            'transport': forms.HiddenInput(),
            'description': forms.TextInput(),
        }


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
