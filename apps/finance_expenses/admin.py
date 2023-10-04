from django.contrib import admin
from .models import ExpenseTypes, FinanceExpense


class AdminFinanceExpense(admin.ModelAdmin):
    list_display = ('id', 'transport', 'summ', 'date', 'odometer', 'expense_type', 'add_date')
    search_fields = ('transport', 'date', 'add_date')
    list_filter = ('date', 'expense_type', 'add_date')
    ordering = ('id', 'transport', 'summ', 'date', 'odometer', 'expense_type', 'add_date')


admin.site.register(ExpenseTypes)
admin.site.register(FinanceExpense, AdminFinanceExpense)
