from django.test import TestCase
from posts.models import Post, Like
from users.test.test_models import CustomUserModelTest


class PostModelTest(TestCase):
    """ Test post creation """

    @staticmethod
    def create_post(user):
        """ Create and return a Post for testing """
        return Post.objects.create(
            user=user,
            title='Test Post',
            content='This is a test post content.'
        )

    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()
        self.post = self.create_post(self.superuser)

    def test_post_attributes(self):
        self.assertEqual(self.post.user, self.superuser)
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.content, 'This is a test post content.')
        self.assertIsNotNone(self.post.created_at)

    def test_post_string_representation(self):
        post = Post.objects.create(
            user=self.superuser,
            title='Test Post 1',
            content='This is a test post content.'
        )
        self.assertEqual(str(post), 'Test Post 1')


class LikeModelTest(TestCase):
    """ Test creating a Like object """

    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()
        self.post = PostModelTest.create_post(self.superuser)

    def test_create_like(self):
        like = Like.objects.create(
            user=self.superuser,
            post=self.post
        )
        self.assertEqual(like.user, self.superuser)
        self.assertEqual(like.post, self.post)
        self.assertIsNotNone(like.created_at)

    def test_like_string_representation(self):
        like = Like.objects.create(
            user=self.superuser,
            post=self.post
        )
        expected_representation = f"Like by {self.superuser.username} on {self.post}"
        self.assertEqual(str(like), expected_representation)
