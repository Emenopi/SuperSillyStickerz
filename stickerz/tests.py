from django.test import TestCase, RequestFactory
from unittest.mock import MagicMock, patch
from stickerz.models import Sticker
from stickerz.views import sticker

class Calculator():
    def hello(self):
        return "hello"

class CategoryMethodTests(TestCase):
    factory = RequestFactory()

    def test_sticker_happens(self):
        sticker = Sticker(name='window', image='asdf', price='1.99', category="Cats", sticker_slug='window')
        sticker.save()
        self.assertEqual((sticker.name == "window"), True)

    @patch('stickerz.models.Sticker.objects')
    def test_displaysSticker(self, mock_sticker): # pass in one sticker and verify it is displayed on index
        mock_sticker.all.return_value = "hi"

        sticker = Sticker()
        x = sticker.objects.all()

        self.assertEqual((x == "hi"), True)

    @patch('stickerz.models.Sticker.objects')
    def test_displaysStickerPage(self, mock_sticker): # pass in one sticker and verify it is displayed on index
        #set up test
        WINDOW_CAT = "window-cat"
        title = "uofgisverycool"
        mock_sticker.get.return_value = Sticker(name=title)#, image='asdf', price='1.99', category="Cats", sticker_slug=WINDOW_CAT)

        # get response
        request = self.factory.get('/customer/details')
        response = sticker(request, WINDOW_CAT)

        #assert results
        if title in str(response.content):
            displays = True
        else:
            displays = False
        self.assertEqual((displays), True)

    def test_calc(self):
        calc = Calculator()
        calc.hello = MagicMock(return_value="hi")
        self.assertEqual((calc.hello() == "hi"), True)

