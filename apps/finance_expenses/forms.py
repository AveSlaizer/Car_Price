from django import forms
from config.settings import MONTHS_NAMES
from .graphs_utils.graph_bulider import GRAPH_CHOICES
from .models import FinanceExpense


class AddFinanceExpensesForm(forms.ModelForm):
    class Meta:
        model = FinanceExpense
        fields = ['transport', 'summ', 'date', 'odometer', 'expense_type', 'description']
        widgets = {
            'transport': forms.HiddenInput(),
            'description': forms.TextInput(),
        }


class MonthGraphsForm(forms.Form):
    transport_id = forms.CharField(widget=forms.HiddenInput)
    month_number = forms.CharField(widget=forms.Select(choices=MONTHS_NAMES, attrs={'default': 1}))
    graph_type = forms.ChoiceField(widget=forms.Select(choices=GRAPH_CHOICES))
