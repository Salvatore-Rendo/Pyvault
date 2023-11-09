import os
from cryptography.fernet import Fernet

# Function to encrypt a file
def encrypt_file(key, input_file, output_file):
    # Read the data from the input file
    with open(input_file, 'rb') as file:
        data = file.read()
    
    # Create a Fernet object with the provided key
    fernet = Fernet(key)
    
    # Encrypt the data
    encrypted_data = fernet.encrypt(data)

    # Write the encrypted data to the output file
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
