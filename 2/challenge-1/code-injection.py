from flask import Flask, request
import ast
import types
app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    try:
        parsed_code = ast.parse(code, mode='eval')
        if isinstance(parsed_code, ast.Expression):
            safe_code = compile(parsed_code, '<string>', 'eval')
            result = eval(safe_code)
        else:
            raise ValueError("Invalid code")
    except (SyntaxError, ValueError):
        return "Error: Invalid code provided"
    return str(result)