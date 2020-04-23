from django.test import TestCase
from django.contrib.auth import get_user_model


test_email_username = "linuxer"
test_email_domain = "@courses.com"
test_password = "Testpass123"


class ModelTests(TestCase):
    def test_create_user_with_email_succeful(self):
        """
        Test creating a new with an email is successful
        """
        email = test_email_username + test_email_domain

        user = get_user_model().objects.create_user(email=email, password=test_password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(test_password))

    def test_new_user_email_normalized(self):
        """
        Test the email for a new user is normalized
        """
        email = test_email_username + test_email_domain.upper()
        user = get_user_model().objects.create_user(email, test_password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test creating user with no email raises error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, test_password)

    def test_create_new_superuser(self):
        """
        Test creating a new superuser
        """
        user = get_user_model().objects.create_superuser(
            test_email_username + test_email_domain, test_password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
