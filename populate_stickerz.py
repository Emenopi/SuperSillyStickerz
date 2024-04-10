import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'SuperSillyStickerz.settings')

import django
django.setup()
from stickerz.models import Shopper, Sticker, Order
from django.contrib.auth.models import User
from SuperSillyStickerz.urls import static
import decimal
import dateutil.parser

def populate():
    populate_stickers()
    # populate_users()
    # populate_orders()

def populate_stickers():
    catStickers = [
        {
            'name': 'Window Cat',
            'price': "1.20",
            'image': 'window_cat.png'
        },
        {
            'name': 'Meowgical Cat',
            'price': "1.05",
            'image': 'meowgical.jpeg'
        },
        {
            'name': 'Space Cat',
            'price': "1.15",
            'image': 'space_cat.png'
        },
        {
            'name': 'Catstronaut',
            'price': "1.00",
            'image': 'catstronaut.jpg'
        },
        {
            'name': 'Sneaky Black Cat',
            'price': "1.10",
            'image': 'sneaky_black_cat.jpg'
        },
        {
            'name': 'Mermaid Cat',
            'price': "1.20",
            'image': 'mermaid_cat.jpg'
        },
    ]
    peopleStickers = [
        {
            'name': 'Matt',
            'price': 0.50,
            'image': 'matt.jpg'
        },
        {
            'name': 'Derek',
            'price': 0.50,
            'image': 'derek.jpeg'
        },
        {
            'name': 'David Tennant',
            'price': 1.00,
            'image': 'david_tennant.jpg'
        },
        {
            'name': 'Spock',
            'price': 1.15,
            'image': 'spock.jpg'
        },
        {
            'name': 'Einstein',
            'price': 1.25,
            'image': 'einstein.jpg'
        },
        {
            'name': 'Marilyn Monroe',
            'price': 1.10,
            'image': 'marilyn_monroe.jpg'
        },
    ]
    dogStickers = [
        {
            'name': 'Sausage Dog',
            'price': 1.20,
            'image': 'sausage_dog.jpg'
        },
        {
            'name': 'Heart Dog',
            'price': 1.05,
            'image': 'heart_dog.jpg'
        },
        {
            'name': 'Funny Heart',
            'price': 1.00,
            'image': 'funny_dog.jpg'
        },
        {
            'name': 'Carrot Dog',
            'price': 0.95,
            'image': 'carrot_dog.jpg'
        },
        {
            'name': 'Happy Dog',
            'price': 0.50,
            'image': 'happy_dog.jpg'
        },
        {
            'name': 'Pawficer',
            'price': 0.90,
            'image': 'pawficer.jpg'
        },
    ]
    placeStickers = [
        {
            'name': 'Paris',
            'price': 1.00,
            'image': 'paris.jpg'
        },
        {
            'name': 'London',
            'price': 1.00,
            'image': 'london.jpg'
        },
        {
            'name': 'New York',
            'price': 1.15,
            'image': 'new_york.jpg'
        },
        {
            'name': 'Manila',
            'price': 1.00,
            'image': 'manila.jpg'
        },
        {
            'name': 'Berlin',
            'price': 1.20,
            'image': 'berlin.jpg'
        },
        {
            'name': 'Madrid',
            'price': 1.25,
            'image': 'madrid.jpg'
        },
    ]
    techStickers = [
        {
            'name': 'Tux',
            'price': 0.75,
            'image': 'tux.jpg'
        },
        {
            'name': 'Women In Tech',
            'price': 1.00,
            'image': 'women_in_tech.jpg'
        },
        {
            'name': 'Dont Forget To Save',
            'price': 0.50,
            'image': 'dont_forget_to_save.jpg'
        },
        {
            'name': 'Java Developer',
            'price': 1.00,
            'image': 'java_developer.jpg'
        },
        {
            'name': 'Heartbeat Python',
            'price': 0.20,
            'image': 'heartbeat_python.jpg'
        },
        {
            'name': 'Tech Brain',
            'price': 1.15,
            'image': 'tech_brain.jpg'
        },
    ]
    fashionStickers = [
        {
            'name': 'Handbag',
            'price': 0.60,
            'image': 'handbag.jpg'
        },
        {
            'name': 'Red Bottom Heels',
            'price': 1.00,
            'image': 'red_bottom_heels.jpg'
        },
        {
            'name': 'Shoe Addict',
            'price': 0.50,
            'image': 'shoe_addict.jpg'
        },
        {
            'name': 'I Love Shopping',
            'price': 1.00,
            'image': 'i_love_shopping.jpg'
        },
        {
            'name': 'Retail Therapy',
            'price': 0.80,
            'image': 'retail_therapy.jpg'
        },
        {
            'name': 'Fashion Girl',
            'price': 1.20,
            'image': 'fashion_girl.jpg'
        },
    ]
    cuteStickers = [
        {
            'name': 'I Love You Heart',
            'price': 1.32,
            'image': 'i_love_you_heart.jpg'
        },
        {
            'name': 'Axolotl Milk',
            'price': 1.00,
            'image': 'axolotl_milk.jpg'
        },
        {
            'name': 'Cute Cactus',
            'price': 1.10,
            'image': 'cute_cactus.jpg'
        },
        {
            'name': 'Strawberry Frog',
            'price': 1.00,
            'image': 'strawberry_frog.jpg'
        },
        {
            'name': 'Cute Unicorn',
            'price': 0.80,
            'image': 'cute_unicorn.jpg'
        },
        {
            'name': 'Cute Watermelon',
            'price': 1.15,
            'image': 'cute_watermelon.jpg'
        },
    ]    
    skatingStickers = [
        {
            'name': 'I Love To Skate',
            'price': 1.30,
            'image': 'i_love_to_skate.jpg'
        },
        {
            'name': 'Skate',
            'price': 1.00,
            'image': 'skate.jpg'
        },
        {
            'name': 'Skateboard Heart',
            'price': 0.95,
            'image': 'skateboard_heart.jpg'
        },
        {
            'name': 'This Is How I Roll',
            'price': 1.22,
            'image': 'this_is_how_i_roll.jpg'
        },
        {
            'name': 'Cool Girls Skate',
            'price': 0.84,
            'image': 'cool_girls_skate.jpg'
        },
        {
            'name': 'Pizza Skateboard',
            'price': 1.15,
            'image': 'pizza_skateboard.png'
        },
    ]
    brandStickers = [
        {
            'name': 'Nutalla',
            'price': 1.00,
            'image': 'nutella.jpg'
        },
        {
            'name': 'Kappa',
            'price': 1.20,
            'image': 'kappa.jpg'
        },
        {
            'name': 'Jim Beam',
            'price': 1.35,
            'image': 'jim_beam.jpg'
        },
        {
            'name': 'Vans',
            'price': 1.24,
            'image': 'vans.jpg'
        },
        {
            'name': 'Kool Aid',
            'price': 0.60,
            'image': 'kool_aid.jpg'
        },
        {
            'name': 'Playstation',
            'price': 1.12,
            'image': 'playstation.jpg'
        },
    ]
    schoolStickers = [
        {
            'name': 'School Is Fun',
            'price': 0.30,
            'image': 'school_is_fun.png'
        },
        {
            'name': 'Graduation',
            'image': 9,
            'price': 1.00,
            'image': 'graduation.jpg'
        },
        {
            'name': 'Too Cool For School',
            'price': 1.43,
            'image': 'too_cool_for_school.jpg'
        },
        {
            'name': 'Welcome Back To School',
            'price': 1.20,
            'image': 'welcome_back_to_school.jpg'
        },
        {
            'name': 'Back To School',
            'price': 0.75,
            'image': 'back_to_school.png'
        },
        {
            'name': 'Pencil',
            'price': 0.85,
            'image': 'pencil.jpg'
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
            add_sticker(stickercat, item['name'], item['price'], "Matte", item['image'])
            add_sticker(stickercat, item['name'], item['price'], "Gloss", item['image'])
            add_sticker(stickercat, item['name'], item['price'], "Holo", item['image'])

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


def populate_orders():
    orderOne = {
        'username': 'mattyBarr',
        'status': 'Processing',
        'sticker': 'Matt',
        'finish': 'Matte',
        'quantity': 50,
        'time': '2024-04-05 09:43:56-15'
    }
    orderTwo = {
        'username': 'mattyBarr',
        'status': 'Delivered',
        'sticker': 'Derek',
        'finish': 'Gloss',
        'quantity': 30,
        'time': '2024-03-29 12:15:32-03'
    }
    orderThree = {
        'username': 'omgstickers',
        'status': 'Dispatched',
        'sticker': 'Shoe Addict',
        'finish': 'Holo',
        'quantity': 15,
        'time': '2024-03-10 08:23:12-08'
    }
    orderFour = {
        'username': 'stickergal1',
        'status': 'Delivered',
        'sticker': 'Paris',
        'finish': 'Gloss',
        'quantity': 5,
        'time': '2024-03-15 08:10:10-20'
    }
    orderFive = {
        'username': 'wowstickerzzz',
        'status': 'Processing',
        'sticker': 'Skateboard Heart',
        'finish': 'Matte',
        'quantity': 12,
        'time': '2024-04-10 13:23:15-13'
    }

    orders = {
        '1': {'data': orderOne},
        '2': {'data': orderTwo},
        '3': {'data': orderThree},
        '4': {'data': orderFour},
        '5': {'data': orderFive}
    }

    for order, order_data in orders.items():
        data = order_data['data']
        shopper = data['username']
        add_order(shopper, data)

def add_sticker(stickerCat, stickerName, stickerPrice, stickerFinish, stickerImage):
    stickerPrice = decimal.Decimal(float(stickerPrice))
    image = os.path.join('/sticker_images', stickerImage)
    sticker = Sticker.objects.get_or_create(name=stickerName, category=stickerCat, price=stickerPrice, finish=stickerFinish, image=image)[0]
    sticker.save()
    return sticker

def add_shopper(username, shopperData):
    print("Adding shopper: ", username)
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

def add_order(username, orderData):
    print("adding ", username, "'s Order")
    user = User.objects.get(username=username)
    shopper = Shopper.objects.get(user=user)
    sticker = Sticker.objects.get(name=orderData['sticker'], finish=orderData['finish'])
    time = dateutil.parser.parse(orderData['time'])
    order = Order.objects.get_or_create(shopper=shopper,
                                        status=orderData['status'],
                                        sticker=sticker,
                                        quantity=orderData['quantity'],
                                        timePlaced=time
                                        )
    return order


def add_user(name, password, email, fName, sName):
    user = User.objects.get_or_create(username=name, password=password, email=email, first_name=fName, last_name=sName)

if __name__ == '__main__':
    print('Starting Stickerz population script...')
    populate()