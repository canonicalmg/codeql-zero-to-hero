@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    if code:
        try:
            exec(code, {"__builtins__": None}, {})
        except Exception as e:
            return str(e)
    return "No code provided"