import os
import base64
from securepyvault.handler import args_handler
from securepyvault.encryptor import encrypt_file
from securepyvault.decryptor import decrypt_file

# Define a constant salt value 
SALT = b'th1s_1s_4_c0stAnt_sAlt_v4lu3'

# Function to combine the password and salt
def combine_password_and_salt(password):
    return password.encode() + SALT

# Define the main function
def main():
    # Parse command-line arguments using the args_handler function
    encrypt, decrypt, password, input_file, output_file = args_handler()

    if password:
        # Combine the password and the constant salt
        salted_password = combine_password_and_salt(password)

        # Hash the salted password to generate an encryption key
        key = base64.urlsafe_b64encode(salted_password)

    # Perform encryption or decryption based on user's choice
    if encrypt:
        encrypt_file(key, input_file, output_file)
        print("File encrypted successfully.")
    elif decrypt:
        decrypt_file(key, input_file, output_file)
        print("File decrypted successfully.")

# Entry point of the script
if __name__ == "__main__":
    main()
