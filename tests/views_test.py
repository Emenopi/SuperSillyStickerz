from django.test import TestCase, RequestFactory
from django.urls import reverse
from stickerz.models import Sticker
from django.test.client import RequestFactory
class IndexViewTests(TestCase):
    def test_index_view_exits(self):
        """
        It returns successful status code when called
        """
        response = self.client.get(reverse('stickerz:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_categories(self):
        """
        It returns empty dict when database is empty.
        """
        response = self.client.get(reverse('stickerz:index'))
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_one_category(self):
        """
        It returns matching category in context dict when database has one non-custom category.
        """
        # Add sticker to db
        add_sticker('teapot', 'kitchen')
        # get response
        response = self.client.get(reverse('stickerz:index'))
        # check response is successful
        self.assertEqual(response.status_code, 200)
        # check only 1 category returned in context_dict
        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 1)
        # check context_dict category is correct
        self.assertContains(response, "kitchen")

    def test_index_view_custom_category(self):
        """
        It returns empty context dict when database has only custom category.
        """
        # Add sticker to db
        add_sticker('teapot', 'Custom')
        # get response
        response = self.client.get(reverse('stickerz:index'))
        # check response is successful
        self.assertEqual(response.status_code, 200)
        # test no categories in context dict
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_login_link(self):
        """
        It returns login link and not dashboard link when user is not authenticated.
        """
        # setup request factory
        self.factory = RequestFactory()
        # make request
        request = self.factory.get('/index/')
        # set user as logged out user
        request.user = MockUser()
        # get response
        response= self.client.get( "/stickerz/" )
        # check login link shows
        self.assertContains(response, '<a class="fixed-right" href="%s">' % reverse('stickerz:login'))
        # check dashboard link doesn't show
        self.assertNotContains(response, '<a class="fixed-right" href="%s">' % reverse('stickerz:dashboard'))  

"""
    Add one sticker for testing
"""
def add_sticker(name, category, price=1):
    sticker = Sticker.objects.get_or_create(name=name, category=category, price=price)[0]
    sticker.save()
    return sticker

