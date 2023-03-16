from django import forms


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

