import os
from cryptography.fernet import Fernet

# Function to decrypt a file
def decrypt_file(key, input_file, output_file):
    # Read the data from the input file
    with open(input_file, 'rb') as file:
        data = file.read()
    
    # Create a Fernet object with the provided key
    fernet = Fernet(key)
    
    # Decrypt the data
    decrypted_data = fernet.decrypt(data)

    # Write the decrypted data to the output file
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
