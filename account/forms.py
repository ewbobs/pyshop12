from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput) #скрывает пароль и показывает черные точки
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation',
                  'first_name', 'last_name')

    def clean_email(self): #через андерскор мы выбираем то что хотим провалидировать чтоб он не повторялся
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Юзер с таким email уже существует')
        return email

    def clean_username(self): #через андерскор мы выбираем то что хотим провалидировать чтоб он не повторялся
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Юзер с таким именем уже существует')
        return username


    def clean(self):
        data = self.cleaned_data #примерно {'username': 'isken', 'password': 'qwerty', 'password_confirmation': 'qwerty'}
        print(data)
        password = data.get('password')
        password_confirm = data.pop('password_confirmation')
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают') #raise поднимает ошибку и выявляет ее на экран
        return data

    def save(self, commit=True):  #commit True значит изменения отправляются в базу данных, этот метод работает только после метода клин
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user


