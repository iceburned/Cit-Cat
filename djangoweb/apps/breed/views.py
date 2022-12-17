from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, ListView

from djangoweb.apps.users.models import CatInfo


class CatInfoPageCreate(CreateView):
    pass


class CatInfoPageEdit(UpdateView):
    pass


class CatInfoPage(ListView):
    model = CatInfo
    template_name = 'cat_info_page.html'
    context_object_name = 'cat_info'

    # def get_context_data(self, **kwargs):
    #     context = super(CatInfoPage, self).get_context_data()
    #     context['cat_info'] = CatInfo.objects.all()
    #     a = 1

