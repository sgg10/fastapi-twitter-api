from typing import List

from fastapi import FastAPI
from fastapi import status

from app.models.user import User, UserLogin
from app.models.tweet import Tweet

app = FastAPI()

# Paths Operations

## Users

@app.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=['Users']
)
def signup():
    pass

@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=['Users']
)
def login():
    pass

@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all user",
    tags=['Users']
)
def show_all_users():
    pass

@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show user",
    tags=['Users']
)
def show_user():
    pass

@app.delete(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=['Users']
)
def delete_user():
    pass

@app.put(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Update a user",
    tags=['Users']
)
def update_user():
    pass


## Tweets

@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all tweets",
    tags=['Tweets']
)
def home():
    return { "Twitter API": "Working!" }

@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=['Tweets']
)
def post():
    pass

@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show tweet",
    tags=['Tweets']
)
def show_tweet():
    pass

@app.delete(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=['Tweets']
)
def delete_tweet():
    pass

@app.put(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Update a tweet",
    tags=['Tweets']
)
def update_tweet():
    pass

