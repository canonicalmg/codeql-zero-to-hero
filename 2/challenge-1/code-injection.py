@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    if code:
        try:
            safe_globals = {"__builtins__": None}
            safe_locals = {}
            exec(code, safe_globals, safe_locals)
        except Exception as e:
            return str(e)
    return "Code executed successfully"