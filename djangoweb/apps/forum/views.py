from pathlib import Path


from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Permission, Group
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView


from djangoweb.apps.forum.forms import TopicCreateForm, TopicEditForm, SubcategoryCreateForm, SubcategoryEditForm, \
    CategoryCreateForm, CategoryEditForm
from djangoweb.apps.forum.models import ForumCategory, ForumSubcategories, ForumTopic
from djangoweb.apps.forum.tasks import search_in_cat_api
from djangoweb.apps.users.models import AppUser
from djangoweb.apps.users.tasks import search_in_subcategory
from djangoweb.apps.utils.cat_pics import main_cat
from djangoweb.apps.utils.dad_jokes import main as dad_jokes
from djangoweb.services.ses import SESService
from djangoweb.services.sqs import SQSService


class ListPageBase(ListView):

    def user_name(self):
        if self.request.user.is_anonymous:
            return 'Anonymous'
        else:
            return self.request.user.get_full_name()


class DetailsPageBase(DetailView):
    pass


class EditPageBase(UpdateView):
    pass


class CreatePageBase(CreateView):
    pass


class CategoryPage(ListPageBase):
    model = ForumCategory
    template_name = 'index.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryPage, self).get_context_data()
        context['joke'] = dad_jokes()
        context['cat_of_the_day'] = search_in_cat_api()
        context['cat_of_the_day1'] = search_in_cat_api()
        context['cat_of_the_day2'] = search_in_cat_api()
        context['cat_of_the_day3'] = search_in_cat_api()
        context['cat_of_the_day4'] = search_in_cat_api()
        context['cat_of_the_day5'] = search_in_cat_api()
        context['full_name'] = self.user_name()
        context['user'] = self.request.user
        context['search_flag'] = False
        context['group_admin'] = self.group_privileges()
        # context['avatar'] = self.avatar()
        return context

    def group_privileges(self):
        current_user = self.request.user
        user_groups = current_user.groups
        if user_groups.filter(name='admins'):
            return True
        return False


class CategoryPageCreate(CreatePageBase):
    model = ForumCategory
    template_name = 'category_create.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('category')


class CategoryPageEdit(EditPageBase):
    model = ForumCategory
    template_name = 'category_edit.html'
    form_class = CategoryEditForm
    success_url = reverse_lazy('category')

# LoginRequiredMixin,
# @login_required(login_url=LOGIN_REDIRECT_URL)
# @method_decorator(login_required, name='dispatch')


class SubcategoryPage(LoginRequiredMixin, ListPageBase):
    model = ForumSubcategories

    template_name = 'subcategory_page.html'
    context_object_name = "subcategory_context"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        count_topic = ForumSubcategories.count_topics(self.kwargs.get('pk'))
        last_topic = ForumSubcategories.last_topic(self.kwargs.get('pk'))
        context['count_topics'] = count_topic
        context['last_topic'] = last_topic
        context['subcategory_pk'] = self.kwargs.get("pk")
        context['joke'] = dad_jokes()
        context['full_name'] = self.user_name()
        # context['group_admin'] = self.group_privileges('admins')
        # context['group_mods'] = self.group_privileges('mods')
        context['search_flag'] = True
        context['subcategory_flag'] = True
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

    def group_privileges(self, value):
        current_user = self.request.user
        user_groups = current_user.groups
        if user_groups.filter(name=value):
            return True
        return False


class SubcategoryCreate(LoginRequiredMixin, CreatePageBase):
    model = ForumSubcategories
    template_name = 'subcategory_create.html'
    form_class = SubcategoryCreateForm
    success_url = reverse_lazy('subcategory')

    def get_initial(self):

        initial = super(SubcategoryCreate, self).get_initial()
        initial['category'] = self.kwargs['pk']
        return initial


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['subcategory_pk'] = self.kwargs.get("pk")
        context['category_id'] = self.kwargs.get("pk")
        return context

    def get_success_url(self):
        return reverse('subcategory', kwargs={'pk': self.kwargs['pk']})


