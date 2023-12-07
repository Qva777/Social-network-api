from django.contrib import admin
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """ Field in admin panel """
    list_display = ('username', 'is_superuser', 'is_active')
    list_display_links = ('username',)
    search_fields = ('username',)
