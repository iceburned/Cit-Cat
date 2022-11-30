from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models


User = get_user_model()


class ForumCategory(models.Model):
    __TITLE_MAX_LENGTH = 50
    __TITLE_MIN_LENGTH = 3
    __DESCRIPTION_MAX_LENGTH = 150

    title = models.CharField(
        unique=True,
        max_length=__TITLE_MAX_LENGTH,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(
                __TITLE_MIN_LENGTH),
        ),
    )

    description = models.CharField(
        max_length=__DESCRIPTION_MAX_LENGTH,
        blank=True,
        null=True,
    )

    date_created = models.TimeField(
        auto_now=True,
    )

    def subcategories(self):
        return ForumSubcategories.objects.filter(
            category_id=self.id
        ).order_by('date_created').reverse()[:5]

    logo = models.ImageField(
        default='',
        upload_to='forum/static_images',
    )

    def __str__(self):
        return self.title

    slug = models.SlugField(
        unique=True,
        editable=False,
    )


class ForumSubcategories(models.Model):
    __TITLE_MAX_LENGTH = 50
    __TITLE_MIN_LENGTH = 3
    __DESCRIPTION_MAX_LENGTH = 150

    title = models.CharField(
        unique=True,
        max_length=__TITLE_MAX_LENGTH,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(
                __TITLE_MIN_LENGTH),
        ),
    )

    description = models.CharField(
        max_length=__DESCRIPTION_MAX_LENGTH,
        blank=True,
        null=True,
    )

    date_created = models.TimeField(
        auto_now=True,
    )

    category = models.ForeignKey(
        ForumCategory,
        on_delete=models.CASCADE,
    )

    slug = models.SlugField(
        unique=True,
        editable=False,
    )

    def count_topics(self):
        count_topics = ForumTopic.objects.filter(subcategory_id=self).count()
        return count_topics

    def last_topic(self):
        last_post = ForumTopic.objects.filter(subcategory_id=self)
        return last_post.order_by("date_created").last()

    def __str__(self):
        return self.title


class ForumTopic(models.Model):
    __TITLE_MAX_LENGTH = 50
    __TITLE_MIN_LENGTH = 3
    __CONTENT_MAX_LENGTH = 255

    title = models.CharField(

        max_length=__TITLE_MAX_LENGTH,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(
                __TITLE_MIN_LENGTH),
        ),
    )

    content = models.TextField(
        max_length=__CONTENT_MAX_LENGTH,
        blank=True,
        null=True,
    )

    date_created = models.TimeField(
        auto_now=True,
    )

    slug = models.SlugField(
        unique=True,
        editable=False,
    )

    subcategory = models.ForeignKey(ForumSubcategories, on_delete=models.CASCADE)
    # users = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
