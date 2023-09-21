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
        User.objects.raw("SELECT * FROM users WHERE username = %s", [username])

        # GOOD -- Using RawSQL with parameters
        User.objects.annotate(RawSQL("insert into names_file ('name') values (%s)", [username]))
        User.objects.raw("insert into names_file ('name') values (%s)", [username])
        User.objects.extra("insert into names_file ('name') values (%s)", [username])