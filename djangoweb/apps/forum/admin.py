from django.contrib import admin

from djangoweb.apps.forum.models import ForumCategory, ForumSubcategories, ForumTopic


@admin.register(ForumCategory)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ForumSubcategories)
class SubcategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ForumTopic)
class PostAdmin(admin.ModelAdmin):
    pass
