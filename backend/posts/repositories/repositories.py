from django.utils import timezone
from django.db.models import Count
from django.shortcuts import get_object_or_404
from posts.models import Post, Like


class PostRepository:
    @staticmethod
    def get_post_by_id(post_id):
        return get_object_or_404(Post, id=post_id)

    @staticmethod
    def create_post(user, content, title):
        post = Post(user=user, content=content, title=title)
        post.save()
        return post

    @staticmethod
    def get_all_posts():
        return Post.objects.all()

    @staticmethod
    def like_post(post, user):
        Like.objects.get_or_create(post=post, user=user)

    @staticmethod
    def unlike_post(post, user):
        Like.objects.filter(post=post, user=user).delete()

    @staticmethod
    def get_likes_analytics(date_from, date_to):
        return Like.objects.filter(
            created_at__date__range=[date_from, date_to],
            post__isnull=False
        ).values('created_at__date').annotate(likes_count=Count('id'))

    @staticmethod
    def update_last_request(user):
        user.last_request = timezone.now()
        user.save()
