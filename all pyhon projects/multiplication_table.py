print("This is a multiplication table generator ")
num = int(input("Enter a number = "))
x = int(input("Enter range = "))
print(f"The multiplication table of {num} is as follows ")
for i in range(1,x+1):
    print(f"{num} X {i} = ", num*i)

    