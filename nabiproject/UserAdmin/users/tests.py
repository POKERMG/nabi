from django.test import TestCase
from .models import User


# Create your tests here.
class UsersTest(TestCase):

    def create_user(self):
        return User.objects.create(username='testers', email='testers@gmail.com',password='pingpong')

    def test_user_creation(self):
        user = self.create_user()
        self.assertTrue(isinstance(user,User))
        self.assertEqual(user.__str__(),user.email)