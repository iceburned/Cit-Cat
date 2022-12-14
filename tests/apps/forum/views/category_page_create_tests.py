from django.test import TestCase
from django.urls import reverse

from djangoweb.apps.users.models import AppUser


class CategoryPageCreateResponseTestsWithSuperuserLogin(TestCase):
    def setUp(self):
        u = {
            "username": "django",
            "email": "asd@abv.bg",
            "password": 'LAPTOP-AJJSFUCE',
            "first_name": 'Teo',
            "last_name": 'Teo',
            "gender": 'male',
        }
        self.admin = AppUser.objects.create_superuser(**u)
        self.client.login(username='django', password='LAPTOP-AJJSFUCE')

    def test_category_page_database_entry(self):
        inserted_user = AppUser.objects.first().username
        self.assertEquals(inserted_user, 'django')

    def test_category_page_status_code_is_200(self):
        response = self.client.get('/forum/create/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('category_create'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('category_create'))
        self.assertTemplateUsed(response, 'category_create.html')


class CategoryPageCreateResponseTestsWithStaffLoginNotAccess(TestCase):
    def setUp(self):
        u = {
            "username": "django",
            "email": "asd@abv.bg",
            "password": 'LAPTOP-AJJSFUCE',
            "first_name": 'Teo',
            "last_name": 'Teo',
            "gender": 'male',
        }
        self.moderator = AppUser.objects.create_user(**u)
        self.moderator.is_staff = True
        self.moderator.save()
        self.client.login(username='django', password='LAPTOP-AJJSFUCE')

    def test_category_page_status_code_is_200(self):
        response = self.client.get('/forum/create/')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('category_create'))
        self.assertNotEqual(response.status_code, 200)

    def test_view_uses_correct_redirect(self):
        response = self.client.get(reverse('category_create'))
        self.assertRedirects(response, '/users/login/?next=/forum/create/')


class CategoryPageCreateResponseTestsWithRegularUserLoginNotAccess(TestCase):
    def setUp(self):
        u = {
            "username": "django",
            "email": "asd@abv.bg",
            "password": 'LAPTOP-AJJSFUCE',
            "first_name": 'Teo',
            "last_name": 'Teo',
            "gender": 'male',
        }
        self.regular_user = AppUser.objects.create_user(**u)
        self.client.login(username='django', password='LAPTOP-AJJSFUCE')

    def test_category_page_status_code_is_200(self):
        response = self.client.get('/forum/create/')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('category_create'))
        self.assertNotEqual(response.status_code, 200)

    def test_view_uses_correct_redirect(self):
        response = self.client.get(reverse('category_create'))
        self.assertRedirects(response, '/users/login/?next=/forum/create/')



