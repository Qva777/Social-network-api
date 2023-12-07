from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """ Serializer for the Post model """

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'created_at']
        extra_kwargs = {
            'user': {'required': False},
        }
