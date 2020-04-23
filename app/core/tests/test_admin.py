from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

test_email = "linuxer@courses.com"
test_email_admin = "admin@courses.com"
test_password = "Testpass123"


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email=test_email_admin, password=test_password
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email=test_email, password=test_password, name="Test User Full Name",
        )

    def test_users_listed(self):
        """
        Test that users are listed on the user page
        """
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """
        Test that the user edit page works
        """
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """
        Test that the create user page works
        """
        url = reverse("admin:core_user_add")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
