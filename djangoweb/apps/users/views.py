from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic


from djangoweb.apps.users.forms import ProfileForm, AboutPageForm
from djangoweb.apps.users.models import UserProfileModel, AboutData

User = get_user_model()


class SignUpBaseForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        field_classes = {'username': UsernameField}


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


class ProfileView(generic.UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = ProfileForm
    context_object_name = 'profile'

    def get_success_url(self):
        return reverse_lazy('Profile', kwargs={'pk': self.kwargs['pk']})


    # def post(self, request, *args, **kwargs):
    #     post = super(ProfileView, self).post(request, *args, **kwargs)
    #     form = ProfileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         name = form.cleaned_data.get("name")
    #         img = form.cleaned_data.get("geeks_field")
    #         obj = User.objects.create(
    #             title = name,
    #             img = img
    #         )
    #         obj.save()
    #         print(obj)
    #
    #
    #     return post

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileView, self).get_context_data()

        # id_instance = self.kwargs['pk']
        # context['profile_model'] = UserProfileModel.objects.get(user_id=id_instance)
        # return context

#
# def send_email_to_new_users():
#     pass

class AboutPage(generic.CreateView):
    model = AboutData
    template_name = 'about_page.html'
    form_class = AboutPageForm
    success_url = reverse_lazy('category')


