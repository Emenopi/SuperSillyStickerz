from django.test import TestCase
from .forms import UserForm

class UserFormTest(TestCase):
    def test_login_form(self):
        valid_form_data = {'username': 'testuser', 'password': 'testpassword'}
        self.form = UserForm(data=valid_form_data)
        self.assertTrue(self.form.is_valid())

    def test_login_form_invalid(self):
        invalid_form_data = [
            {'username': 'testuser'},  # no password
            {'password': 'testpassword'},  # no username
            {'username': ' ', 'password': 'testpassword'},  # space username
            {'username': 'testuser', 'password': ' '}  # space password
        ]

        for form_data in invalid_form_data:
            form = UserForm(data=form_data)
            self.assertFalse(form.is_valid())

    
