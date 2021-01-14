from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email normalize function for a new user"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raised error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    def test_create_superuser(self):
        """Tests creation of superuser with staff setting"""
        user = get_user_model().objects.create_superuser(
            'admin@admin.com', 'password'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
