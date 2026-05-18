import random
import string
num = int(input("Enter pair of password = "))
for i in range(num):
    x = str(random.randrange(0,10))
    y = random.choice(string.ascii_letters)
    z = x+y
    print(z, end="")    