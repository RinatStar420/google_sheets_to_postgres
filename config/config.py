import os

database = {
    "db_user": os.environ.get("DATABASE_USER"),
    "db_password": os.environ.get("DATABASE_PASSWORD"),
    "db": os.environ.get("DATABASE"),
    "host": os.environ.get("HOST"),
    "port": os.environ.get("PORT")
    }