import random

pass_length = input('Choose length of your new password: ')
pass_length = int(pass_length)
password = ""

for i in range(pass_length):

    password += chr(random.randint(33,126))

print(password)