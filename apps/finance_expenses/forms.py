from django import forms
from .models import FinanceExpense


class AddFinanceExpensesForm(forms.ModelForm):
    class Meta:
        model = FinanceExpense
        fields = ['transport', 'summ', 'date', 'odometer', 'expense_type', 'description']
        widgets = {
            'transport': forms.HiddenInput(),
            'description': forms.TextInput(),
        }
