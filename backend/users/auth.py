from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

from users.repositories.repositories import UserRepository


class CustomTokenObtainPairView(TokenObtainPairView):
    """ Custom token JWT """

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            user = get_user_model().objects.get(username=request.data['username'])
            UserRepository.update_last_login(user)

        return response
