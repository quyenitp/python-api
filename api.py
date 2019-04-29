#!/usr/bin/env python
from flask import Flask
from flask_restful import Api, Resource, reqparse

from resources.user import *
from resources.account import *

app = Flask(__name__)
api = Api(app)

users = [
    {
        "id": 1,
        "name": "Jame",
        "accountID": "1,3,5"
    },
    {
        "id": 2,
        "name": "Bond",
        "accountID": "4"
    },
    {
        "id": 3,
        "name": "Jimmy",
        "accountID": "2"
    }

]

accounts = [
    {
        "id": 1,
        "userID": 1,
        "name":"Tiet Kiem",
        "balance":10000

    },
    {
        "id": 2,
        "userID": 3,
        "name":"Tiet Kiem",
        "balance":10000

    },
    {
        "id": 3,
        "userID": 1,
        "name":"Tiet Kiem",
        "balance":10000

    },
    {
        "id": 4,
        "userID": 2,
        "name":"Tiet Kiem",
        "balance":10000

    },
    {
        "id": 5,
        "userID": 1,
        "name":"Tiet Kiem",
        "balance":10000

    }
]


      
api.add_resource(User, "/users/<int:id>", resource_class_kwargs={'users': users})
api.add_resource(UserAccount, "/users/<int:id>/accounts")
api.add_resource(Account, "/accounts/<int:id>", resource_class_kwargs={'accounts': accounts})

app.run(debug=True)