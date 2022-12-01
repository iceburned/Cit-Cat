from pathlib import Path

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView


from djangoweb.apps.forum.forms import TopicCreateForm, TopicEditForm
from djangoweb.apps.forum.models import ForumCategory, ForumSubcategories, ForumTopic
from djangoweb.apps.utils.cat_pics import main_cat
from djangoweb.apps.utils.dad_jokes import main as dad_jokes

User = get_user_model()

class ListPageBase(ListView):
    pass


class DetailsPageBase(DetailView):
    pass


class EditPageBase(UpdateView):
    pass


class CreatePageBase(CreateView):
    pass


class CategoryPage(ListPageBase):
    model = ForumCategory
    template_name = 'category_page.html'

    def user_name(self):
        if self.request.user.is_anonymous:
            return 'Anonymous'
        else:
            return self.request.user.get_full_name()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryPage, self).get_context_data()
        context['joke'] = dad_jokes()
        context['cat_of_the_day'] = main_cat()
        context['full_name'] = self.user_name()
        context['user'] = self.request.user
        return context


class SubcategoryPage(ListPageBase):
    model = ForumSubcategories
    template_name = 'subcategory_page.html'
    context_object_name = "subcategory_context"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        count_topic = ForumSubcategories.count_topics(self.kwargs.get('pk'))
        last_topic = ForumSubcategories.last_topic(self.kwargs.get('pk'))
        context['count_topics'] = count_topic
        context['last_topic'] = last_topic
        context['subcategory_pk'] = self.kwargs.get("pk")
        context['joke'] = dad_jokes()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if_present = self.kwargs.get('pk')
        if if_present:
            queryset = ForumSubcategories.objects.filter(category_id=if_present
                                                         ).order_by('-date_created')
            return queryset
        else:
            return queryset.none()


class TopicsPage(ListPageBase):
    model = ForumTopic
    template_name = 'topics_page.html'
    context_object_name = 'topics_context'

    def get_queryset(self):
        queryset = super().get_queryset()
        if_present = self.kwargs.get('ek')
        if if_present:
            queryset = ForumTopic.objects.filter(subcategory_id=if_present
                                                 ).order_by("-date_created")
            return queryset
        else:
            return queryset.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic_id'] = self.kwargs['ek']
        context['subcategory_pk'] = self.kwargs['pk']
        context['topics_ek'] = self.kwargs['ek']
        return context


class EditTopicPage(EditPageBase):
    model = ForumTopic
    template_name = 'topic_create_page.html'
    context_object_name = 'topic_create_context'
    form_class = TopicCreateForm

    def get_success_url(self):
        return reverse('topics', kwargs={'pk': self.kwargs['pk'], 'ek': self.kwargs['ek']})

    def get_context_data(self, **kwargs):
        context = super(EditTopicPage, self).get_context_data()
        kwargs_path = self.request.resolver_match.captured_kwargs
        context['category_pk'] = kwargs_path['pk']
        context['subcategory_ek'] = kwargs_path['ek']
        context['topics_tk'] = kwargs_path['tk']
        return context


class CreateTopicPage(CreatePageBase):
    model = ForumTopic
    template_name = 'topic_edit_page.html'
    context_object_name = 'topic_create_context'
    form_class = TopicEditForm

    def get_success_url(self):
        return reverse('topics', kwargs={'pk': self.kwargs['pk'], 'ek': self.kwargs['ek']})


