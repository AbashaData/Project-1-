import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    """
    Generate a random password.

    :param length: Length of the password
    :param use_uppercase: Include uppercase letters
    :param use_numbers: Include numbers
    :param use_special: Include special characters
    :return: Randomly generated password
    """
    characters = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("No character sets selected for password generation.")

    # Generate a password by randomly sampling characters
    password = ''.join(random.choices(characters, k=length))
    return password

# User Interaction
def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length (e.g., 12): "))
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"\nYour generated password is: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

