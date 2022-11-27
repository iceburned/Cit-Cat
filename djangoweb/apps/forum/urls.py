from django.urls import path, include

from djangoweb.apps.forum.views import CategoryPage, SubcategoryPage, TopicsPage, CreateTopicPage, EditTopicPage

urlpatterns = (
    path('', CategoryPage.as_view(), name="category"),
    path('sub/<int:pk>/', SubcategoryPage.as_view(), name='subcategory'),
    path('sub/<int:pk>/topics/<int:ek>/', TopicsPage.as_view(), name='topics'),
    path('sub/<int:pk>/topics/<int:ek>/edit/<int:tk>/', EditTopicPage.as_view(), name='edit_topic'),
    path('sub/<int:pk>/topics/<int:ek>/create/', CreateTopicPage.as_view(), name='create_topic'),
)
