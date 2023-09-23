from django.shortcuts import render


# Create your views here.
def show_main(request):
    return render(request, 'main.html')


def show_garage(request):
    return render(request, 'garage/garage.html')


def show_account(request):
    return render(request, 'personal_account.html')

# TODO реализовать добавление транспорта в гараж пользователя
# TODO реализовать отображения карточек транспорта в гараже пользователя

