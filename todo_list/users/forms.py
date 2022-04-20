from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

User = get_user_model()


class UserRegistrationForm(ModelForm):
    """Форма регистрации пользователя"""

    password1 = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(max_length=64, widget=forms.PasswordInput(), label='Confirm Password')

    def __init__(self, *args, **kwargs):
        """Инициализация формы. Устанавливаем стили формам"""

        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'autocomplete': "off",
                'placeholder': field.label
            })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        """Проверяет тождество паролей"""

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError('Passwords must be equal')
        return password2

    def save(self, commit=True):
        """Создаем пользователя"""

        user = User.objects.create_user(self.cleaned_data['username'],
                                        self.cleaned_data['email'],
                                        self.cleaned_data['password1'])
        return user


class UserLoginForm(AuthenticationForm):
    """Форма авторизации пользователя"""

    def __init__(self, *args, **kwargs):
        """Инициализация формы. Устанавливаем стили формам"""

        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'autocomplete': "off",
                'placeholder': field.label
            })

    class Meta:
        model = User
        fields = ('username', 'password')
