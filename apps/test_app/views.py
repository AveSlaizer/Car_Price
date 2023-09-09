from django.shortcuts import render


# Create your views here.
def show_main(request):
    return render(request, 'main.html')


def show_garage(request):
    return render(request, 'garage/garage.html')


def show_account(request):
    return render(request, 'personal_account.html')

# TODO написать приложение main. (развернул)
# TODO написать приложение garage. (развернул)
# TODO написать приложение account (личный кабинет).
# TODO реализовать/настроить встроенную в джанго авторизацию
# TODO создать необходимые таблицы в БД
# TODO наполнить таблицы тестовыми данными
# TODO верстать!
