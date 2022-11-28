from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class SignInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
