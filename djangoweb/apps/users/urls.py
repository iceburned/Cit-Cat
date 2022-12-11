from django.urls import path
from .views import RegisterUserView, SignInView, SignOutView, ProfileView, AboutPage
from .signals import *


urlpatterns = (
    path('reg/', RegisterUserView.as_view(), name='Register'),
    path('login/', SignInView.as_view(), name='Log-in'),
    path('logout/', SignOutView.as_view(), name='Log-out'),
    path('profile/<pk>/', ProfileView.as_view(), name='Profile'),
    path('about/', AboutPage.as_view(), name="about_page"),
)


