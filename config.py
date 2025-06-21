import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "mary6539")



#class Config:
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
   # SQLALCHEMY_TRACK_MODIFICATIONS = False
   # JWT_SECRET_KEY = 'mary6539'  # Change this!
