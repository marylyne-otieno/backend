
from flask import request, make_response
from .models import User, db
from flask_restful import Resource
from flask_jwt_extended import create_access_token

class Register(Resource):
    def post(self):
        data = request.get_json(force=True)  # Force ensures JSON is parsed
        print("REGISTER DATA:", data)

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
        print("LOGIN DATA:", data)

        username = data.get("username")
        password = data.get("password")

        if not all([username, password]):
            return {"message": "Username and password are required"}, 400

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            access_token = create_access_token(identity=user.username)
            return {
                "access_token": access_token,
                "user": {"id": user.id, "username": user.username}
            }, 200

        return {"message": "Invalid credentials"}, 401
