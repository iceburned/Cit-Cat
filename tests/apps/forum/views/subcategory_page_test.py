from django.test import TestCase
from django.urls import reverse

from djangoweb.apps.users.models import AppUser


class CategoryPageResponseTests(TestCase):
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
        response = self.client.get('forum/sub/1/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('subcategory', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('subcategory', kwargs={'pk': 1}))
        self.assertTemplateUsed(response, 'subcategory_page.html')
