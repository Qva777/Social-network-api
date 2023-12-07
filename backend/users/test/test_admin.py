from django.urls import reverse
from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from rest_framework import status

from users.test.test_models import CustomUserModelTest


class CustomUserAdminTest(TestCase):
    """ Test admin panel """

    def setUp(self):
        self.superuser = CustomUserModelTest.create_superuser()

        self.site = AdminSite()

    def test_custom_user_admin_list_display(self):
        self.client.force_login(self.superuser)
        url = reverse('admin:users_customuser_changelist')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, 'username')
        self.assertContains(response, 'is_superuser')
        self.assertContains(response, 'is_active')

    def test_custom_user_admin_search_fields(self):
        self.client.force_login(self.superuser)

        url = reverse('admin:users_customuser_changelist')
        response = self.client.get(url, {'q': 'admin'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'admin')
