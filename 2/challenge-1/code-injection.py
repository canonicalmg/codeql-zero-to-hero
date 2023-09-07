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
            safe_eval = lambda code: eval(compile(parsed_code, '<string>', 'eval'), {'__builtins__': None}, {})
            result = safe_eval(code)
        else:
            raise ValueError("Invalid code")
    except (SyntaxError, ValueError, TypeError):
        result = "Error: Invalid or unsafe code"
    return str(result)