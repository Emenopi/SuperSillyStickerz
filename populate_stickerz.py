from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from population.populator import Populator
from population.stub_reader import StubReader
from stickerz.models import Sticker, Shopper, Order
from django.contrib.auth.models import User

models = {
    "sticker" : Sticker,
    "user" : User,
    "shopper" : Shopper,
    "order" : Order,
    }
populator = Populator(StubReader(), models)
populator.populate()