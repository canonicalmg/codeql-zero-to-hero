import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

ALLOWED_FILES = ["file1", "file2", "file3"]

@app.route("/command1")
def command_injection1():
    files = request.args.get('files', '')
    if files in ALLOWED_FILES:
        os.system("ls " + files)
    else:
        return "Invalid file request"

@app.route("/command2")
def command_injection2():
    files = request.args.get('files', '')
    if files in ALLOWED_FILES:
        subprocess.Popen("ls " + files, shell=True)
    else:
        return "Invalid file request"

@app.route("/path-exists-not-sanitizer")
def path_exists_not_sanitizer():
    path = request.args.get('path', '')
    if path in ALLOWED_FILES and os.path.exists(path):
        os.system("ls " + path)
    else:
        return "Invalid path request"
