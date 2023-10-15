from django.shortcuts import render
from django.utils import timezone
from django.views.generic import FormView

from .forms import MonthGraphSelectForm
from .utils.graph_builder import MonthGraphBuilder
from .utils.month_graphs_settings import MONTHS_NAMES
from ..garage.models import Transport


class MonthGraphView(FormView):
    form_class = MonthGraphSelectForm
    template_name = 'month_graphs/month_graph_form.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transport_obj = None
        self.form_data = None

    def get_transport(self):
        transport_id = self.request.GET.get('transport_id')
        self.transport_obj = Transport.objects.get(pk=transport_id)

    def get_initial(self):
        initial = super(MonthGraphView, self).get_initial()
        self.get_transport()
        initial['username'] = self.request.user.username
        initial['transport'] = self.transport_obj.id
        initial['year'] = timezone.now().year
        return initial

    def form_valid(self, form):
        form_data = form.cleaned_data
        print('form valid:', form_data)
        builder = MonthGraphBuilder(**form_data)
        builder.build_and_save_graph(self.request)
        path = builder.get_user_dir() + '\\' + builder.get_file_name()
        context = {
            'file': path,
            'transport': self.transport_obj,
            'month': dict(MONTHS_NAMES)[form_data['month_number']].lower(),
            'year': form_data['year']
        }
        print(context)
        return render(self.request, 'month_graphs/month_graph.html', context=context)
