import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'SuperSillyStickerz.settings')

import django
django.setup()
from stickerz.models import Shopper, Sticker, Order
from django.contrib.auth.models import User
import decimal

def populate():
    populate_stickers()
    populate_users()

def populate_stickers():
    catStickers = [
        {
            'name': 'Window Cat',
            'price': "1.20",
        },
        {
            'name': 'Meowgical Cat',
            'price': "1.05",
        },
        {
            'name': 'Space Cat',
            'price': "1.15",
        },
        {
            'name': 'Catstronaut',
            'price': "1.00",
        },
        {
            'name': 'Sneaky Black Cat',
            'price': "1.10",
        },
        {
            'name': 'Mermaid Cat',
            'price': "1.20",
        },
    ]
    peopleStickers = [
        {
            'name': 'Matt',
            'price': 0.50,
        },
        {
            'name': 'Derek',
            'price': 0.50,
        },
        {
            'name': 'David Tennant',
            'price': 1.00,
        },
        {
            'name': 'Spock',
            'price': 1.15,
        },
        {
            'name': 'Einstein',
            'price': 1.25,
        },
        {
            'name': 'Marilyn Monroe',
            'price': 1.10,
        },
    ]
    dogStickers = [
        {
            'name': 'Sausage Dog',
            'price': 1.20,
        },
        {
            'name': 'Heart Dog',
            'price': 1.05,
        },
        {
            'name': 'Funny Heart',
            'price': 1.00,
        },
        {
            'name': 'Carrot Dog',
            'price': 0.95,
        },
        {
            'name': 'Happy Dog',
            'price': 0.50,
        },
        {
            'name': 'Pawficer',
            'price': 0.90,
        },
    ]
    placeStickers = [
        {
            'name': 'Paris',
            'price': 1.00,
        },
        {
            'name': 'London',
            'price': 1.00,
        },
        {
            'name': 'New York',
            'price': 1.15,
        },
        {
            'name': 'Manila',
            'price': 1.00,
        },
        {
            'name': 'Berlin',
            'price': 1.20,
        },
        {
            'name': 'Madrid',
            'price': 1.25,
        },
    ]
    techStickers = [
        {
            'name': 'Tux',
            'price': 0.75,
        },
        {
            'name': 'Women In Tech',
            'price': 1.00,
        },
        {
            'name': 'Dont Forget To Save',
            'price': 0.50,
        },
        {
            'name': 'Java Developer',
            'price': 1.00,
        },
        {
            'name': 'Heartbeat Python',
            'price': 0.20,
        },
        {
            'name': 'Tech Brain',
            'price': 1.15,
        },
    ]
    fashionStickers = [
        {
            'name': 'Handbag',
            'price': 0.60,
        },
        {
            'name': 'Red Bottom Heels',
            'price': 1.00,
        },
        {
            'name': 'Shoe Addict',
            'price': 0.50,
        },
        {
            'name': 'I Love Shopping',
            'price': 1.00,
        },
        {
            'name': 'Retail Therapy',
            'price': 0.80,
        },
        {
            'name': 'Fashion Girl',
            'price': 1.20,
        },
    ]
    cuteStickers = [
        {
            'name': 'I Love You Heart',
            'price': 1.32,
        },
        {
            'name': 'Axolotl Milk',
            'price': 1.00,
        },
        {
            'name': 'Cute Cactus',
            'price': 1.10,
        },
        {
            'name': 'Strawberry Frog',
            'price': 1.00,
        },
        {
            'name': 'Cute Unicorn',
            'price': 0.80,
        },
        {
            'name': 'Cute Watermelon',
            'price': 1.15,
        },
    ]    
    skatingStickers = [
        {
            'name': 'I Love To Skate',
            'price': 1.30,
        },
        {
            'name': 'Skate',
            'price': 1.00,
        },
        {
            'name': 'Skateboard Heart',
            'price': 0.95,
        },
        {
            'name': 'This Is How I Roll',
            'price': 1.22,
        },
        {
            'name': 'Cool Girls Skate',
            'price': 0.84,
        },
        {
            'name': 'Pizza Skateboard',
            'price': 1.15,
        },
    ]
    brandStickers = [
        {
            'name': 'Nutalla',
            'price': 1.00,
        },
        {
            'name': 'Kappa',
            'price': 1.20,
        },
        {
            'name': 'Jim Beam',
            'price': 1.35,
        },
        {
            'name': 'Vans',
            'price': 1.24,
        },
        {
            'name': 'Kool Aid',
            'price': 0.60,
        },
        {
            'name': 'Playstation',
            'price': 1.12,
        },
    ]
    schoolStickers = [
        {
            'name': 'School Is Fun',
            'price': 0.30,
        },
        {
            'name': 'Graduation',
            'image': 9,
            'price': 1.00,
        },
        {
            'name': 'Too Cool For School',
            'price': 1.43,
        },
        {
            'name': 'Welcome Back To School',
            'price': 1.20,
        },
        {
            'name': 'Back To School',
            'price': 0.75,
        },
        {
            'name': 'Pencil',
            'price': 0.85,
        },
    ]
    stickers = {'Cats': {'items': catStickers},
            'People': {'items': peopleStickers},
            'Dogs': {'items': dogStickers},
            'Places': {'items': placeStickers},
            'Tech': {'items': techStickers},
            'Fashion': {'items': fashionStickers},
            'Skating': {'items': skatingStickers},
            'Cute': {'items': cuteStickers},
            'Brands': {'items': brandStickers},
            'School': {'items': schoolStickers}}
    
    for stickercat, sticker_data in stickers.items():
        print(stickercat)
        for item in sticker_data['items']:
            add_sticker(stickercat, item['name'], item['price'], "Matte")
            add_sticker(stickercat, item['name'], item['price'], "Gloss")
            add_sticker(stickercat, item['name'], item['price'], "Holo")

