from django.urls import path
from posts import views

urlpatterns = [
    # Create Post
    path('posts/', views.PostCreateView.as_view(), name='post_create'),

    # set Like/Unlike
    path('posts/<str:post_id>/like/', views.PostLikeView.as_view(), name='post_like'),
    path('posts/<str:post_id>/unlike/', views.PostUnlikeView.as_view(), name='post_unlike'),

    # Analytics aggregated by day
    path('analytics/', views.LikesAnalyticsView.as_view(), name='likes_analytics'),
]
