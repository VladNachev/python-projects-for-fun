import random
import string

def generate_password(length):
    # Get a random selection of characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a password with a length of 16 characters
print(generate_password(16))
