
from flask import request, jsonify
from .models import User, Profile, Post, db
from flask_restful import Resource, Api, reqparse

# Request parser for validation
user_parser = reqparse.RequestParser()
user_parser.add_argument('username', required=True, help="Username is required")
user_parser.add_argument('email', required=True, help="Email is required")


# USERS Resource
class UserListResource(Resource):

    def get(self):
        users = User.query.all()
        users_list = []

        for user in users:
            users_list.append({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "profile": user.profile.bio if user.profile else None,
                "posts": [
                    {
                        "id": post.id,
                        "title": post.title,
                        "content": post.content
                    } for post in user.posts
                ]
            })
        return jsonify(users_list)

    def post(self):
        args = user_parser.parse_args()
        user = User(username=args["username"], email=args["email"])
        db.session.add(user)
        db.session.commit()
        return {'id': user.id, 'message': "User created successfully"}, 201


# Register the resource
def register_resources(api):
    api.add_resource(UserListResource, '/users')
