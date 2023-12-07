from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from posts.serializers import PostSerializer
from posts.repositories.repositories import PostRepository
from posts.services.services import PostService


class PostCreateView(APIView):
    """ View for creat/list of post """
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, *args, **kwargs):
        posts = PostRepository.get_all_posts()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            PostRepository.update_last_request(request.user)

            post = PostRepository.create_post(
                request.user,
                serializer.validated_data['content'],
                serializer.validated_data['title']
            )
            return Response({'message': 'Post created successfully', 'id': post.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostLikeView(APIView):
    """ View for liking a post """
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, post_id, *args, **kwargs):
        post = PostRepository.get_post_by_id(post_id)
        PostRepository.update_last_request(request.user)

        if not post:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        PostRepository.like_post(post, request.user)
        return Response({'message': 'Post liked successfully'}, status=status.HTTP_200_OK)


class PostUnlikeView(APIView):
    """ View for unliking a post """
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, post_id, *args, **kwargs):
        post = PostRepository.get_post_by_id(post_id)
        PostRepository.update_last_request(request.user)

        if not post:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        PostRepository.unlike_post(post, request.user)
        return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)


class LikesAnalyticsView(APIView):
    """ View for retrieving likes analytics aggregated by day """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if not date_from or not date_to:
            return Response({'error': 'Both date_from and date_to parameters are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            date_from = timezone.datetime.strptime(str(date_from), "%Y-%m-%d")
            date_to = timezone.datetime.strptime(str(date_to), "%Y-%m-%d")
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        likes_analytics = PostService.get_likes_analytics(date_from, date_to)
        return Response(likes_analytics, status=status.HTTP_200_OK)
