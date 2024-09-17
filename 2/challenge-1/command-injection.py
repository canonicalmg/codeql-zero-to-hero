@app.route("/command1")
def command_injection1():
    files = request.args.get('files', '')
    os.system("ls " + re.escape(files))


@app.route("/command2")
def command_injection2():
    files = request.args.get('files', '')
    subprocess.Popen("ls " + re.escape(files), shell=True)


@app.route("/path-exists-not-sanitizer")
def path_exists_not_sanitizer():
    path = request.args.get('path', '')
    if os.path.exists(path):
        os.system("ls " + re.escape(path))