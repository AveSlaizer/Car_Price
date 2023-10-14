from django.urls import path
from apps.month_graphs.views import MonthGraphView

urlpatterns = [
    path('', MonthGraphView.as_view(), name='month_graph_form')
]