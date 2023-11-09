import argparse
import textwrap
import os

def validate_file_existence(file_path, file_description):
    """
    Validate the existence of a file in the file system.

    Args:
        file_path (str): Path to the file to validate.
        file_description (str): Description of the file.

    Raises:
        argparse.ArgumentTypeError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise argparse.ArgumentTypeError(f"{file_description} '{file_path}' does not exist.")

def check_args(parser, args):
    """
    Check command-line arguments for validity and mutual exclusivity.

    Args:
        parser (argparse.ArgumentParser): The argument parser.
        args (argparse.Namespace): Parsed command-line arguments.

    Raises:
        argparse.ArgumentError: If there are issues with the arguments.
    """
    if not args.encrypt and not args.decrypt:
        parser.error("You must specify either '-e' for encryption or '-d' for decryption. Choose one.")
    if not args.key:
        parser.error("You must specify your secret key with '-k'.")
    if not args.input:
        parser.error("You must specify '-i' for the input file.")
    if args.decrypt and args.encrypt:
        parser.error("You must specify either '-e' for encryption or '-d' for decryption. Only one of them.")

def args_handler():
    """
    Parse command-line arguments for the SecurePyVault script.
    Returns:
        tuple: A tuple containing the validated encryption key, input file, and output file.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        SecurePyVault: A secure file encryptor/decryptor.

        Usage examples:
        1. To encrypt a file with a specific key:
            Run: python spv.py -e -k my_secret_key -i input.txt -o encrypted.txt

        2. To decrypt a file with the same key:
            Run: python spv.py -d -k my_secret_key -i encrypted.txt -o decrypted.txt

        WARNING: If you do not specify an output file with '-o', the input file will be encrypted/decrypted in place, overwriting its content. 
        Use this option with caution to avoid data loss.
        ''')
    )

    # Required argument to specify encryption or decryption
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt a file')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt a file')

    # Required argument for the encryption key
    parser.add_argument('-k', '--key', type=str, required=True, help='Encryption key')

    # Required argument for the input file
    parser.add_argument('-i', '--input', type=str, required=True, help='Input file to encrypt/decrypt')

    # Optional argument for the output file
    parser.add_argument('-o', '--output', type=str, help='Output file after encryption/decryption')

    args = parser.parse_args()

    # Check the validity of the command-line arguments
    check_args(parser, args)

    # If the output file is not provided, set it to the same as the input file
    if args.output is None:
        args.output = args.input

    # Validate that the input file exists
    validate_file_existence(args.input, "Input file")

    return args.encrypt, args.decrypt, args.key, args.input, args.output
