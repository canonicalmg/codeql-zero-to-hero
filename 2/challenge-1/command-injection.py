import re
import os
import subprocess
from shlex import quote
from flask import Flask, request
app = Flask(__name__)

@app.route("/command1")
def command_injection1():
    files = request.args.get('files', '')
    safe_files = quote(files)
    os.system("ls " + safe_files)

@app.route("/command2")
def command_injection2():
    files = request.args.get('files', '')
    safe_files = quote(files)
    subprocess.Popen("ls " + safe_files, shell=True)

@app.route("/path-exists-not-sanitizer")
def path_exists_not_sanitizer():
    path = request.args.get('path', '')
    if os.path.exists(path):
        safe_path = quote(path)
        os.system("ls " + safe_path)