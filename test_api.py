import requests
import json
import pytest


def get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    for x in response:
        print(x['title'])


def get_one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/post/1').json()


def post_new_post():
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
    }
    body = json.dumps({

        "userId": 1,
        "title": "foo",
        "body": "dooo"
    })
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        data=body,
        headers=headers
    )
    print(response.json())
    print(response.status_code)


def update_post():
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
    }
    body = json.dumps({

        "userId": 1,
        "title": "foo1",
        "body": "dooo2"
    })
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/1',
        data=body,
        headers=headers
    )
    print(response.json())


update_post()
