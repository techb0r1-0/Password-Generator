import secrets
import string
import random

# The libraries required are: 'secrets', for generating secure random values
# 'string', for providing a set of the digits, letters, and symbols

def generate_password(): 
    length = 60 # Sets a length for how long the password should be
    password = list(''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase) for _ in range(length))) # Generates a string of random letters based on the rules it was given above and assigns it to the 'password' variable
    random.shuffle(password)
    shuffled_password = ''.join(password)
    return shuffled_password # Returns the generated password

'''
# Do not change the code below
'''
# Generate a password that meets the criteria
password = generate_password()
print(password)
