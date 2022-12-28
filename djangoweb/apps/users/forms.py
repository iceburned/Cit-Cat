from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from djangoweb.apps.users.models import AboutData

User = get_user_model()


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'username', 'email', 'first_name', 'last_name', 'age', 'city', 'gender', 'avatar_pic'


class SignUpBaseForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        field_classes = {'username': UsernameField}


class AboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutData
        fields = '__all__'
