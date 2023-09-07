from django.db import connection, models
from django.db.models.expressions import RawSQL
from flask import Flask, request
app = Flask(__name__)

class User(models.Model):
    pass

@app.route("/users/<username>")
def show_user(username):
    with connection.cursor() as cursor:
        # GOOD -- Using parameters
        cursor.execute("SELECT * FROM users WHERE username = %s", [username])
        User.objects.raw("SELECT * FROM users WHERE username = %s", (username,))

        # Remove the BAD examples

    return "User information retrieved"