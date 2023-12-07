from rest_framework import serializers
from users.models import CustomUser


class UserActivitySerializer(serializers.ModelSerializer):
    """ Displaying user activity information """
    class Meta:
        model = CustomUser
        fields = ['last_login', 'last_request']
