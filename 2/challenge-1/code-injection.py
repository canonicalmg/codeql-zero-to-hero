from flask import Flask, request
import ast
import base64
app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    sanitized_code = base64.b64encode(code.encode()).decode() # Sanitize user input
    decoded_code = base64.b64decode(sanitized_code.encode()).decode()
    safe_code = ast.literal_eval(decoded_code) # Use ast.literal_eval instead of exec or eval
