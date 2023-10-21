from django.contrib import admin
from .models import MainPageCarousel


class AdminMainPageCarousel(admin.ModelAdmin):
    """
    Настройки таблицы MainPageCarousel для админ-панели.
    """
    list_display = ('title', 'image',)


admin.site.register(MainPageCarousel, AdminMainPageCarousel)
