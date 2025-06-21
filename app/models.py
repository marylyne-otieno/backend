
from . import db
from sqlalchemy import CheckConstraint
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(237), nullable=False)





    profile = db.relationship('Profile', backref='user', uselist=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return f'<User {self.username}, {self.email}, {self.id}>'


   # one to one relationship
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(129))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Profile {self.bio}>'

    #one to many relationship
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(233))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Post {self.title}, {self.content}>'
