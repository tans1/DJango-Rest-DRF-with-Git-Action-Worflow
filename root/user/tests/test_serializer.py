from .test_setup import UserTestSetUp
from django.test import TestCase
from user.serializers import RegisterUserSerializer

class UserSerializerTest(UserTestSetUp, TestCase):
    def test_registration_serializer(self):
        """ 
        Here we will test the serializer
        """
        
        result = RegisterUserSerializer(data=self.invalid_user_data_to_register)
        self.assertEqual(result.is_valid(), False)
        