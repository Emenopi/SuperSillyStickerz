from django.test import TestCase
from .forms import UserForm

class UserFormTest(TestCase):
    def test_login_form(self):
        valid_form_data = {'username': 'testuser', 'password': 'testpassword'}
        self.form = UserForm(data=valid_form_data)
        self.assertTrue(self.form.is_valid())

    def test_login_form_invalid(self):
        invalid_form_data_no_password = {'username': 'testuser'}
        invalid_form_data_no_username = {'password': 'testpassword'}
        invalid_form_data_space_username = {'username': ' ', 'password': 'testpassword'}
        invalid_form_data_space_password = {'username': 'testuser', 'password': ' '}

        self.form1 = UserForm(data=invalid_form_data_no_password)
        self.form2 = UserForm(data=invalid_form_data_no_username)
        self.form3 = UserForm(data=invalid_form_data_space_username)
        self.form4 = UserForm(data=invalid_form_data_space_password)


        self.assertFalse(self.form1.is_valid())
        self.assertFalse(self.form2.is_valid())
        self.assertFalse(self.form3.is_valid())
        self.assertFalse(self.form4.is_valid())
