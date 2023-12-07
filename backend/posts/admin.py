from django.contrib import admin
from posts.models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Field in admin panel """
    list_display = ('title', 'user', 'content', 'created_at')
    list_display_links = ('title', 'user', 'content')
    search_fields = ('title', 'user', 'content')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """ Field in admin panel """
    list_display = ('user', 'post', 'created_at')
    list_display_links = ('user', 'post')
    search_fields = ('user', 'post')
