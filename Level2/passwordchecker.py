import re

def passwordvalidator(password):
    errors = []
    strength = 0
    
    if not len(password) >= 8:
        errors.append("Password must be at least 8 characters long.")
    else:
        strength += 1

    if not re.search("[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
    else:
        strength += 1

    if not re.search("[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")
    else:
        strength += 1

    if not re.search("[0-9]", password):
        errors.append("Password must contain at least one digit.")
    else:
        strength += 1

    if not re.search("[^A-Za-z0-9]", password):
        errors.append("Password must contain at least one special character.")
    else:
        strength += 1

    return errors, strength

password = input("Enter the password to check: ")
errors, strength = passwordvalidator(password)

if strength == 5:
    print("It is a very strong password.")
elif strength == 4:
    print("It is a strong password.")
elif strength == 3:
    print("It is a normal password.")
elif strength == 2:
    print("It is a weak password.")
elif strength == 1:
    print("It is a very weak password.")
else:
    print("It is not a valid password at all.")

if strength < 5:
    print("\nYour password lacks the following criteria:")
    for error in errors:
        print(f" - {error}")
