from django.shortcuts import render


class MainPage:
    @staticmethod
    def show_main_page(request):
        return render(request, 'main.html')
