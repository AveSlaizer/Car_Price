from django.db import models


class MainPageCarousel(models.Model):
    class Meta:
        verbose_name = 'элемент карусели'
        verbose_name_plural = 'Карусель главной страницы'

    image = models.ImageField(
        upload_to='image/main_page/carousel/',
        verbose_name='Изображение',
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
    )
    description = models.TextField(
        max_length=250,
        blank=True,
        verbose_name='Краткое описание',
    )
