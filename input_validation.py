# Function to Validate inputs that need to be Positive Integers
def validate_positive_int(value, field_name):
    try:
        int_value = int(value)
        if int_value <= 0:
            raise ValueError
        return int_value
    except ValueError:
        print(f"{field_name} must be a positive integer.")
        return None

# Function to Validate inputs that cannot be Empty
def validate_non_empty_string(value, field_name):
    if not value.strip():
        print(f"{field_name} cannot be empty.")
        return None
    return value.strip()

# Function to Confirm action choice
def confirm_action(message):
    while True:
        confirmation = input(f"{message} (Y/N): ").strip().lower()
        if confirmation in ["y", "n"]:
            return confirmation == "y"
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")