from django.urls import path

from djangoweb.apps.forum.views import *

urlpatterns = (
    path('', CategoryPage.as_view(), name="category"),
    path('create/', CategoryPageCreate.as_view(), name="category_create"),
    path('edit/<int:pk>/', CategoryPageEdit.as_view(), name="category_edit"),
    path('sub/<int:pk>/', SubcategoryPage.as_view(), name='subcategory'),
    path('sub/<int:pk>/create/', SubcategoryCreate.as_view(), name='subcategory_create'),
    path('sub/<int:pk>/edit/<int:ek>/', SubcategoryEdit.as_view(), name='subcategory_edit'),
    path('sub/<int:pk>/topics/<int:ek>/', TopicsPage.as_view(), name='topics'),
    path('sub/<int:pk>/topics/<int:ek>/edit/<int:tk>/', EditTopicPage.as_view(), name='edit_topic'),
    path('sub/<int:pk>/topics/<int:ek>/create/', CreateTopicPage.as_view(), name='create_topic'),
    path('sub/<int:pk>/search/', SearchResultView.as_view(), name="search"),
    path('sub/<int:pk>/topics/<int:ek>/search/', SearchResultViewTopics.as_view(), name="search"),

)
