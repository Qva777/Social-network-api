import os
import random
import requests
from rest_framework import status
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('HOST')

class UserService:
    @staticmethod
    def signup_user(username, password):
        """ Sign up a new user"""
        signup_url = f"{HOST}/api/auth/users/"
        signup_data = {"username": username, "password": password}
        response = requests.post(signup_url, json=signup_data)
        return response


class PostService:
    @staticmethod
    def get_random_post_id(user_token, excluded_posts):
        """ Get a random post ID"""
        headers = {"Authorization": f"Bearer {user_token}"}
        posts_url = f"http://localhost:8000/api/posts/?limit=1&offset={random.randint(0, 10)}"
        response = requests.get(posts_url, headers=headers)

        if response.status_code == status.HTTP_200_OK and response.json():
            available_posts = [post['id'] for post in response.json() if post['id'] not in excluded_posts]
            if available_posts:
                return random.choice(available_posts)
        elif response.status_code == status.HTTP_200_OK:
            print("No posts available to like. Response:", response.json())
        else:
            print("Error fetching posts. Status Code:", response.status_code)

        return None

    @staticmethod
    def create_post(user_token):
        """ Create a new post """
        create_post_url = f"{HOST}/api/posts/"
        post_data = {
            "title": f"Post Title {random.randint(1, 100)}",
            "content": f"Post Content {random.randint(1, 100)}"
        }
        headers = {"Authorization": f"Bearer {user_token}"}
        response = requests.post(create_post_url, json=post_data, headers=headers)
        return response

    @staticmethod
    def like_post(user_token, post_id):
        """ Like a post"""
        like_post_url = f"{HOST}/api/posts/{post_id}/like/"
        headers = {"Authorization": f"Bearer {user_token}"}
        response = requests.post(like_post_url, headers=headers)
        return response


class AuthService:
    @staticmethod
    def get_user_token(username):
        """ Get JWT token for the user"""
        token_url = f"{HOST}/api/token/"
        token_data = {"username": username, "password": f"password_{username.split('_')[1]}"}
        response = requests.post(token_url, json=token_data)
        return response.json()["access"]
