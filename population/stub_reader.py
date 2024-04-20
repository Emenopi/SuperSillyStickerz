from django.contrib.auth.models import User
from stickerz.models import Sticker, Shopper
from population.reader import Reader
from population.utils import find_dict_by_item, obj_to_dict
import decimal
import os

class StubReader(Reader):
    def get_data(self):
        data = {
            "shopper" : self.get_shopper(),
            "user" : self.get_user(),
            "order" : self.get_order(),
            "sticker" : self.get_sticker(),
        }
        return data

    def get_sticker(self):
        sticker=[
            {
                "id" : 0,
                "name" : "Window Cat",
                "price" : "1.20",
                "image" : "window_cat.png",
                "category" : "Cats"
            },
            {
                "id" : 1,
                "name" : "Meowgical Cat",
                "price" : "1.05",
                "image" : "meowgical.jpeg",
                "category" : "Cats"
            },
            {
                "id" : 2,
                "name" : "Matt",
                "price" : "0.50",
                "image" : "matt.jpg",
                "category" : "People"
            },
            {
                "id" : 3,
                "name" : "David Tennant",
                "price" : "1.00",
                "image" : "spock.jpg",
                "category" : "People"
            },
            {
                "id" : 4,
                "name" : "Sausage Dog",
                "price" : "1.20",
                "image" : "sausage_dog.jpg",
                "category" : "Dogs"
            },
            {
                "id" : 5,
                "name" : "Heart Dog",
                "price" : "1.05",
                "image" : "heart_dog.png",
                "category" : "Dogs"
            },
        ]
        for index in range(len(sticker)):
            sticker[index]["image"] = os.path.join('sticker_images', sticker[index]["image"])
            sticker[index]["price"] = decimal.Decimal(float(sticker[index]["price"]))
        return sticker

    def get_order(self):
        order=[
            {
                "id" : 0,
                "shopper" : "stickergal1",
                "status" : "Processing",
                "sticker" : "Window Cat",
                "finish" : "holographic",
                "quantity" : "4",
                "timePlaced" : "2024-04-05 09:43:56-15",
            },
            {
                "id" : 1,
                "shopper" : "ilovestickers",
                "status" : "Delivered",
                "sticker" : "David Tennant",
                "finish" : "gloss",
                "quantity" : "99",
                "timePlaced" : "2024-03-10 08:23:12-08",
            }
        ]
        for index in range(len(order)):
            # replace names with real objects
            userData = find_dict_by_item("username", order[index]["shopper"], self.get_user())
            user = obj_to_dict(User(), userData)

            shopperData = find_dict_by_item("user", user, self.get_shopper())
            shopper = obj_to_dict(Shopper(), shopperData)
            order[index]["shopper"] = shopper
            
            stickerData = find_dict_by_item("name", order[index]["sticker"], self.get_sticker())
            sticker = obj_to_dict(Sticker(), stickerData)
            order[index]["sticker"] = sticker
        return order
    
    def get_user(self):
        user=[
            {
                "id" : 0,
                "username" : "stickergal1",
                "password": "klhsadf8798uas",
                "email" : "sticker@stickers.com",
                "first_name" : "sticker",
                "last_name" : "gal"
            },
            {
                "id" : 1,
                "username" : "ilovestickers",
                "password": "jnfds878u9",
                "email" : "stickerlove@stickers.com",
                "first_name" : "sticker",
                "last_name" : "lover"
            },
        ]
        return user

    def get_shopper(self):
        shopper=[
                {
                    "id" : 0,
                    "user" : "stickergal1",
                    "shippingFName" : "sticker",
                    "shippingLName" : "gal",
                    "shippingAddress" : "123 Sticker St",
                    "shippingCountry" : "Belgium",
                    "shippingPostcode" : "BE12 1GM",
                    "billingFName" : "sticker",
                    "billingLName" : "gal",
                    "billingAddress" : "123 Sticker St",
                    "billingCountry" : "Belgium",
                    "billingPostcode" : "BE12 1GM",
                    "cardNo" : "1234567812341230",
                    "exp" : "0924",
                    "cvv" : "123",
                },
                {
                    "id" : 1,
                    "user" : "ilovestickers",
                    "shippingFName" : "sticker",
                    "shippingLName" : "crazy",
                    "shippingAddress" : "47 crazy rd",
                    "shippingCountry" : "France",
                    "shippingPostcode" : "PA92 7RS",
                    "billingFName" : "sticker",
                    "billingLName" : "crazy",
                    "billingAddress" : "47 crazy rd",
                    "billingCountry" : "France",
                    "billingPostcode" : "PA92 7RS",
                    "cardNo" : "8475927465937480",
                    "exp" : "0527",
                    "cvv" : "485",
                }
            ]
        for index in range(len(shopper)):
            # replace names with real objects
            userData = find_dict_by_item("username", shopper[index]["user"], self.get_user())
            user = obj_to_dict(User(), userData)
            shopper[index]["user"] = user
        return shopper
    