from django.core.exceptions import ValidationError
from django.test import TestCase
from stocks.models import User
from django.db.utils import IntegrityError

class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='johndoe',
            password='Password123'
        )

    def create_second_user(self):
        user = User.objects.create_user(
            username='janedoe',
            password='Password123'
        )

        return user

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        user2 = self.create_second_user()
        self.user.username = user2.username
        self._assert_user_is_invalid()
    
    def test_username_cannot_be_longer_than_30_characters(self):
        self.user.username = "a"*31
        self._assert_user_is_invalid()
    
    def test_username_can_have_numbers(self):
        self.user.username = 'johndoe1'
        self._assert_user_is_valid()
    
    def test_username_can_have_symbols(self):
        self.user.username = 'johndoe@'
        self._assert_user_is_valid()
    
        