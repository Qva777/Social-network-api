from django.test import TestCase
from django.utils import timezone

from posts.serializers import PostSerializer
from users.test.test_models import CustomUserModelTest


class PostSerializerTest(TestCase):
    """ Test PostSerializerTest """

    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()

        self.post_data = {
            'user': self.superuser.pk,
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'created_at': timezone.now(),
        }

    def test_post_serializer_valid_data(self):
        serializer = PostSerializer(data=self.post_data)
        self.assertTrue(serializer.is_valid())

        self.assertEqual(serializer.validated_data['user'], self.superuser)
        self.assertEqual(serializer.validated_data['title'], 'Test Post')
        self.assertEqual(serializer.validated_data['content'], 'This is a test post content.')

    def test_post_serializer_extra_fields(self):
        extra_data = {
            'user': self.superuser.pk,
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'created_at': '2023-01-01T12:00:00Z',
            'extra_field': 'Extra Field',
        }
        serializer = PostSerializer(data=extra_data)
        self.assertTrue(serializer.is_valid())
        self.assertNotIn('extra_field', serializer.validated_data)
