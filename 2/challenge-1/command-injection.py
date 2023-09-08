import re
import os
import subprocess
from werkzeug.utils import secure_filename
from flask import Flask, request

app = Flask(__name__)

@app.route("/command1")
def command_injection1():
    files = request.args.get('files', '')
    safe_files = secure_filename(files)
    os.system("ls " + safe_files) # $result=GOOD

@app.route("/command2")
def command_injection2():
    files = request.args.get('files', '')
    safe_files = secure_filename(files)
    subprocess.Popen("ls " + safe_files, shell=True) # $result=GOOD

@app.route("/path-exists-not-sanitizer")
def path_exists_not_sanitizer():
    path = request.args.get('path', '')
    safe_path = secure_filename(path)
    if os.path.exists(safe_path):
        os.system("ls " + safe_path) # $result=GOOD
