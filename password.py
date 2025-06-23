import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected. Cannot generate password."

    # For debugging
    print("DEBUG: Using characters:", characters)

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")

    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
        use_digits = input("Include DIGITS? (y/n): ").lower() == 'y'
        use_symbols = input("Include SYMBOLS? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_symbols)
        print("\n🔑 Generated Password:", password)

    except ValueError:
        print("Invalid input! Please enter a valid number for password length.")

main()
