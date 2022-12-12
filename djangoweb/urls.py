
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from djangoweb.apps.forum.views import CategoryPage



urlpatterns = [
    path('', CategoryPage.as_view(), name="category"),
    path('admin/', admin.site.urls),
    path('users/', include('djangoweb.apps.users.urls')),
    path('forum/', include('djangoweb.apps.forum.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "djangoweb.apps.forum.views.error_404_view"