class SubcategoryEdit(LoginRequiredMixin, EditPageBase):
    model = ForumSubcategories
    template_name = 'subcategory_create.html'
    form_class = SubcategoryEditForm
    # success_url = reverse_lazy('category')

    pk_url_kwarg = 'ek'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['subcategory_pk'] = self.kwargs.get("pk")
        context['topics_ek'] = self.kwargs['ek']
        a = 1
        return context


class TopicsPage(LoginRequiredMixin, ListPageBase):
    model = ForumTopic
    template_name = 'topics_page.html'
    context_object_name = 'topics_context'
    paginate_by = 10

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
        context['joke'] = dad_jokes()
        context['full_name'] = self.user_name()
        context['group_admin'] = self.group_privileges('admins')
        context['group_mods'] = self.group_privileges('mods')
        context['instance_user'] = self.request.user
        context['search_flag'] = True

        return context

    def group_privileges(self, value):
        current_user = self.request.user
        user_groups = current_user.groups
        if user_groups.filter(name=value):
            return True
        return False


class EditTopicPage(LoginRequiredMixin, EditPageBase):
    model = ForumTopic
    template_name = 'topic_create_page.html'
    context_object_name = 'topic_create_context'
    form_class = TopicCreateForm
    pk_url_kwarg = 'tk'

    def get_success_url(self):
        return reverse('topics', kwargs={'pk': self.kwargs['pk'], 'ek': self.kwargs['ek']})

    def get_context_data(self, **kwargs):
        context = super(EditTopicPage, self).get_context_data()
        kwargs_path = self.request.resolver_match.captured_kwargs
        context['category_pk'] = kwargs_path['pk']
        context['subcategory_ek'] = kwargs_path['ek']
        context['topics_tk'] = kwargs_path['tk']
        return context


class CreateTopicPage(LoginRequiredMixin, CreatePageBase):
    model = ForumTopic
    template_name = 'topic_edit_page.html'
    context_object_name = 'topic_create_context'
    form_class = TopicCreateForm

    def get_initial(self):
        initial = super(CreateTopicPage, self).get_initial()
        initial['subcategory'] = self.kwargs['ek']
        initial['user'] = self.request.user
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['subcategory'] = self.kwargs.get("pk")
        # context['category_id'] = self.kwargs.get("pk")
        return context

    def get_success_url(self):
        return reverse('topics', kwargs={'pk': self.kwargs['pk'], 'ek': self.kwargs['ek']})


class SearchResultView(LoginRequiredMixin, ListPageBase):
    model = ForumSubcategories
    template_name = 'search_subcategories.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query.strip() == '':
            return []
        object_list = ForumSubcategories.objects.filter(
            Q(title__icontains=query) & Q(category_id=self.kwargs["pk"])
        )
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchResultView, self).get_context_data()
        context['query_search'] = self.request.GET.get('q')
        context['joke'] = dad_jokes()
        context['full_name'] = self.user_name()
        context['user'] = self.request.user
        context['search_flag'] = True
        context['subcategory_flag'] = True
        context['subcategory_pk'] = self.kwargs['pk']
        return context


class SearchResultViewTopics(LoginRequiredMixin, ListPageBase):
    model = ForumTopic
    template_name = 'search_topics.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query.strip() == '':
            return []
        object_list = ForumTopic.objects.filter(
            Q(title__icontains=query) & Q(subcategory_id=self.kwargs["ek"])
        )
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchResultViewTopics, self).get_context_data()
        context['query_search'] = self.request.GET.get('q')
        context['joke'] = dad_jokes()
        context['full_name'] = self.user_name()
        context['user'] = self.request.user
        context['subcategory_pk'] = self.kwargs['pk']
        context['topics_ek'] = self.kwargs['ek']
        context['search_flag'] = True
        return context
