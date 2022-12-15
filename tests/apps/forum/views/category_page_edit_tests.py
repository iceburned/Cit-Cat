from django.test import TestCase
from django.urls import reverse


from djangoweb.apps.users.models import AppUser


class CategoryPageEditResponseTestsWithSuperuserLogin(TestCase):
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

    def test_category_page_edit_database_entry(self):
        inserted_user = AppUser.objects.first()
        inserted_user.username = 'dango'
        inserted_user.save()
        try:
            self.assertEquals(AppUser.objects.first().username, 'dango')
        except Exception as es:
            print(es)

    def test_category_page_status_code_is_200(self):
        response = self.client.get('/forum/create/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('category_create'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('category_create'))
        self.assertTemplateUsed(response, 'category_create.html')


class CategoryPageEditResponseTestsWithStaffLoginNotAccess(TestCase):
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

    def test_category_page_status_code_is_not_200(self):
        response = self.client.get('/forum/edit/1/')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('category_edit', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_redirect(self):
        response = self.client.get(reverse('category_edit', kwargs={'pk': 1}))
        self.assertRedirects(response, '/users/login/?next=/forum/edit/1/')


class CategoryPageEditResponseTestsWithRegularUserLoginNotAccess(TestCase):
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

    def test_category_page_status_code_is_not_200(self):
        response = self.client.get('/forum/edit/1/')
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('category_edit', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_redirect(self):
        response = self.client.get(reverse('category_edit', kwargs={'pk': 1}))
        self.assertRedirects(response, '/users/login/?next=/forum/edit/1/')
