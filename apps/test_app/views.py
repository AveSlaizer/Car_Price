from django.shortcuts import render


# Create your views here.
def show_main(request):
    return render(request, 'main.html')


def show_garage(request):
    return render(request, 'garage.html')


def show_account(request):
    return render(request, 'personal_account.html')
