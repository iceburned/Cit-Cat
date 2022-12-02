
from enum import Enum

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

# User = get_user_model()


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    donotshow = 'DO no\'t show'


class AppUser(AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 30
    AGE_MIN_VALUE = 12
    SIGNATURE_MAX_LENGTH = 255
    CITY_MAX_LENGTH = 30

    username = models.CharField(
        unique=True,
        max_length=MAX_LEN_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
            validators.RegexValidator(
                r"^[a-zA-z0-9_-]+$",
                message="Ensure this value contains only letters, numbers, underscore "
                        "and dashes."
            ),
        ),
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validators.RegexValidator(
                r"^[a-zA-z]+$",
                message="Ensure this value contains only letters and numbers."
            ),
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validators.RegexValidator(
                r"^[a-zA-z]+$",
                message="Ensure this value contains only letters and numbers."
            ),
        ),
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=(
            validators.MinValueValidator(AGE_MIN_VALUE),
            validators.RegexValidator(
                r"^\d+$",
                message="Ensure this value contains only numbers."
            ),
        ),
    )

    avatar_pic = models.ImageField(
        default='/static/users/img/avatars_icon.png',
        blank=True,
        null=True,
    )

    signature = models.TextField(
        max_length=SIGNATURE_MAX_LENGTH,
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        editable=False,
    )

    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.username:
            return self.username
        else:
            return "Anonymous"


class UserProfileModel(models.Model):
    AGE_MIN_VALUE = 12
    SIGNATURE_MAX_LENGTH = 255
    CITY_MAX_LENGTH = 30

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(AGE_MIN_VALUE),
            validators.RegexValidator(
                r"^\d+$",
                message="Ensure this value contains only numbers."
            ),
        ),
    )

    avatar_pic = models.URLField()

    signature = models.TextField(
        max_length=SIGNATURE_MAX_LENGTH,
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        blank=True,
        null=True,
    )
