name = input("Enter name = ")
roll = int(input("Enter roll = "))
physics = int(input("Enter you physics marks = "))
chem = int(input("Enter your chem marks = "))
maths = int(input("Enter your maths marks = "))
total = physics+chem+maths
avg = total/3
print("Hello " + name)
print("Your results are as follows:")
print("your roll no = ",roll)
print("physics marks = ",physics)
print("Chem marks = ",chem)
print("Maths marks = ",maths)
print("Total marks = ",total)
print("Average marks = ",avg)
if physics>=30 and chem>=30 and maths>=30 :
    print(name + "You Have Passed ")
else:
    print(name + "You have failed ")