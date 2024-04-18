from django.test import TestCase, RequestFactory
from django.urls import reverse
from stickerz.models import Sticker
from django.contrib.auth.models import AnonymousUser

class IndexViewTests(TestCase):
    def test_index_view_exits(self):
        """
        If database is empty, returns empty dict.
        """
        response = self.client.get(reverse('stickerz:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_categories(self):
        response = self.client.get(reverse('stickerz:index'))
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_one_category(self):
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

    def test_index_view_login_link(self):
        # setup request factory
        self.factory = RequestFactory()
        # make request
        request = self.factory.get('/index/')
        # set user as logged out user
        request.user = AnonymousUser()
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

