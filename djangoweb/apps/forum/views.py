
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from djangoweb.apps.forum.forms import TopicCreateForm, SubcategoryCreateForm, SubcategoryEditForm, \
    CategoryCreateForm, CategoryEditForm
from djangoweb.apps.forum.models import ForumCategory, ForumSubcategories, ForumTopic
from djangoweb.apps.forum.tasks import search_in_cat_api
from djangoweb.apps.utils.dad_jokes import main as dad_jokes
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required


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


class DeletePageBase(DeleteView):
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
        return context


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryPageCreate(CreatePageBase):
    model = ForumCategory
    template_name = 'category_create.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('category')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryPageEdit(EditPageBase):
    model = ForumCategory
    template_name = 'category_edit.html'
    form_class = CategoryEditForm
    success_url = reverse_lazy('category')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryPageDelete(DeletePageBase):
    model = ForumCategory
    template_name = 'delete.html'
    success_url = reverse_lazy('category')


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


@method_decorator(staff_member_required, name='dispatch')
class SubcategoryCreate(CreatePageBase):
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


@method_decorator(staff_member_required, name='dispatch')
class SubcategoryEdit(EditPageBase):
    model = ForumSubcategories
    template_name = 'subcategory_edit.html'
    form_class = SubcategoryEditForm
    pk_url_kwarg = 'ek'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['subcategory_pk'] = self.kwargs.get("pk")
        context['topics_ek'] = self.kwargs['ek']
        return context

    def get_success_url(self):
        return reverse('subcategory', kwargs={'pk': self.kwargs['pk']})


@method_decorator(staff_member_required, name='dispatch')
class SubcategoryDelete(DeletePageBase):
    model = ForumSubcategories
    template_name = 'delete.html'
    pk_url_kwarg = 'ek'

    def get_success_url(self):
        return reverse('subcategory', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['subcategory_pk'] = self.kwargs.get("pk")
        context['topics_ek'] = self.kwargs['ek']
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
        context['instance_user'] = self.request.user
        context['search_flag'] = True
        return context


class EditTopicPage(LoginRequiredMixin, EditPageBase):
    model = ForumTopic
    template_name = 'topic_edit_page.html'
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
    template_name = 'topic_create_page.html'
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
        return context

    def get_success_url(self):
        return reverse('topics', kwargs={'pk': self.kwargs['pk'], 'ek': self.kwargs['ek']})


class TopicPageDelete(LoginRequiredMixin, DeletePageBase):
    model = ForumTopic
    template_name = 'delete.html'
    pk_url_kwarg = 'tk'

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
