#!/bin/bash

# Run pw generator
python3 ./pwGen.py

# Function to encrypt a string using ROT13
encrypt_rot13() {
    echo "$1" | tr 'a-zA-Z' 'n-za-mN-ZA-M'
}

# Check if the file exists
if [ -f "generated_password.txt" ]; then
    # Read the password from the file
    password=$(cat generated_password.txt)
    
    # Encrypt the password using ROT13
    encrypted_password=$(encrypt_rot13 "$password")

    # Save the encrypted password to a new file
    echo "$encrypted_password" > encrypted_password.txt

    rm generated_password.txt

    echo "Password encrypted successfully."
else
    echo "generated_password.txt not found. Please generate a password first."
fi

