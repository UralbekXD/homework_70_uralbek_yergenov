from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )

    password = forms.CharField(
        required=True,
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3',
            }
        )
    )


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3'
            }
        ),
    )

    password_confirm = forms.CharField(
        label='Подтвердить пароль',
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-3'
            }
        ),
    )

    email = forms.EmailField(
        label='Электронная почта',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control mb-3'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'email'
        )

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control mb-3',
                }
            ),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) == 0:
            raise ValidationError('Это поле обязательное для заполнения!')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) == 0:
            raise ValidationError('Это поле обязательное для заполнения!')
        return last_name

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
