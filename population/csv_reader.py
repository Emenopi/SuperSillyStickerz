from django.contrib.auth.models import User
from stickerz.models import Sticker, Shopper
from population.reader import Reader
from population.utils import create_obj_by_attr
import decimal
import csv
import os

class CsvReader(Reader):
    def get_data(self):
        data = {
            "shopper" : self.get_shopper(),
            "user" : self.get_user(),
            "order" : self.get_order(),
            "sticker" : self.get_sticker(),
        }
        return data
    
    def csv_to_dict(self, path):
        with open(path, "r", encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def get_sticker(self):
        sticker = self.csv_to_dict(os.path.join("population", "data", "sticker.csv"))
        for index in range(len(sticker)):
            sticker[index]["id"] = int(sticker[index]["id"])
            sticker[index]["image"] = os.path.join('sticker_images', sticker[index]["image"])
            sticker[index]["price"] = decimal.Decimal(float(sticker[index]["price"]))
        return sticker

    def get_order(self):
        order = self.csv_to_dict(os.path.join("population", "data", "order.csv"))
        for index in range(len(order)):
            order[index]["id"] = int(order[index]["id"])

            user = create_obj_by_attr("username", order[index]["shopper"],  self.get_user(), User())
            shopper = create_obj_by_attr("user", user,  self.get_shopper(), Shopper())
            order[index]["shopper"] = shopper
    
            sticker = create_obj_by_attr("name", order[index]["sticker"],   self.get_sticker(), Sticker())
            order[index]["sticker"] = sticker
        return order

    def get_user(self):
        user = self.csv_to_dict(os.path.join("population", "data", "user.csv"))
        for index in range(len(user)):
            user[index]["id"] = int(user[index]["id"])
        return user

    def get_shopper(self):
        shopper = self.csv_to_dict(os.path.join("population", "data", "shopper.csv"))
        for index in range(len(shopper)):
            shopper[index]["id"] = int(shopper[index]["id"])

            user = create_obj_by_attr("username", shopper[index]["user"],   self.get_user(),User())
            shopper[index]["user"] = user
        return shopper
    