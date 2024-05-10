from django.test import TestCase
from . import models
from Forms.signup_form import ISignupForm, CSignupForm
from Forms.individual_form import IndividualForm

# Create your tests here.

class ISignupTestCase(TestCase):
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
        signup = ISignupForm(self.create_data())
        self.assertTrue(signup.is_valid(), signup.errors)
        
    def test_phone_not_num(self):
        data = self.create_data()
        data['individual-phone_number'] = '12e4567'
        signup = ISignupForm(data)
        self.assertFalse(signup.is_valid(), signup.errors)

    def test_dob_in_future(self):
        data = self.create_data()
        data['individual-date_of_birth'] = '2030-01-01'
        signup = ISignupForm(data)
        self.assertFalse(signup.is_valid(), signup.errors)
    
    def test_address_only_text(self):
        data = self.create_data()
        data['individual-address'] = 'Test'
        signup = ISignupForm(data)
        self.assertFalse(signup.is_valid(), signup.errors)
        
    def test_address_only_num(self):
        data = self.create_data()
        data['individual-address'] = ' 10'
        signup = ISignupForm(data)
        self.assertFalse(signup.is_valid(), signup.errors)


    
class CSignupTestCase(TestCase):
    def create_data(self):
        return {'user-username':'Test@Company.com',
                'user-password1':'abcdefg789',
                'user-password2':'abcdefg789',
                'company-name':'Company',
                'company-contact_email':'Contact@Company.com',
                'company-phone_number':'1234567',
                'company-address':'Street 123',
                'company-description':'Generic Company'}
    
    def test_successful_cSignup(self):
        signup = CSignupForm(self.create_data())
        self.assertTrue(signup.is_valid(), signup.errors)

    def test_num_not_numeric(self):
        data = self.create_data()
        data['company-phone_number'] = '12e4567'
        signup = CSignupForm(data)
        
        self.assertFalse(signup.is_valid(), signup.errors)
