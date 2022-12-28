from django.urls import path

from djangoweb.apps.breed.views import CatInfoPage

urlpatterns = (
    path('cat_info_page/', CatInfoPage.as_view(), name="cat_info"),
)
