import string

common_passwords = [
    "password", "123456", "123456789", "qwerty",
    "admin", "welcome", "abc123", "letmein"
]

password = input("Enter your password: ")

score = 0
feedback = []

# Length
if len(password) >= 12:
    score += 30
elif len(password) >= 8:
    score += 20
else:
    feedback.append("Make your password at least 8 characters long.")

# Uppercase
if any(c.isupper() for c in password):
    score += 15
else:
    feedback.append("Add an uppercase letter.")

# Lowercase
if any(c.islower() for c in password):
    score += 15
else:
    feedback.append("Add a lowercase letter.")

# Numbers
if any(c.isdigit() for c in password):
    score += 20
else:
    feedback.append("Add a number.")

# Special characters
if any(c in string.punctuation for c in password):
    score += 20
else:
    feedback.append("Add a special character (!, @, #, etc.).")

# Common password check
if password.lower() in common_passwords:
    score = 0
    feedback = ["This is a very common password. Choose a unique one."]

# Strength Rating
if score >= 90:
    strength = "Very Strong 💪"
elif score >= 70:
    strength = "Strong 👍"
elif score >= 50:
    strength = "Medium 🙂"
elif score >= 30:
    strength = "Weak ⚠️"
else:
    strength = "Very Weak ❌"

print("\n----- Password Report -----")
print(f"Password Length : {len(password)}")
print(f"Score           : {score}/100")
print(f"Strength        : {strength}")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print(f"- {item}")
else:
    print("\nGreat! Your password follows all recommended rules.")
