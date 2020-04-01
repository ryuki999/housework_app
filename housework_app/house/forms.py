from django import forms
from .models import User


class User(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user_id", "username", "password"]


class UsernameForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        required=True, label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ユーザ名を入力してください．'
            }
        ))


class PasswordForm(forms.Form):
    password = forms.CharField(
        max_length=50,
        required=True, label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'パスワードを入力してください．'
                }
        ))
