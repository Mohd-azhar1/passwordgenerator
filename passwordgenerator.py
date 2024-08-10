print("**********PASSWORD GENERATOR*************")
import random
import string

def password_generator(leng):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if (leng< 8):
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(leng))
    return password

leng = int(input("Enter the desired length of the password: "))
password = password_generator(leng)
if password:
    print("Generated Password : ", password)