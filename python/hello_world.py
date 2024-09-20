"""
A simple Python script that demonstrates basic functionality with added
complexity so that it can be checked with pylint and bandit.
"""

import os  # Import the os module to introduce a Bandit finding

def print_message(message: str) -> None:
    """
    Prints a message to the console.

    Args:
        message (str): The message to print.
    """
    if not isinstance(message, str):
        raise ValueError("The message must be a string.")
    print(message)

def insecure_function() -> None:
    """
    Executes an insecure operation using os.system which Bandit will flag.
    """
    # Insecure system command execution (Bandit B602 - subprocess injection)
    os.system("ls -l")  # This is potentially insecure

def main() -> None:
    """
    Main function to execute the script.
    """
    try:
        message = "Hello, World!"
        print_message(message)
        insecure_function()  # Call to the insecure function
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()