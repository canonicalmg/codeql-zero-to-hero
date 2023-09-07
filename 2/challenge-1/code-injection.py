from flask import Flask, request
import ast
import sys
from io import StringIO

app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        # Safely evaluate the code
        code_ast = ast.parse(code, mode='exec')
        exec(compile(code_ast, '<string>', 'exec'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Restore stdout
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

    return output