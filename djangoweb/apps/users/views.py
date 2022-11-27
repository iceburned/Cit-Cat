from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from djangoweb.apps.users.forms import SignInForm

User = get_user_model()


def index(request):
    return render(request, 'index.html')


class SignUpBaseForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        field_classes = {'username': UsernameField}


class RegisterUserView(generic.CreateView):
    template_name = 'sign-up.html'
    form_class = SignUpBaseForm
    success_url = reverse_lazy('Index')


class SignInBaseForm(LoginView):
    pass


class SignInView(SignInBaseForm):
    template_name = 'sign-in.html'
    success_url = reverse_lazy('Index')


class SignOutBaseForm(LogoutView):
    pass


class SignOutView(SignOutBaseForm):
    next_page = reverse_lazy('Index')

