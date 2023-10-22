from django.urls import path
from django.views.generic import TemplateView

from apps.month_graphs.views import MonthGraphFormView

urlpatterns = [
    path('', TemplateView.as_view(template_name='month_graphs/month_graph.html'), name='month_graph'),
    path('month_graph_form/', MonthGraphFormView.as_view(), name='month_graph_form'),
]
