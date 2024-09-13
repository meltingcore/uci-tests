"""
A simple Python script that demonstrates basic functionality with added
complexity so that it can be checked with pylint and bandit.
"""

def print_message(message: str) -> None:
    """
    Prints a message to the console.

    Args:
        message (str): The message to print.
    """
    if not isinstance(message, str):
        raise ValueError("The message must be a string.")
    print(message)


def main() -> None:
    """
    Main function to execute the script.
    """
    try:
        message = "Hello, World!"
        print_message(message)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()