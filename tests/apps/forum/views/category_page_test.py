from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.urls import reverse
from django.utils import timezone

from djangoweb.apps.forum.models import ForumCategory
from djangoweb.apps.forum.views import CategoryPage
from djangoweb.apps.users.models import AppUser

# User = get_user_model()


class AppUserModelTests(TestCase):
    def setUp(self):
        self.regular_user = {
            'username': "Teo",
            'email': "asd@abv.bg",

        }

    def test_username_not_allowed_characters(self):
        u = AppUser(
            username="#$%",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='Teo',
            gender='male',
        )
        try:
            u.full_clean()
            u.save()
            self.fail()

        except ValidationError as ex:
            print(ex.messages)
            self.assertIsNotNone(ex)

    def test_username__allowed_characters(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='Teo',
            gender='male',
        )

        u.full_clean()
        u.save()

        self.assertIsNotNone(u)

    def test_first_name_not_only_letters(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo1',
            last_name='Teo',
            gender='male',
        )

        try:
            u.full_clean()
            u.save()
            self.fail()

        except ValidationError as ex:
            print(ex.messages)
            self.assertIsNotNone(ex)

    def test_first_name__only_letters(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='Teo',
            gender='male',
        )

        u.full_clean()
        u.save()
        self.assertIsNotNone(u)

    def test_last_name_not_only_letters(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='T1eo11',
            gender='male',
        )

        try:
            u.full_clean()
            u.save()
            self.fail()

        except ValidationError as ex:
            print(ex.messages)
            self.assertIsNotNone(ex)

    def test_last_name__only_letters(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='Teo',
            gender='male',
        )

        u.full_clean()
        u.save()
        self.assertIsNotNone(u)

    def test_age_not_only_digits(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='Teo',
            gender='male',
            age='22a',
        )

        try:
            u.full_clean()
            u.save()
            self.fail()

        except ValidationError as ex:
            print(ex.messages)
            self.assertIsNotNone(ex)

    def test_age__only_digits(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='Teo',
            gender='male',
            age=22
        )

        u.full_clean()
        u.save()
        self.assertIsNotNone(u)

    def test_if_no_avatar_pic_is_present_in_database_then_put_default(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='Teo',
            gender='male',
            avatar_pic='',
        )
        image = u.avatar()
        self.assertEquals(image, '/media/avatars_icon.png')

    def test_if__avatar_pic_is_present_in_database_then_put_saved(self):
        u = AppUser(
            username="Teo",
            email="asd@abv.bg",
            password='LAPTOP-AJJSFUCE',
            first_name='Teo',
            last_name='Teo',
            gender='male',
            avatar_pic='/cat_12342536245678.jpg',
        )
        image = u.avatar()
        self.assertEquals(image.title().lower(), '/media/cat_12342536245678.jpg')


class CategoryPageResponseTests(TestCase):

    def test_category_page_status_code_is_200(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('category'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('category'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
