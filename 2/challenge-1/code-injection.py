from flask import Flask, request
app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    # Use a safe method to evaluate the code
    from ast import literal_eval
    try:
        result = literal_eval(code)
    except (ValueError, SyntaxError):
        result = "Invalid input"
    return str(result)