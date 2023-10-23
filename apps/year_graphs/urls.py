from django.urls import path
from django.views.generic import TemplateView

from apps.year_graphs.views import YearGraphFormView


urlpatterns = [
    path('', TemplateView.as_view(template_name='year_graphs/year_graph.html'), name='year_graph'),
    path('year_graph_form/', YearGraphFormView.as_view(), name='year_graph_form'),
]