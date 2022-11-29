from django.contrib import admin
from django.contrib.auth import get_user_model, admin as auth_admin

from djangoweb.apps.users.models import UserProfileModel

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    pass


@admin.register(UserProfileModel)
class UserProfile(admin.ModelAdmin):
    pass
