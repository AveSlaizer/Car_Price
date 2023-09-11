from django.contrib import admin
from .models import ExpenseTypes, FinanceExpense

admin.site.register(ExpenseTypes)
admin.site.register(FinanceExpense)
