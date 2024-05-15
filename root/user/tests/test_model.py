from .test_setup import UserTestSetUp
from django.db.utils import IntegrityError
from user.models import User

class UserModelTest(UserTestSetUp):
    def test_user_creation(self):
        """Test if user is created properly."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')

    def test_unique_email_constraint(self):
        """Test if the unique email constraint works."""
        # Attempt to create a user with the same email should raise IntegrityError
        with self.assertRaises(IntegrityError):
            User.objects.create(username='anotheruser', email='test@example.com')

    def test_user_str_representation(self):
        """Test if the __str__ method returns the username."""
        self.assertEqual(str(self.user), 'testuser')