def populate_users():
    userOne = {
            'username': 'stickergal1',
            'password': "as234kjn128",
            'email': "sticker@stickers.com",
            "fName" : "sticker",
            "sName" : "gal"
        }
    userTwo = {
            'username': 'ilovestickers',
            'password': "18ndjf2",
            'email': "stickerlove@stickers.com",
            "fName" : "sticker",
            "sName" : "lover"
        }
    userThree =  {
            'username': 'mattyBarr',
            'password': "238ind35",
            'email': "mattBar@mattBarrFanClub.com",
            "fName" : "Matt",
            "sName" : "Barr"
        }
    userFour = {
            'username': 'omgstickers',
            'password': "2983hdfnk",
            'email': "DSomerville@mattBarrFanClub.com",
            "fName" : "derek",
            "sName" : "somerville"
        }
    userFive = {
            'username': 'wowstickerzzz',
            'password': "2398nsjf21",
            'email': "wow@stickers.com",
            "fName" : "wow",
            "sName" : "stickazz"
        }
    shopperOne = {
            'shipfName': "sticker",
            'shiplName': "gal",
            "shipAddress" : "123 sticker st",
            "shipCountry" : "Belgium",
            "shipPostcode": "BE12 1GM",
            "billfName": "sticker",
            "billsName": "gal",
            "billAddress" : "123 sticker st",
            "billCountry" : "Belgium",
            "billPostcode": "BE12 1GM",
            "cardno": "1234567812341234",
            "exp": "0924",
            "cvv": "123"

        }
    shopperTwo = {
            'shipfName': "sticker",
            'shiplName': "crazy",
            "shipAddress" : "47 crazy rd",
            "shipCountry" : "France",
            "shipPostcode": "PA92 7RS",
            "billfName": "crazy",
            "billsName": "lady",
            "billAddress" : "38 stuck cresc",
            "billCountry" : "Germany",
            "billPostcode": "LP87 9ZG",
            "cardno": "8475927465937485",
            "exp": "0527",
            "cvv": "485"

        }
    shopperThree = {
            'shipfName': "derek",
            'shiplName': "somerville",
            "shipAddress" : "1 derek rd",
            "shipCountry" : "Scotland",
            "shipPostcode": "G5 8DS",
            "billfName": "matt",
            "billsName": "barr",
            "billAddress" : "12 matt st",
            "billCountry" : "Scotland",
            "billPostcode": "G1 1MT",
            "cardno": "9274659847472882",
            "exp": "1029",
            "cvv": "384"

        }
    shopperFour = {
            'shipfName': "derek",
            'shiplName': "somerville",
            "shipAddress" : "1 derek rd",
            "shipCountry" : "Scotland",
            "shipPostcode": "G5 8DS",
            "billfName": "derek",
            "billsName": "somerville",
            "billAddress" : "1 derek rd",
            "billCountry" : "Scotland",
            "billPostcode": "G5 8DS",
            "cardno": "3744766492837404",
            "exp": "1228",
            "cvv": "387"

        }
    shopperFive = {
            'shipfName': "wim",
            'shiplName': "vanderbauwheder",
            "shipAddress" : "13 wim pass",
            "shipCountry" : "Nederlands",
            "shipPostcode": "AM22 8DM",
            "billfName": "wim",
            "billsName": "vvanderbauwheder",
            "billAddress" : "13 wim pass",
            "billCountry" : "Nederlands",
            "billPostcode": "AM22 8DM",
            "cardno": "3746583920383747",
            "exp": "0826",
            "cvv": "384"

        }
    users = {
        '1': {'data': userOne, 'shopper': shopperOne},
        '2': {'data': userTwo, 'shopper': shopperTwo},
        '3': {'data': userThree, 'shopper': shopperThree},
        '4': {'data': userFour, 'shopper': shopperFour},
        '5': {'data': userFive, 'shopper': shopperFive}
    }

    for user, user_data in users.items():
        data = user_data['data']
        shopper = user_data['shopper']
        add_user(data['username'], data['password'], data['email'], data['fName'], data['sName'])
        add_shopper(data['username'], shopper)

def add_sticker(stickerCat, stickerName, stickerPrice, stickerFinish):
    stickerPrice = decimal.Decimal(float(stickerPrice))
    sticker = Sticker.objects.get_or_create(name=stickerName, category=stickerCat, price=stickerPrice, finish=stickerFinish)[0]
    sticker.save()
    return sticker

def add_shopper(username, shopperData):
    user = User.objects.get(username=username)
    shopper = Shopper.objects.get_or_create(user=user, shippingFName=shopperData['shipfName'],
                                            shippingLName=shopperData['shiplName'],
                                            shippingAddress=shopperData['shipAddress'],
                                            shippingCountry=shopperData['shipCountry'],
                                            shippingPostcode=shopperData['shipPostcode'],
                                            billingFName=shopperData['billfName'],
                                            billingLName=shopperData['billsName'],
                                            billingAddress=shopperData['billAddress'],
                                            billingCountry=shopperData['billCountry'],
                                            billingPostcode=shopperData['billPostcode'],
                                            cardNo=shopperData['cardno'],
                                            expiration=shopperData['exp'],
                                            cvv=shopperData['cvv'])
    return shopper

def add_user(name, password, email, fName, sName):
    user = User.objects.get_or_create(username=name, password=password, email=email, first_name=fName, last_name=sName)

if __name__ == '__main__':
    print('Starting Stickerz population script...')
    populate()