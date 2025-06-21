
from flask import jsonify, request
from flask_restful import Resource, Api
from app import create_app, db
from app.models import User, Profile, Post

app = create_app()
api = Api(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Profile': Profile, 'Post': Post}

# '''''''''
# USERS
#
'''
@app.route("/users/<int:id>", methods=["PATCH"])
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if "username" in data:
        user.username = data["username"]
    if "email" in data:
        user.email = data["email"]
    if "bio" in data:
        if user.profile:
            user.profile.bio = data["bio"]
        else:
            new_profile = Profile(bio=data["bio"], user=user)
            db.session.add(new_profile)
        db.session.commit()
        return jsonify({
        "message": "User updated successfully",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "profile": user.profile.bio if user.profile else None
        }
    })

    @app.route("/users/<int:id>", methods=["DELETE"])
    def delete_user(id):
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"User with id{id} deleted successfully"})

'''
if __name__ == '__main__':
    app.run(debug=True)
