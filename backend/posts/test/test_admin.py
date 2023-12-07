from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from posts.admin import PostAdmin, LikeAdmin
from posts.models import Post, Like
from posts.test.test_models import PostModelTest

from users.test.test_models import CustomUserModelTest


class PostAdminTest(TestCase):

    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()
        self.site = AdminSite()
        self.post = PostModelTest.create_post(self.superuser)

        self.post_admin = PostAdmin(Post, self.site)

    def test_post_admin_list_display(self):
        """ Test list display attributes in PostAdmin """
        self.assertEqual(self.post_admin.list_display, ('title', 'user', 'content', 'created_at'))

    def test_post_admin_list_display_links(self):
        """ Test list display links in PostAdmin """
        self.assertEqual(self.post_admin.list_display_links, ('title', 'user', 'content'))


class LikeAdminTest(TestCase):

    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()
        self.site = AdminSite()
        self.post = PostModelTest.create_post(self.superuser)
        self.like = Like.objects.create(user=self.superuser, post=self.post)

        self.post_admin = PostAdmin(Post, self.site)
        self.like_admin = LikeAdmin(Like, self.site)

    def test_like_admin_list_display(self):
        """ Test list display attributes in LikeAdmin """
        self.assertEqual(self.like_admin.list_display, ('user', 'post', 'created_at'))

    def test_like_admin_list_display_links(self):
        """ Test list display links in LikeAdmin """
        self.assertEqual(self.like_admin.list_display_links, ('user', 'post'))
