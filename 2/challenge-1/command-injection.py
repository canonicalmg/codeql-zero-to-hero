import re
import os
import subprocess
from shlex import quote
from flask import Flask, request

app = Flask(__name__)

@app.route("/command1")
def command_injection1():
    files = request.args.get('files', '')
    # Don't let files be `; rm -rf /`
    os.system("ls " + quote(files)) # $result=GOOD

@app.route("/command2")
def command_injection2():
    files = request.args.get('files', '')
    # Don't let files be `; rm -rf /`
    subprocess.Popen("ls " + quote(files), shell=True) # $result=GOOD

@app.route("/path-exists-not-sanitizer")
def path_exists_not_sanitizer():
    path = request.args.get('path', '')
    if os.path.exists(path):
        os.system("ls " + quote(path)) # $result=GOOD