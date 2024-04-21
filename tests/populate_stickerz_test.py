from django.test import TestCase
from unittest.mock import patch
from stickerz.models import Sticker, Order, Shopper, User
from population.populator import Populator
from population.stub_reader import StubReader
from population.utils import dict_to_obj
from django.db.utils import IntegrityError

class PopulateStickerzTests(TestCase):

    # run the tests in this file with :
    # $python manage.py test tests.populate_stickerz_test

    def valid_populate(self):
        models = {
            "sticker" : Sticker,
            "user" : User,
            "shopper" : Shopper,
            "order" : Order,
            }
        populator = Populator(StubReader(), models, verbose=False)
        populator.populate()

    def test_populator_populateWithValidData_stickersFilled(self):
        """
        It fills the sticker table
        """
        self.valid_populate()

        first = dict_to_obj(Sticker(), StubReader().get_sticker()[0])
        self.assertEqual(dir(Sticker.objects.first()), dir(first))
        
        last = dict_to_obj(Sticker(), StubReader().get_sticker()[-1])
        self.assertEqual(dir(Sticker.objects.last()), dir(last))

        self.assertEquals(len(Sticker.objects.all()), 6)

    def test_populator_populateWithValidData_usersFilled(self):
        """
        It fills the user table
        """
        self.valid_populate()

        first = dict_to_obj(User(), StubReader().get_user()[0])
        self.assertEqual(dir(User.objects.first()), dir(first))
        
        last = dict_to_obj(User(), StubReader().get_user()[-1])
        self.assertEqual(dir(User.objects.last()), dir(last))

        self.assertEquals(len(User.objects.all()), 2)

    def test_populator_populateWithValidData_shoppersFilled(self):
        """
        It fills the user table
        """
        self.valid_populate()

        first = dict_to_obj(Shopper(), StubReader().get_shopper()[0])
        self.assertEqual(Shopper.objects.first().shippingAddress, first.shippingAddress) # hashing prevents full comparison
        
        last = dict_to_obj(Shopper(), StubReader().get_shopper()[-1])
        self.assertEqual(Shopper.objects.last().shippingAddress, last.shippingAddress) # hashing prevents full comparison

        self.assertEquals(len(Shopper.objects.all()), 2)
