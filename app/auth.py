
from flask import request, make_response
from .models import User, db
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token


# Define parser for registration input
register_parser = reqparse.RequestParser()
register_parser.add_argument('username', required=True, help="Username is required")
register_parser.add_argument('email', required=True, help="Email is required")
register_parser.add_argument('password', required=True, help="Password is required")


login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True, help="Username is required")
login_parser.add_argument('password', required=True, help="Password is required")

class Register(Resource):
    def post(self):
        args = register_parser.parse_args()
        print("===", args)

        # Check if username already exists

        if User.query.filter_by(username=args["username"]).first():
            return {"message": "Username already exists"}, 400
        if User.query.filter_by(email=args["email"]).first():
            return {"message": "Email already exists"}, 400


        user = User(username=args['username'], email=args['email'])
        user.set_password(password=args['password'])  # assuming you have a set_password method

        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully"}, 201



class Login(Resource):
    def post(self):
     args = register_parser.parse_args()

        # Check if username already exists

     user = User.query.filter_by(username=args["username"]).first()
     resp = make_response("cookie set")
     resp.set_cookie('user', user, max_age=24*60*60)
     if user and user.check_password(args["password"]):
        access_token = create_access_token(identity=user.username)
        return {"access_token": access_token, "user": {"id": user.id, "username": user.username}}, 200
     return{"message": "Invalid creditials"}, 401






def register_user_resources(api):
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')


