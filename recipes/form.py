from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Movie
from accounts.models import Profile
from django.forms import TextInput
from django.core.validators import ValidationError


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie']
        widgets = {'movie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'add your favorite movie'})}


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First name'}))
    last_name = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last name'}))

    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your user name'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'}),
                   }
        # password2 = forms.CharField(
        #     widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
        # password1 = forms.PasswordInput()

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.widgets.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your password'})
        self.fields['password2'].widget = forms.widgets.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Your password'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'biography', 'image_cover']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Location'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your biography'}),

        }


class ChangePassword(PasswordChangeForm):
    old_password = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'})
    new_password1 = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'})
    new_password2 = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Confirmation'})


class UserEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}),
        }


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'biography', 'image_cover']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Biography'}),
        }