from django.test import TestCase
from ..models import User


class TestUserModel(TestCase):
    def setUp(self):
        self.user = User(username='test', password='test')
        self.user.save()

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
