import random

pass_length = int(input('Choose length of your new password: '))
password = ""

for i in range(pass_length):

    password += chr(random.randint(33,126))

print(password)