from flask import Flask, request
import ast
import sys
app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    try:
        safe_code = ast.literal_eval(code)
    except (ValueError, SyntaxError):
        return "Invalid input. Please provide a safe expression."

    return str(safe_code)