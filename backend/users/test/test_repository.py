from django.test import TestCase
from django.utils import timezone

from users.repositories.repositories import UserRepository
from users.test.test_models import CustomUserModelTest


class UserRepositoryTest(TestCase):
    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()

    def test_get_user_by_id(self):
        """ Test UserRepository's get_user_by_id method """

        retrieved_user = UserRepository.get_user_by_id(self.superuser.id)
        self.assertEqual(retrieved_user, self.superuser)

    def test_update_last_login(self):
        """ Test UserRepository's update_last_login method """

        updated_last_login = timezone.now() - timezone.timedelta(days=1)
        self.superuser.last_login = updated_last_login
        UserRepository.update_last_login(self.superuser)
        self.superuser.refresh_from_db()

        delta = timezone.timedelta(seconds=1)
        self.assertLessEqual(updated_last_login - self.superuser.last_login, delta)
