import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperSillyStickerz.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from population.populator import Populator
from population.stub_reader import StubReader
from population.csv_reader import CsvReader
from stickerz.models import Sticker, Shopper, Order
from django.contrib.auth.models import User

models = {
    "sticker" : Sticker,
    "user" : User,
    "shopper" : Shopper,
    "order" : Order,
    }
populator = Populator(CsvReader(), models)
populator.populate()