from apps.garage.models import Transport


class DataMixin:
    @staticmethod
    def get_transport(request):
        return Transport.objects.get(pk=request.GET.get('transport_id'))
