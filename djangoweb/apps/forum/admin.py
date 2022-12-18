from django.contrib import admin

from djangoweb.apps.forum.models import ForumCategory, ForumSubcategories, ForumTopic


@admin.register(ForumCategory)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'slug', 'logo')
    list_display = ('title', 'description', 'slug')


@admin.register(ForumSubcategories)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')


@admin.register(ForumTopic)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug')


