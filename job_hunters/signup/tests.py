from django.test import TestCase
from . import models

# Create your tests here.

class SignupTestCase(TestCase):
    def create_data(self):
        return {'user-username':'Test',
                'user-password1':'abcdefg123',
                'user-password2':'abcdefg123',
                'user-first_name': 'Test',
                'user-last_name': 'Name',
                'individual-address': 'Address 10',
                'individual-date_of_birth': '01-01-2000',
                'individual-phone_number': '1234567'}

    def test_successful_signup(self):
        data = self.create_data()
        signup = models.SignupForm(data)
        self.assertTrue(signup.is_valid(), "Signup is valid")