secret_num = 80
num = int(input("Enter your guess = "))
attempt = 1 
while num != secret_num:
    print(f" {attempt} attempt ")
    if num > secret_num:
        print("your guess was higher")
    elif num < secret_num:
        print("your guess was lower ")
    num = int(input("Try again = "))
    attempt = attempt+1
print(f"Yes your guess {num} was the secret number ")
