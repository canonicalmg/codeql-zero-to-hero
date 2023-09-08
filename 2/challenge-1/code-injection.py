```python
from flask import Flask, request
import ast
import base64

app = Flask(__name__)

@app.route("/code-execution")
def code_execution():
    code = request.args.get("code")
    sanitized_code = base64.b64decode(code).decode('utf-8')
    parsed_code = ast.literal_eval(sanitized_code)
    # Perform necessary actions with parsed_code
```