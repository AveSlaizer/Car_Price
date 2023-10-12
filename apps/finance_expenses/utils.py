from apps.garage.models import Transport


class DataMixin:
    """
    Миксин, содержащий различные методы для получения данных
    """
    @staticmethod
    def get_transport(request):
        """
        Возвращает объект Transport из БД по id взятому из GET запроса
        """
        return Transport.objects.get(pk=request.GET.get('transport_id'))
