from django.urls import path
from users.views import UserActivityView

urlpatterns = [
    # User_activity
    path('user_activity/', UserActivityView.as_view(), name='user_activity'),
]
