# Introduction

'Super Silly Stickerz' is a website that sells pre-made and customisable stickers. It allows users to login, browse, customise, and purchase stickers.

The home page displays all pre-made stickers which can be filtered by categories which appear in the sidebar.

Once the user has chosen a sticker they wish to purchase, they can then choose the finish of the sticker from the available options, and the quantity they wish to purchase.

There is also an option to buy custom stickers. This functionality allows users to make a unique sticker by uploading an image. Users can also select finish and quantity for custom stickers.

In order to purchase a sticker, the user must have an account and be logged in.

There is also a dashboard page where users can view their order history and view/edit their shipping and billing information.

# Architecture

UML diagrams are located in the UML directory.

This project uses the Django framework and heavily relies on its architecture. The classes which represent our database tables are based on Django's Model class. There is an Order class that keeps track of orders a user has placed. Each order has a Shopper and a Sticker in it. It also has a finish attribute so that each sticker does not need a seperate object for each finish of the same design (eg gloss cat, matte cat, holographic cat).

The User class is another built in class that we use because because it is integrated with a built in user registration system. To keep this functionality, instead of extending User, each instance of our Shopper class has an instance of User. This also means that in the future we could switch to a different registration system by using an adapter with an interface matching User's.

Our populations script uses a Populate class. This class has a reader which must be an implementation of the Reader interface. This means that we can easily switch the reader that Populate uses at runtime. This is an example of the strategy design pattern. One concrete benefit of this is we can use a StubReader for testing so that we don't slow down tests with the file handling done by CsvReader.

# Usage

Create a python 3.10 environemnt, install listed extensions, open root directory, and run `$python manage.py runserver`.

To run a test use `python manage.py test tests.NAME_OF_TEST`

If you need assistance just ask.

asgiref==3.8.1
cffi==1.16.0
cryptography==42.0.5
Django==2.2
django-appconf==1.0.6
django-cryptography==1.1
django-registration-redux==2.2
pillow==10.2.0
pycparser==2.22
pycryptodome==3.20.0
python-dateutil==2.9.0.post0
pytz==2024.1
six==1.16.0
sqlparse==0.4.4
typing_extensions==4.10.0

# Retrospective 18/04/2024:

## Wind - What helped us

- pair programming
- good reviews
- familiarity with Python

## Anchor - what held us back

- very large and general tickets
- large non self contained commits
	- sometimes commits break main
- delay before code reviews
- lots of merges all at once
- time constraints due to other subjects in conjunction with TSI

## Sun - what made us feel good

- everyone supports each other
- respectful of each others time
- growing familiarity with Django framework

## Reef - future risks

- deadline is monday
- unsure of testing methods for Django
- harder communication over weekend
	- not in person

## Actions

- Make smaller, more detailed tickets
- Make smaller, self contained commits
- Prototpye testing methods in Django today
