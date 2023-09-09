from django.shortcuts import render


class Garage:

    @staticmethod
    def show_garage_page(request, page: str = ""):
        return render(request, f'garage/{page}.html')
