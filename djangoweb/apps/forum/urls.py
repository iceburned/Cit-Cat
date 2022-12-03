from django.urls import path

from djangoweb.apps.forum.views import *

urlpatterns = (
    path('', CategoryPage.as_view(), name="category"),
    path('sub/<int:pk>/', SubcategoryPage.as_view(), name='subcategory'),
    path('sub/<int:pk>/topics/<int:ek>/', TopicsPage.as_view(), name='topics'),
    path('sub/<int:pk>/topics/<int:ek>/edit/<int:tk>/', EditTopicPage.as_view(), name='edit_topic'),
    path('sub/<int:pk>/topics/<int:ek>/create/', CreateTopicPage.as_view(), name='create_topic'),
    path('sub/<int:pk>/search/', SearchResultView.as_view(), name="search"),
    path('sub/<int:pk>/topics/<int:ek>/search/', SearchResultViewTopics.as_view(), name="search"),
)
