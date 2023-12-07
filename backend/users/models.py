from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """ Extended User model with additional fields """

    last_login = models.DateTimeField(_("last login"), blank=True, null=True)
    last_request = models.DateTimeField(_("last request"), blank=True, null=True)

    def __str__(self):
        """ String representation """
        return self.username

    class Meta:
        """ Representation in the admin panel """
        verbose_name = 'User'
        verbose_name_plural = 'Users'
