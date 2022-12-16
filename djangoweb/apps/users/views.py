from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic


from djangoweb.apps.users.forms import ProfileForm, AboutPageForm, SignUpBaseForm
from djangoweb.apps.users.models import AboutData

User = get_user_model()


class RegisterUserView(generic.CreateView):
    template_name = 'sign-up.html'
    form_class = SignUpBaseForm
    success_url = reverse_lazy('category')


class SignInView(LoginView):
    template_name = 'sign-in.html'
    success_url = reverse_lazy('category')


class SignOutBaseForm(LogoutView):
    pass


class SignOutView(SignOutBaseForm):
    next_page = reverse_lazy('category')


class ProfileView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = ProfileForm
    context_object_name = 'profile'

    def get_success_url(self):
        return reverse_lazy('Profile', kwargs={'pk': self.kwargs['pk']})


class AboutPage(generic.CreateView):
    model = AboutData
    template_name = 'about_page.html'
    form_class = AboutPageForm
    success_url = reverse_lazy('category')


# def handler500(request, *args, **kwargs):
#     template = loader.get_template('505.html')
#
#     response.status_code = 500
#     return HttpResponse(template.render(request))
