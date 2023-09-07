from flask import Flask, request
import ast
import sys
import io
app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    if code is None:
        return "No code provided", 400

    try:
        parsed_code = ast.parse(code, mode='exec')
    except SyntaxError:
        return "Invalid code syntax", 400

    safe_nodes = {ast.Module, ast.Expr, ast.Load, ast.Call, ast.Name, ast.Str, ast.Num, ast.BinOp, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow}

    for node in ast.walk(parsed_code):
        if type(node) not in safe_nodes:
            return "Unsafe code detected", 400

    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    try:
        exec(compile(parsed_code, "<string>", "exec"))
    except Exception as e:
        return f"Error executing code: {e}", 400
    finally:
        sys.stdout = old_stdout

    return redirected_output.getvalue()