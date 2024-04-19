from unittest import mock
from django.core.files import File
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.conf import settings
from unittest.mock import patch
from django.utils.text import slugify
from stickerz.models import Sticker
from stickerz.views import index

class IndexViewTests(TestCase):

   # patch "passes in" mock_sticker
    @patch('stickerz.models.Sticker.objects.all')
    @patch('stickerz.models.Sticker.objects.exclude')
    @patch('stickerz.models.Sticker.objects')
    def test_indexView_single_mockSticker_stickerDisplayed(self, mock_all, mock_exclude, mock_sticker_objects):
        """
        It returns sticker in response
        """
        # set up request factory
        factory = RequestFactory()
        request = factory.get('/stickerz/')
        #set up mock sticker
        title = "matte matt"
        mock_sticker = [Sticker(name=title, sticker_slug = slugify(title), category="people")]
        mock_all.return_value = mock_sticker
        mock_exclude.return_value = mock_sticker
        mock_sticker_objects.return_value = mock_sticker

        # get response
        response = index(request)

        #assert results
        self.assertContains(response, title)