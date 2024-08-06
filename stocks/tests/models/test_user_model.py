from django.core.exceptions import ValidationError
from django.test import TestCase
from stocks.models import User

class UserModelTestCase(TestCase):

    def test_username_cannot_be_blank(self):
        user = User.objects.create_user(
            username = 'yaseryl',
            password = 'Password123'
        )
        user.username = '' 
        with self.assertRaises(ValidationError):
            user.full_clean()
