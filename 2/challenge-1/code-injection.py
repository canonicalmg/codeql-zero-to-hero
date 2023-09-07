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
            safe_eval = types.FunctionType(ast.compile(parsed_code, "", "eval"), {})
            result = safe_eval()
        else:
            raise ValueError("Invalid code")
    except Exception as e:
        result = str(e)

    return str(result)