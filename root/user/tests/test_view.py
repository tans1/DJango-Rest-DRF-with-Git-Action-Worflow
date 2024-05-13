from .test_setup import UserTestSetUp

class TestUserViews(UserTestSetUp):
    def test_user_register_without_any_data(self):
        """
        Expected Outcome:
        The test expects the registration endpoint to handle the request gracefully even when no data is provided,
        returning an error response with a status code of 400.
        """
        response = self.client.post(self.register_url,format="json")
        
        self.assertEqual(response.status_code, 400)
    
    def test_user_successful_registration(self):
        """
        Expected Outcome:
        The test will pass and the user will successfully registered
        """
        
        result = self.client.post(self.register_url, self.valid_user_data_to_register, format="json")
        
        self.assertEqual(result.status_code, 201)
        