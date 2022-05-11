from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import UserProfile


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm password'}),
    )

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'name': 'username', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'name': 'email', 'class': 'form-control', 'placeholder': 'Email kiriting'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Tel kiriting'}),
        }


class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name',
                  'email', 'phone_number', 'image', 'birthday', 'bio', 'address']

        widgets = {
            'username': forms.TextInput(attrs={'name': 'username', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'name': 'username', 'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'name': 'username', 'type': 'date', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'name': 'email', 'class': 'form-control', 'placeholder': 'Email kiriting'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Tel kiriting'}),
        }