from django.test import TestCase, RequestFactory
from unittest.mock import MagicMock, patch
from stickerz.models import Sticker
from stickerz.views import sticker

class Sticker_model_tests(TestCase):
    valid_mock_sticker = Sticker(name="test_1", price=1.00, category="test", sticker_slug="test_1")
    
    
    @patch('stickerz.models.Sticker.save')
    def test_valid_stickers_get_created(self, valid_mock_sticker):
        
        result = Sticker.objects.get_or_create(valid_mock_sticker)

        self.assertTrue(result, True)


    