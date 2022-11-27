from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


def index(request):
    return render(request, 'index.html')


class SignUpBaseForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        field_classes = {'username': UsernameField}


class RegisterUserView(generic.CreateView):
    template_name = 'templates/sign-up.html'
    form_class = SignUpBaseForm
    success_url = reverse_lazy('Index')


class SignInBaseForm(LoginView):
    pass


class SignInView(SignInBaseForm):
    template_name = 'templates/sign-in.html'


class SignOutBaseForm(LogoutView):
    pass


class SignOutView(SignOutBaseForm):
    next_page = reverse_lazy('Index')

