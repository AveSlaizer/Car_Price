from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name='common user')
            user.groups.add(user_group)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/registration.html', {'form': form})

# TODO дальше разбираться с регистрацией пользователей
