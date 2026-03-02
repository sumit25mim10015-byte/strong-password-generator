import string
import secrets

length = int(input("Enter the length of password: "))

if length < 4:
    print("Password length should be at least 4")
else:
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure at least one of each
    password = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    
    all_characters = letters + digits + symbols
    
    for i in range(length - 3):
        password.append(secrets.choice(all_characters))
    
    secrets.SystemRandom().shuffle(password)
    
    print("Generated Password:", "".join(password))