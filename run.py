import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password)
    uppercase_criteria = re.search(r'[A-Z]', password)
    digit_criteria = re.search(r'\d', password)
    special_char_criteria = re.search(r'[@$!%*?&]', password)
    
    # Check all criteria
    if length_criteria and lowercase_criteria and uppercase_criteria and digit_criteria and special_char_criteria:
        return "Strong"
    elif length_criteria and (lowercase_criteria or uppercase_criteria) and digit_criteria:
        return "Medium"
    else:
        return "Weak"

# Example usage
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"The password strength is: {strength}")
