It seems like you are facing a command injection vulnerability due to the use of user-provided input in your code. To help you fix this issue, I would need to see the actual code in the "command-injection.py" file. However, I can provide you with a general solution to prevent command injection.

You can use the `subprocess` module to safely execute shell commands with user-provided input. Here's an example of how to use the `subprocess` module to prevent command injection:

```python
import subprocess

# Get user input
user_input = input("Please enter a value: ")

# Safely execute the command with user-provided input
result = subprocess.run(["your_command", user_input], capture_output=True, text=True)

# Print the output
print(result.stdout)
```

Replace "your_command" with the actual command you want to execute. This will safely pass the user-provided input as an argument to the command without allowing command injection.

Please provide the actual code if you need more specific help.