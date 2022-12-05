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

    def test_new_user_email_normalized(self):
        """Testing that new user's emails are normalized"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email(self):
        """Test that creating a new user with invalid email address raises a value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "sample123")

    def test_create_superuser(self):
        """Test that a super user created"""
        user = get_user_model().objects.create_superuser("test@example.com", "123456")
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.is_admin)
