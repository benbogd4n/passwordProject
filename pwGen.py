import random
import string

# Pw generator function
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generated pw saving function
def save_password_to_file(password):
    with open("generated_password.txt", "w") as file:
        file.write(password)

# User input
length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
use_digits = input("Include digits? (y/n): ").lower() == "y"
use_special_chars = input("Include special characters? (y/n): ").lower() == "y"

# Generate and display the password
password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
print("Generated Password:", password)

# Save the password to a file
save_password_to_file(password)
