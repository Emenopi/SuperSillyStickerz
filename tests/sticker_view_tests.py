from django.test import TestCase, RequestFactory
from unittest.mock import patch
from stickerz.models import Sticker
from stickerz.views import sticker
from django.utils.text import slugify

class StickerViewTests(TestCase):
    @patch('stickerz.models.Sticker.objects')
    def test_stickerView_mockSticker_stickerDisplayed(self, mock_sticker):
        """
        It returns sticker page with correct title from slug
        """
        # set up mock
        title = "matte matt"
        mock_sticker.get.return_value = Sticker(name=title, sticker_slug=slugify(title))

        # get response
        self.factory = RequestFactory()
        request = self.factory.get('/'+mock_sticker.sticker_slug+"/")
        response = sticker(request, title)

        # check sticker title is in response
        self.assertContains(response, title)

