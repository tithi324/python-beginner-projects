# user input pwd length 
# generate password of the same length 

import random
l = int(input("Enter length of your password: "))

my_list = []
for i in range (l):
    pwdletter = chr(random.randint(33,126))
    my_list.append(pwdletter)

pwd = ''.join(my_list)
print(pwd)
