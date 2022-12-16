from django.urls import path


from djangoweb.apps.forum.views import *
from djangoweb.apps.utils.error_handler_500 import custom_handler500

urlpatterns = (
    path('create/', CategoryPageCreate.as_view(), name="category_create"),
    path('edit/<int:pk>/', CategoryPageEdit.as_view(), name="category_edit"),
    path('delete/<int:pk>/', CategoryPageDelete.as_view(), name="category_delete"),
    path('sub/<int:pk>/', SubcategoryPage.as_view(), name='subcategory'),
    path('sub/<int:pk>/create/', SubcategoryCreate.as_view(), name='subcategory_create'),
    path('sub/<int:pk>/edit/<int:ek>/', SubcategoryEdit.as_view(), name='subcategory_edit'),
    path('sub/<int:pk>/delete/<int:ek>/', SubcategoryDelete.as_view(), name='subcategory_delete'),
    path('sub/<int:pk>/topics/<int:ek>/', TopicsPage.as_view(), name='topics'),
    path('sub/<int:pk>/topics/<int:ek>/edit/<int:tk>/', EditTopicPage.as_view(), name='edit_topic'),
    path('sub/<int:pk>/topics/<int:ek>/delete/<int:tk>/', TopicPageDelete.as_view(), name='topic_delete'),
    path('sub/<int:pk>/topics/<int:ek>/create/', CreateTopicPage.as_view(), name='create_topic'),
    path('sub/<int:pk>/search/', SearchResultView.as_view(), name="search"),
    path('sub/<int:pk>/topics/<int:ek>/search/', SearchResultViewTopics.as_view(), name="search_topic"),


)


handler500 = custom_handler500
