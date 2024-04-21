from django.test import TestCase, RequestFactory
from unittest.mock import patch
from stickerz.models import Sticker, Order, Shopper, User
from stickerz.views import sticker, dashboard

class DashboardViewTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )

    # run the tests in this file with :
    # $python manage.py test tests.views_test

    # # # example test

    # # patch "passes in" mock_sticker
    # @patch('stickerz.models.Sticker.objects')
    # # name must start with test_ to run
    # # format of name is test_thingBeingTested_input_expectedOutput
    # def test_stickerView_mockSticker_stickerDisplayed(self, mock_sticker):
    #     #set up test
    #     title = "matte matt"
    #     title_slug = "matte-matt"
    #     mock_sticker.get.return_value = Sticker(name=title)

    #     # get response
    #     request = self.factory.get('/'+title_slug+"/")
    #     response = sticker(request, title)

    #     #assert results
    #     self.assertContains(response, title) # asserts response contains title
    
    def get_mock_order_info(self):
        sticker_name = "ghost"
        orders = [
            Order(
                shopper=Shopper(),
                status="Delivered",
                sticker=Sticker(name=sticker_name),
                finish="holographic",
                quantity=8,
                timePlaced ="April 18, 2024, 11:42 a.m."
                )
            ]
        return sticker_name, orders
    
    @patch('stickerz.models.Shopper.objects.get')
    @patch('stickerz.models.Order.objects.filter')
    def test_dashboard_mockOrders_orderHistoryDisplayed(self, mock_order_filter, mock_shopper_get):
        """
        It displays orders in dashboard
        """
        sticker_name, orders = self.get_mock_order_info()
        mock_shopper_get.return_value = Sticker()
        mock_order_filter.return_value = orders

        request = self.factory.get("/dashboard/")
        request.user = self.user
        response = dashboard(request)
        
        expected = "<li>"+sticker_name+" - "+orders[0].timePlaced+"</li>"
        self.assertContains(response, expected)

    @patch('stickerz.models.Shopper.objects.get')
    @patch('stickerz.models.Order.objects.filter')
    def test_dashboardView_mockShopper_dataDisplayed(self, mock_order_filter, mock_shopper):

        shopper = Shopper( 
            user = self.user, 

            shippingFName = 'Emily', 
            shippingLName = 'Holt',  
            shippingAddress = '1 Street Street', 
            shippingCountry = 'United Kingdom', 
            shippingPostcode = 'AB12 3CD', 

            billingFName = 'Emily', 
            billingLName = 'Holt', 
            billingAddress = '1 Street Street', 
            billingCountry = 'United Kingdom', 
            billingPostcode = 'AB12 3CD', 
        )

        mock_shopper.return_value = shopper
        mock_order_filter.return_value = [Order()]

        request = self.factory.get("/dashboard/")
        request.user = self.user
        response = dashboard(request)

        expected = """    <h2>Shipping Address</h2>
    <p>Emily Holt</p>
    <p>1 Street Street</p>
    <p>United Kingdom</p>
    <p>AB12 3CD</p>

    <h2>Billing Address</h2>
    <p>Emily Holt</p>
    <p>1 Street Street</p>
    <p>United Kingdom</p>
    <p>AB12 3CD</p>""" # format needs to be like this so test passes

        self.assertContains(response, expected)
