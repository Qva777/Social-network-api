import json
import random
import logging
from rest_framework import status
from services import UserService, PostService, AuthService

logging.basicConfig(level=logging.INFO)


def read_config(file_path):
    """ Read bot_config.json """
    with open(file_path, 'r') as file:
        return json.load(file)


def signup_users(number_of_users):
    """ Create user """
    users = []

    for i in range(0, number_of_users):
        username = f"user_{i}"
        password = f"password_{i}"

        response = UserService.signup_user(username, password)

        if response.status_code == status.HTTP_201_CREATED:
            users.append(username)

    return users


def create_posts(user, max_posts_per_user):
    """ Create Posts """

    user_token = AuthService.get_user_token(user)
    num_posts = random.randint(1, max_posts_per_user)

    for _ in range(num_posts):
        response = PostService.create_post(user_token)
        if response.status_code == status.HTTP_201_CREATED:
            logging.info(f"{user} created a post")


def like_posts(user, max_likes_per_user):
    """ Like posts """
    user_token = AuthService.get_user_token(user)
    liked_posts = set()

    num_likes = random.randint(1, max_likes_per_user)

    for _ in range(num_likes):
        post_id = PostService.get_random_post_id(user_token, liked_posts)
        if post_id is not None:
            response = PostService.like_post(user_token, post_id)
            if response.status_code == status.HTTP_200_OK:
                logging.info(f"{user} liked post {post_id}")
        else:
            logging.info("No posts available to like.")


def run_bot():
    """ Run the bot based on the provided bot_config.json """
    config = read_config('bot_config.json')
    users = signup_users(config['number_of_users'])

    if not users:
        logging.info("Add new user in bot_config.json")

    for user in users:
        create_posts(user, config['max_posts_per_user'])

    for user in users:
        like_posts(user, config['max_likes_per_user'])


if __name__ == "__main__":
    run_bot()
