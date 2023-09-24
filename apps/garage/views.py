from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .forms import AddTransportForm
from .models import Transport


class AddTransport(SuccessMessageMixin, CreateView):
    form_class = AddTransportForm
    template_name = 'garage/add_transport.html'
    success_message = 'Транспорт успешно добавлен'

    def form_valid(self, form):
        transport = form.save(commit=False)
        transport.save()
        transport.owner = self.request.user
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('garage')


class GarageView(ListView):
    model = Transport
    context_object_name = 'transport_list'
    template_name = 'garage/garage.html'

    def get_queryset(self):
        return Transport.objects.filter(owner=self.request.user.id)

