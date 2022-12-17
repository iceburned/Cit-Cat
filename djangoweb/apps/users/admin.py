from django.contrib import admin
from django.contrib.auth import get_user_model

from djangoweb.apps.users.models import CatInfo, UserProfileModel

UserModel = get_user_model()


# class UserProfileModelAdmin(admin.StackedInline):
#     model = UserProfileModel
#     list_display = ('user',)


@admin.register(UserModel)
class UserAdmins(admin.ModelAdmin):
    list_display = ('username', 'age')
    # inlines = [
    #     UserProfileModelAdmin,
    # ]


@admin.register(CatInfo)
class CatInfoAdmins(admin.ModelAdmin):
    list_display = ('name',)


# class BookInline(admin.TabularInline):
#     model = Book
#
# class AuthorAdmin(admin.ModelAdmin):
#     inlines = [
#         BookInline,
#     ]