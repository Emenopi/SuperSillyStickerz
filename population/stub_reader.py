from django.contrib.auth.models import User
from stickerz.models import Sticker, Shopper
from population.reader import Reader
from population.utils import create_obj_by_attr
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
        sticker = self.sticker_data()
        for index in range(len(sticker)):
            sticker[index]["image"] = os.path.join('sticker_images', sticker[index]["image"])
            sticker[index]["price"] = decimal.Decimal(float(sticker[index]["price"]))
        return sticker

    def get_order(self):
        order = self.order_data()
        for index in range(len(order)):
            user = create_obj_by_attr("username", order[index]["shopper"], self.get_user(), User())
            shopper = create_obj_by_attr("user", user, self.get_shopper(), Shopper())
            order[index]["shopper"] = shopper
        
            sticker = create_obj_by_attr("name", order[index]["sticker"], self.get_sticker(), Sticker())
            order[index]["sticker"] = sticker
        return order
    
    def get_user(self):
        return self.user_data()

    def get_shopper(self):
        shopper = self.shopper_data()
        for index in range(len(shopper)):
            user = create_obj_by_attr("username", shopper[index]["user"],  self.get_user(), User())
            shopper[index]["user"] = user
        return shopper
    

    def user_data(self):
        USER=[
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
        return USER
    
    def shopper_data(self):
        SHOPPER=[
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
        return SHOPPER

    def sticker_data(self):
        STICKER=[
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
        return STICKER
    
    def order_data(self):
        ORDER=[
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
        return ORDER