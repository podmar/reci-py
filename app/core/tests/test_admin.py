"""Test for the django admin custom setup"""

from django.test import (TestCase, Client)
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django Admin"""

    def setUp(self):
        """Create a user and a client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            "test_admin@example.com", "123456"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            "test@example.com", "123456", name="Test User"
        )

    def test_users_list(self):
        """Test that the users are listed"""
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
