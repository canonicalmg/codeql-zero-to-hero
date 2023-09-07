from flask import Flask, request
import ast
import types

app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    try:
        parsed_code = ast.parse(code, mode='exec')
        exec(compile(parsed_code, '<string>', 'exec'))
    except Exception as e:
        return str(e)
    return "Code executed successfully"