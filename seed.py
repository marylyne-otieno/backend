
from app import app
from app.models import db, User

with app.app_context():
    User.query.delete()

    # Create users
    user1 = User(username="marylyne", email="mary@example.com")
    user2 = User(username="john_doe", email="john@example.com")
    user3 = User(username="jane_doe", email="jane@example.com")

    # Add users to session
    db.session.add_all([user1, user2, user3])

    # Commit to database
    db.session.commit()

