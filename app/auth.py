
from flask import request, make_response
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from .models import User, db

class Register(Resource):
    def post(self):
        data = request.get_json(force=True)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not all([username, email, password]):
            return {"message": "All fields are required"}, 400

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 400
        if User.query.filter_by(email=email).first():
            return {"message": "Email already exists"}, 400

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully"}, 201


class Login(Resource):
    def post(self):
        data = request.get_json(force=True)
        username_or_email = data.get("username") or data.get("email")
        password = data.get("password")

        user = User.query.filter(
            (User.username == username_or_email) | (User.email == username_or_email)
        ).first()

        if user and user.check_password(password):
            token = create_access_token(identity=user.username)
            return {"access_token": token}, 200

        return {"message": "Invalid credentials"}, 401


def register_user_resources(api):
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')
