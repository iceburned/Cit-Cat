from django.contrib import admin
from django.contrib.auth import get_user_model

from djangoweb.apps.users.models import CatInfo

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmins(admin.ModelAdmin):
    list_display = ('username', 'age')


@admin.register(CatInfo)
class CatInfoAdmins(admin.ModelAdmin):
    list_display = ('name',)
