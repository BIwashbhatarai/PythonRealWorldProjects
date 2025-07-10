import re  # Regular expression module for pattern matching

# Function to validate email using custom rules + regex
def strongEmailValidation(Email):
    # Regex pattern for a valid email format
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # Rule 1: Minimum length check
    if len(Email) < 6:
        return False, "Email length too short"
    
    # Rule 2: First character must be a letter
    if not Email[0].isalpha():
        return False, "Email must start with a letter"
    
    # Rule 3: No spaces allowed in the email
    if " " in Email:
        return False, "Email must not contain space"
    
    # Rule 4: Pattern match using regex
    if re.match(pattern, Email):
        return True, "Email is valid"
    else:
        return False, "Email is not valid"

# ---- Program Execution Starts Here ----

# Take user input for email
Email_input = input("Enter an Email: ")

# Call the validation function and store result
valid, message = strongEmailValidation(Email_input)

# Print the result message
print(message)
