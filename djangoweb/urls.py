
from django.conf import settings
from django.contrib import admin

from django.urls import path, include
from django.conf.urls.static import static


from djangoweb.apps.forum.views import CategoryPage
from djangoweb.apps.utils.error_handler_500 import custom_handler500


urlpatterns = [
    path('', CategoryPage.as_view(), name="category"),
    path('admin/', admin.site.urls),
    path('users/', include('djangoweb.apps.users.urls')),
    path('forum/', include('djangoweb.apps.forum.urls')),
    path('breed/', include('djangoweb.apps.breed.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler500 = custom_handler500
