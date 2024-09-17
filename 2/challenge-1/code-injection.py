from flask import Flask, request
import ast
import sys
from io import StringIO

app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    
    # Check if the code is a single expression
    try:
        node = ast.parse(code, mode='eval')
    except SyntaxError:
        return "Invalid code. Please provide a single expression."

    # Redirect stdout to capture the output
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        # Safely evaluate the expression
        result = eval(compile(node, '<string>', 'eval'))
        output = sys.stdout.getvalue()
    except Exception as e:
        output = str(e)
    finally:
        # Restore stdout
        sys.stdout = old_stdout

    return output