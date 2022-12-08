from django import forms

from djangoweb.apps.forum.models import ForumTopic, ForumSubcategories


class TopicCreateForm(forms.ModelForm):

    class Meta:
        model = ForumTopic
        fields = '__all__'


class TopicEditForm(forms.ModelForm):

    class Meta:
        model = ForumTopic
        fields = '__all__'


class SubcategoryCreateForm(forms.ModelForm):

    class Meta:
        model = ForumSubcategories
        fields = ('title', 'description', 'category')
        widgets = {
            'category': forms.HiddenInput(),
        }


class SubcategoryEditForm(forms.ModelForm):

    class Meta:
        model = ForumSubcategories

        fields = ('title', 'description')
        # widgets = {
        #     'category': forms.HiddenInput(),
        # }
