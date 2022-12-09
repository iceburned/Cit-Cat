from django.urls import path
from .views import RegisterUserView, index, SignInView, SignOutView, ProfileView, AboutPage

urlpatterns = (
    path('', index, name='Index'),
    path('reg/', RegisterUserView.as_view(), name='Register'),
    path('login/', SignInView.as_view(), name='Log-in'),
    path('logout/', SignOutView.as_view(), name='Log-out'),
    path('profile/<pk>/', ProfileView.as_view(), name='Profile'),
    path('about/', AboutPage.as_view(), name="about_page"),
)

from .signals import *
