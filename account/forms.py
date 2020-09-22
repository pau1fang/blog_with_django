from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(
            attrs={'id': 'inputUsername', 'class': 'form-control', 'placeholder': '用户名'})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'id': 'inputPassword', 'class': 'form-control', 'placeholder': '密   码'})


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = widgets.TextInput(
            attrs={'id': 'inputUsername', 'class': 'form-control', 'placeholder': '请输入用户名'})
        self.fields['email'].widget = widgets.EmailInput(
            attrs={'id': 'inputEmail', 'class': 'form-control', 'placeholder': '请输入邮箱'})
        self.fields['password1'].widget = widgets.PasswordInput(
            attrs={'id': 'inputPassword', 'class': 'form-control', 'placeholder': '请输入密码'})
        self.fields['password2'].widget = widgets.PasswordInput(
            attrs={'id': 'inputPassword', 'class': 'form-control', 'placeholder': '请确认密码'})

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("该邮箱已经存在.")
        return email

    class Meta:
        model = get_user_model()
        fields = ("username", "email")

