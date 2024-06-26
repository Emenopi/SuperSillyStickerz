from django.test import TestCase
from stickerz.models import Sticker

class Sticker_model_tests(TestCase):
    def setUp(self):
        self.valid_sticker_data = {
            "name": "test 1",
            "price": 1.00,
            "category": "test",
        }

        self.invalid_sticker_data = {
            "name": "test 2",
            "price": -1.00,
            "category": "test",
        }
        
        self.free_sticker_data = {
            "name": "test 3",
            "price": 0.00,
            "category": "test",
        }

    def test_valid_stickers_get_created(self):
        sticker, created = Sticker.objects.get_or_create(**self.valid_sticker_data)

        self.assertTrue(created)
        self.assertEqual(sticker.name, self.valid_sticker_data["name"])
        self.assertEqual(sticker.price, self.valid_sticker_data["price"])
        self.assertEqual(sticker.category, self.valid_sticker_data["category"])
        self.assertEqual(sticker.sticker_slug, "test-1")
        #return string should be set to the name of the sticker
        self.assertEqual(sticker.__str__(), "test 1")


    def test_invalid_stickers_dont_get_created(self):
        with self.assertRaises(ValueError):
            sticker, created = Sticker.objects.get_or_create(**self.invalid_sticker_data)


    def test_free_stickers_can_be_created(self):
        sticker, created = Sticker.objects.get_or_create(**self.free_sticker_data)

        self.assertTrue(created)
        self.assertEqual(sticker.price, self.free_sticker_data["price"])


        