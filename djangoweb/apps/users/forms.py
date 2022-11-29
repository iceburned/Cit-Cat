from django.contrib.auth import get_user_model
from django import forms

from djangoweb.apps.users.models import UserProfileModel

User = get_user_model()


class SignInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self._user_id_kwargs = kwargs['pk']
    #     self._user_age = UserProfileModel.objects.get('user_id')
    #     super().__init__(*args, **kwargs)

    class Meta:

        model = UserProfileModel
        fields = '__all__'

        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'self.labels'}),
            'gender': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control', }),
            'signature': forms.Textarea(attrs={'class': 'card', }),

        }


