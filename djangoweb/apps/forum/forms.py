from django import forms

from djangoweb.apps.forum.models import ForumTopic, ForumSubcategories, ForumCategory


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = ForumCategory
        fields = ('title', 'description')


class CategoryEditForm(forms.ModelForm):

    class Meta:
        model = ForumCategory
        fields = ('title', 'description')


class TopicCreateForm(forms.ModelForm):

    class Meta:
        model = ForumTopic
        fields = ('title', 'content', 'subcategory', 'user')
        widgets = {
            'subcategory': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }


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



