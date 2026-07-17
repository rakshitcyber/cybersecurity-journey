import random
import string

print("===== Secure Password Generator =====")

# Ask for password length
length = int(input("Enter password length (minimum 8): "))

# Check minimum length
if length < 8:
    print("Password length must be at least 8.")
else:
    # Ask how many passwords to generate
    count = int(input("How many passwords do you want? "))

    # Ask whether to include special characters
    choice = input("Include special characters? (y/n): ").lower()

    # Choose character set
    if choice == "y":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    print("\nGenerated Password(s):\n")

    # Generate passwords
    for i in range(count):
        password = ""

        for j in range(length):
            password += random.choice(characters)

        print(f"Password {i+1}: {password}")
