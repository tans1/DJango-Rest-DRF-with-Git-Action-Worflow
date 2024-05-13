from rest_framework.test import APITestCase
from django.urls import reverse # to get the route to a view by the view name
from faker import Faker
from user.models import User


class UserTestSetUp(APITestCase):
    
    def setUp(self) -> None:
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_details_url = reverse('user-details')
        self.fake = Faker()
        
        password = self.fake.password(length=8, special_chars=True, upper_case=True, lower_case=True)
        
        self.valid_user_data_to_register = {
            'username' : self.fake.user_name(), 
            'email' : self.fake.email(), 
            'password' : password,
            'confirm_password' : password,
            'first_name' : self.fake.first_name(),
            'last_name' : self.fake.last_name(),
        }
        
        self.invalid_user_data_to_register = {
            'username' : self.fake.user_name(), 
            'email' : '', 
            'password' : password,
            'confirm_password' : password,
            'first_name' : self.fake.first_name(),
            'last_name' : self.fake.last_name(),
        }
        
        self.user_model_data = {
            'username' : 'testuser', 
            'email' : 'test@example.com', 
            'password' : '1234567890',
            'first_name' : 'test',
            'last_name' : 'test'
        }
        
        self.user = User.objects.create(**self.user_model_data)

        
        
        return super().setUp()
    
    
    def tearDown(self) -> None:
        return super().tearDown()
    