from dis import dis
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class createUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    Options = (
        ('nan', 'Your Gender'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('trans', 'Prefer not to say')
    )
    gender = forms.ChoiceField(required=True, choices=Options, widget=forms.Select(attrs={'class': 'gender'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile Number'}))

    class Meta:
        model = Profile
        fields = ["gender", "age", "mobile"]
