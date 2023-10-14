from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import MonthGraphSelectForm
from ..garage.models import Transport


class MonthGraphView(FormView):
    form_class = MonthGraphSelectForm
    template_name = 'month_graphs/month_graph_form.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transport_obj = None

    def get_transport(self):
        transport_id = self.request.GET.get('transport_id')
        self.transport_obj = Transport.objects.get(pk=transport_id)

    def get_initial(self):
        initial = super(MonthGraphView, self).get_initial()
        self.get_transport()
        initial['transport'] = self.transport_obj
        return initial

    def form_valid(self, form):
        print(form.cleaned_data)

        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('main')