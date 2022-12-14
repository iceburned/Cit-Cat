
from django.test import TestCase
from django.urls import reverse
from djangoweb.apps.forum.tasks import search_in_cat_api
from djangoweb.apps.utils.dad_jokes import main as dad_jokes


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


class CategoryOtherSiteApiOnlineToResponse(TestCase):

    def test_dad_joke_site__responding_no_error(self):
        try:
            joke = dad_jokes()
            print(('-----------downloaded dad joke-----------'))
        except Exception as ex:
            print(ex)
            self.assertIsNone(ex)

    def test_cat_pics_site__responding_no_error(self):
        try:
            cats_pics = search_in_cat_api()
        except Exception as ex:
            print(ex)
            self.assertIsNone(ex)


