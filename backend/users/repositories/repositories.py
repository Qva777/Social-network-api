from users.models import CustomUser
from django.utils import timezone


class UserRepository:
    @staticmethod
    def get_user_by_id(user_id):
        """ Get a user by ID """
        return CustomUser.objects.get(id=user_id)

    @staticmethod
    def update_last_login(user):
        user.last_login = timezone.now()
        user.save()
