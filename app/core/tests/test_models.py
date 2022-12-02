"""
Testing models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests for models"""

    def test_create_user_with_email_successfull(self):
        """Test happy path for creating a user with email (success)"""

        email = "test@example.com"
        password = "123456"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))