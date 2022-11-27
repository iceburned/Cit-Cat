from django import forms

from djangoweb.apps.forum.models import ForumTopic


class TopicCreateForm(forms.ModelForm):

    class Meta:
        model = ForumTopic
        fields = '__all__'


class TopicEditForm(forms.ModelForm):

    class Meta:
        model = ForumTopic
        fields = '__all__'