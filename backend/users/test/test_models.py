from django.test import TestCase

from users.models import CustomUser


class CustomUserModelTest(TestCase):
    """ Test user creation """

    @staticmethod
    def create_superuser():
        """ Create and return a CustomUser for testing """

        return CustomUser.objects.create_superuser(
            username='admin',
            password='adminpassword'
        )

    def setUp(self):
        self.superuser = self.create_superuser()

    def test_create_superuser(self):
        self.client.login(username=self.superuser.username, password='adminpassword')

        superuser = CustomUser.objects.get(username=self.superuser.username)

        self.assertEqual(superuser.username, self.superuser.username)
        self.assertTrue(superuser.check_password('adminpassword'))
        self.assertIsNotNone(superuser.last_login)
        self.assertIsNone(superuser.last_request)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)

    def test_str_representation(self):
        self.assertEqual(str(self.superuser), self.superuser.username)
