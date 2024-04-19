from django.test import TestCase, RequestFactory
from unittest.mock import patch
from stickerz.models import Sticker
from stickerz.views import sticker

class CategoryMethodTests(TestCase):
    factory = RequestFactory()

    # run the tests in this file with :
    # $python manage.py test tests.views_test

    # # example test

    # # patch "passes in" mock_sticker
    # @patch('stickerz.models.Sticker.objects')
    # # name must start with test_ to run
    # # format of name is test_thingBeingTested_input_expectedOutput
    # def test_stickerView_mockSticker_stickerDisplayed(self, mock_sticker):
    #     #set up test
    #     title = "matte matt"
    #     title_slug = "matte-matt"
    #     mock_sticker.get.return_value = Sticker(name=title)

    #     # get response
    #     request = self.factory.get('/'+title_slug+"/")
    #     response = sticker(request, title)

    #     #assert results
    #     self.assertContains(response, title) # asserts response contains title