import re
import os
import subprocess

from flask import Flask, request
app = Flask(__name__)

ALLOWED_FILES = ["file1", "file2", "file3"]

def is_valid_file(file):
    return file in ALLOWED_FILES

@app.route("/command1")
def command_injection1():
    files = request.args.get('files', '')
    if is_valid_file(files):
        os.system("ls " + files)

@app.route("/command2")
def command_injection2():
    files = request.args.get('files', '')
    if is_valid_file(files):
        subprocess.Popen("ls " + files, shell=True)

@app.route("/path-exists-not-sanitizer")
def path_exists_not_sanitizer():
    path = request.args.get('path', '')
    if os.path.exists(path) and is_valid_file(path):
        os.system("ls " + path)