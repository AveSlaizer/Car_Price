from django.views.generic import ListView

from .models import MainPageCarousel


class MainPageView(ListView):
    model = MainPageCarousel
    context_object_name = 'carousel_list'
    template_name = 'main_page/main.html'

    def get_queryset(self):
        """
        Возвращает объект Queryset. Результат запроса в БД
        """
        queryset = enumerate(MainPageCarousel.objects.all())
        return queryset
