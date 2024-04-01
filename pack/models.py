# Check the user input for SQL injection and XSS attacks
def check_query(data):
    error = None
    if any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in data):
        error = "Invalid Input"
    elif any(char.isspace() for char in data):
        error = "Invalid Input"
    elif len(data) > 20:
        error = "Invalid Input"
    elif len(data) < 10:
        error = "Invalid Input"
    return error

# Check the user input for SQL injection and XSS attacks
def check_pass(key):
    error = None
    if len(key) > 4:
        error = "Invalid Key"
    elif len(key) < 3:
        error = "Invalid Key"
    elif any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in key):
        error = "Invalid Key"
    elif any(char.isspace() for char in key):
        error = "Invalid Key"
    return error

