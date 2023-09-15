@app.route("/command1")
def command_injection1():
    files = request.args.get('files', '')
    # Use an allowlist to ensure only valid commands are executed
    allowed_files = ["file1", "file2", "file3"]
    if files in allowed_files:
        os.system("ls " + files) # $result=GOOD
    else:
        return "Invalid file request"

@app.route("/command2")
def command_injection2():
    files = request.args.get('files', '')
    # Use an allowlist to ensure only valid commands are executed
    allowed_files = ["file1", "file2", "file3"]
    if files in allowed_files:
        subprocess.Popen("ls " + files, shell=True) # $result=GOOD
    else:
        return "Invalid file request"

@app.route("/path-exists-not-sanitizer")
def path_exists_not_sanitizer():
    path = request.args.get('path', '')
    # Use an allowlist to ensure only valid paths are accessed
    allowed_paths = ["path1", "path2", "path3"]
    if path in allowed_paths:
        os.system("ls " + path) # $result=GOOD
    else:
        return "Invalid path request"