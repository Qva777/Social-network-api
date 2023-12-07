from django.test import TestCase
from django.utils import timezone
from django.utils.timezone import localtime
from users.serializer import UserActivitySerializer
from users.test.test_models import CustomUserModelTest


class UserActivitySerializerTest(TestCase):
    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()

        self.superuser.last_login = timezone.now()
        self.superuser.last_request = timezone.now()
        self.superuser.save()

    def test_user_activity_serializer(self):
        """ Test UserActivitySerializer data """
        serializer = UserActivitySerializer(instance=self.superuser)

        self.assertEqual(serializer.data['last_login'], localtime(self.superuser.last_login).isoformat())
        self.assertEqual(serializer.data['last_request'], localtime(self.superuser.last_request).isoformat())
