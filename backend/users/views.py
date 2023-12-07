from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from posts.repositories.repositories import PostRepository
from users.repositories.repositories import UserRepository
from users.serializer import UserActivitySerializer


class UserActivityView(APIView):
    """ View for retrieving user activity """
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, *args, **kwargs):
        user = request.user

        if user.is_authenticated:

            serializer = UserActivitySerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
