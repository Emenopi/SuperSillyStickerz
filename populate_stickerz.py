from population.populator import Populator
from population.stub_reader import StubReader
from stickerz.models import Sticker, Shopper, Order
from django.contrib.auth.models import User

models = {
    "sticker" : Sticker,
    "shopper" : Shopper,
    "order" : Order,
    "user" : User,
    }
populator = Populator(StubReader(), models)
populator.populate()