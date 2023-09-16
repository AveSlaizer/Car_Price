'''
class RegistrationForm(forms.Form):
    login = forms.SlugField(
        label='Логин',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Логин'}),
    )
    e_mail = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'example@examle.ex'}),
    )
    first_name = forms.CharField(
        label='Имя',
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Миша'})
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Иванов'})
    )
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
    )
'''