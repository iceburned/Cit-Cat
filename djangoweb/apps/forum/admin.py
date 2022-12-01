from django.contrib import admin

from djangoweb.apps.forum.models import ForumCategory, ForumSubcategories, ForumTopic


@admin.register(ForumCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    # prepopulated_fields = {"slug": ("title",)}


@admin.register(ForumSubcategories)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    # prepopulated_fields = {"slug": ("title",)}


@admin.register(ForumTopic)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug')


