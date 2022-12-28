from django import forms
from django.contrib.auth.forms import UsernameField


class LoginForm(forms.Form):
    username = UsernameField(label="用户名", widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label="密码",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
