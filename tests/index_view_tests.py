from django.test import TestCase, RequestFactory
from unittest.mock import patch
from django.utils.text import slugify
from stickerz.models import Sticker
from stickerz.views import index

class IndexViewTests(TestCase):

   # patch "passes in" mocks
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

    # patch "passes in" mocks
    @patch('stickerz.models.Sticker.objects.all')
    @patch('stickerz.models.Sticker.objects.exclude')
    @patch('stickerz.models.Sticker.objects')
    def test_indexView_multi_mockSticker_stickerDisplayed(self, mock_all, mock_exclude, mock_sticker_objects):
        """
        It returns sticker in response
        """
        # set up request factory
        factory = RequestFactory()
        request = factory.get('/stickerz/')
        #set up mock stickers
        title_matt = "matte matt"
        title_derek = "gloss derek"
        title_wim = "holographic wim"
        mock_stickers = [Sticker(name=title_matt, sticker_slug = slugify(title_matt), category='celebrities'),
                         Sticker(name=title_derek, sticker_slug = slugify(title_derek), category='fashion'),
                         Sticker(name=title_wim, sticker_slug = slugify(title_wim), category='tech'),]
        mock_all.return_value = mock_stickers
        mock_exclude.return_value = mock_stickers
        mock_sticker_objects.return_value = mock_stickers

        # get response
        response= self.client.get( "/stickerz/" )

        #assert results
        self.assertQuerysetEqual(response.context['categories'], ["'celebrities'", "'fashion'", "'tech'"])
        self.assertQuerysetEqual(response.context['stickers'], ['<Sticker: %s>' % mock_stickers[0], '<Sticker: %s>' % mock_stickers[1], '<Sticker: %s>' % mock_stickers[2]])