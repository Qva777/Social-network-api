# Social Network REST API and Automated Bot

<!-- ABOUT -->
> This project involves creating a simple REST API
> for a social network, accompanied by an automated
> bot that demonstrates the system's functionalities
> based on predefined rules.
<!-- END ABOUT -->

<hr>

<h1>📍How to install: </h1>

<!-- POSTMAN -->
<details><summary><h2>📮Connect to Postman:</h2></summary><br/>
<h3><b>1.1</b> Import `Postman Collections`folder into Postman</h3>
<h3><b>1.2</b> Set the environment settings `Social network.postman_environment`</h3>
<h3><b>1.3</b> The `Social Network.postman_collection` collection contains requests</h3>
</details>
<!-- END POSTMAN -->


<!-- DOCKER -->
<details><summary><h2>🐳Connect to Docker Compose:</h2></summary><br/>

<h4>Create Your .env and set correct values look at .env.example</h4>

<h3>UP Docker-compose:</h3>

```
docker-compose -f docker/docker-compose.yml up --build
```

<h3>Login to the container console:</h3>

```
docker exec -it django_container bash
```

<h3>Create superuser:</h3>

```
python manage.py createsuperuser
```

</details>
<!-- END DOCKER -->

<!-- BOT -->
<details>
  <summary><h2>🤖Automated bot(run docker before)</h2></summary>

<h3>Set your data in bot config.json:</h3>

<h3>Run Bot:</h3>

```
python bot.py
```

</details>
<!-- END BOT -->

# Endpoints

## Authentication Endpoints

- **POST** `/api/token/`: Log in and receive a JWT token.
- **POST** `/api/token/refresh/`: Refresh the JWT token.

## User Management Endpoints

- **POST** `/api/auth/users/`: Create a new user.
- **GET** `/api/auth/users/me/`: .
- **GET** `/api/user_activity/`: Retrieve information about the user's activity, including the last login time and the
  timestamp of the last request made to the service

## Posts Endpoints

- **GET** `/api/posts/`: Retrieve a list of all posts.
- **POST** `/api/posts/`: Create a new post.
- **POST** `/api/posts/{{last_post}}/like/`: Like a specific post.
- **POST** `/api/posts/{{last_post}}/unlike/`: Unlike a previously liked post.
- **GET** `/api/analytics/?date_from=2022-01-01&date_to=2024-12-31`: Retrieve analytics data for the number of likes
  aggregated by day within the specified date range.