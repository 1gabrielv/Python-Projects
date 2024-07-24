import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def password_generator(length):
    password = ""

    for digit in range(length):
        type = random.randint(1,2)
        if(type == 1):
            password += random.choice(numbers)
        else:
            password += random.choice(letters).upper()
    return password


def email_generator(name):
    email_name = name.split()
    email_name = [word.capitalize() for word in email_name]

    email = ""
    email = ''.join(email_name)
    for number in range(3):
        email += random.choice(numbers)
    
    email += "@gmail.com"
    return email


name = input("type your name: \n")
length = int(input("enter the length of your password: \n"))

password = password_generator(length)
email = email_generator(name)

print(f"Your new email: {email} \nYour new password: {password}")
