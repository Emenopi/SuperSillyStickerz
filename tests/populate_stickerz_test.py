from django.test import TestCase
from unittest.mock import patch
from stickerz.models import Sticker, Order, Shopper, User
from population.populator import Populator
from population.stub_reader import StubReader
from population.utils import obj_to_dict
from django.db.utils import IntegrityError

class PopulateStickerzTests(TestCase):

    # run the tests in this file with :
    # $python manage.py test tests.populate_stickerz_test

    # # # example test

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
    def valid_populate(self):
        models = {
            "sticker" : Sticker,
            "user" : User,
            "shopper" : Shopper,
            "order" : Order,
            }
        populator = Populator(StubReader(), models)
        populator.populate(verbose=False)

    def test_populator_populateWithValidData_stickersFilled(self):
        """
        It fills the sticker table
        """
        self.valid_populate()

        first = obj_to_dict(Sticker(), StubReader().get_sticker()[0])
        self.assertEqual(dir(Sticker.objects.first()), dir(first))
        
        last = obj_to_dict(Sticker(), StubReader().get_sticker()[-1])
        self.assertEqual(dir(Sticker.objects.last()), dir(last))

        self.assertEquals(len(Sticker.objects.all()), 6)

    def test_populator_populateWithValidData_usersFilled(self):
        """
        It fills the user table
        """
        self.valid_populate()

        first = obj_to_dict(User(), StubReader().get_user()[0])
        self.assertEqual(dir(User.objects.first()), dir(first))
        
        last = obj_to_dict(User(), StubReader().get_user()[-1])
        self.assertEqual(dir(User.objects.last()), dir(last))

        self.assertEquals(len(User.objects.all()), 2)

    def test_populator_populateWithValidData_shoppersFilled(self):
        """
        It fills the user table
        """
        self.valid_populate()

        first = obj_to_dict(Shopper(), StubReader().get_shopper()[0])
        self.assertEqual(Shopper.objects.first().shippingAddress, first.shippingAddress) # hashing prevents full comparison
        
        last = obj_to_dict(Shopper(), StubReader().get_shopper()[-1])
        self.assertEqual(Shopper.objects.last().shippingAddress, last.shippingAddress) # hashing prevents full comparison

        self.assertEquals(len(Shopper.objects.all()), 2)
