import uuid
from users.models import CustomUser

from django.db import models
from django.utils import timezone


class Post(models.Model):
    """ Model for user posts """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=125, unique=True, blank=False)
    content = models.TextField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """ String representation of a post """
        return self.title

    class Meta:
        """ Meta information for the Post model """
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Like(models.Model):
    """ Model for post likes """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """ String representation of a like """
        return f"Like by {self.user.username} on {self.post}"

    class Meta:
        """ Meta information for the Like model """
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
