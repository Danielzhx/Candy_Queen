from django.test import TestCase
from . import models

# Create your tests here.

class SignupTestCase(TestCase):
    def create_data(self):
        return {'user-username':'Test',
                'user-password1':'abcdefg789',
                'user-password2':'abcdefg789',
                'user-first_name': 'Test',
                'user-last_name': 'Name',
                'individual-address': 'Address 10',
                'individual-date_of_birth': '2000-01-01',
                'individual-phone_number': '1234567'}

    def test_successful_signup(self):
        signup = models.SignupForm(self.create_data())
        self.assertTrue(signup.is_valid(), signup.errors)
        
    def test_phone_not_num(self):
        data = self.create_data()
        data['individual-phone_number'] = '12e4567'
        signup = models.SignupForm(data)
        self.assertFalse(signup.is_valid(), signup.errors)

    def test_dob_in_future(self):
        data = self.create_data()
        data['individual-date_of_birth'] = '2030-01-01'
        signup = models.SignupForm(data)
        self.assertFalse(signup.is_valid(), signup.errors)
    
    def test_address_only_text(self):
        data = self.create_data()
        data['address'] = 'Test'
        signup = models.SignupForm(data)
        self.assertFalse(signup.is_valid(), signup.errors)
        
    def test_address_only_num(self):
        data = self.create_data()
        data['address'] = ' 10'
        signup = models.SignupForm(data)
        self.assertFalse(signup.is_valid(), signup.errors)