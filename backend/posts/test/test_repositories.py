from django.test import TestCase
from posts.models import Post
from posts.repositories.repositories import PostRepository
from posts.test.test_models import PostModelTest
from users.test.test_models import CustomUserModelTest


class PostRepositoryTest(TestCase):
    """ Test PostRepositoryTest """
    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()
        self.post = PostModelTest.create_post(self.superuser)

    def test_get_post_by_id(self):
        retrieved_post = PostRepository.get_post_by_id(self.post.id)
        self.assertEqual(retrieved_post, self.post)

    def test_create_post(self):
        new_post = PostRepository.create_post(
            user=self.superuser,
            title='New Post',
            content='This is a new post.'
        )
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(new_post.user, self.superuser)
        self.assertEqual(new_post.title, 'New Post')
