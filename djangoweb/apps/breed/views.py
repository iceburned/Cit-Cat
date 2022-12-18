
from django.views.generic import UpdateView, CreateView, ListView

from djangoweb.apps.users.models import CatInfo


class CatInfoPageCreate(CreateView):
    pass


class CatInfoPageEdit(UpdateView):
    pass


class CatInfoPage(ListView):
    model = CatInfo
    template_name = 'cat_info_page.html'
    context_object_name = 'cat_info'


