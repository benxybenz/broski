def outro():
    print("Thanks for shopping ")
    x = len(cart)
    print(f"Total no. of items = {x}")



def item_remover():
    item_to_be_removed = input("Enter the item that you want removed = ")
    cart.remove(item_to_be_removed)
    menu()
    task_restarter(task)


def view_cart():
    print("your cart looks like :")
    count = 1
    for i in cart:
        print(f"{count}.",i)
        count = count+1
    print("Anything else: ")
    print("\n")
    menu()
    task_restarter(task)

    


def task_restarter(task):
    task = input("Enter you choice again =  ")
    task_identifier(task)



def task_identifier(task):
    if task == "add":
        add_items()
    elif task == "view":
        view_cart()
    elif task == "remove":
        item_remover()
    else:
        outro()
    




def add_items():
    count = 1
    choice = "Yes"
    while choice != "No":
        x = input(f"{count}. Enter your item = ")
        count = count + 1 
        cart.append(x)
        choice = input("Do you want more items (Yes/No) = ").capitalize()
        if choice == "No":
            print("Any more sir ? ")
            menu()
            task_restarter(task)







def menu():
    table = ["1) Add items", "2) Remove items ", "3) View items ", "4) Exit"]
    print(table[0])
    print(table[1])
    print(table[2])
    print(table[3])
    
    


cart = []
name = input("Enter name = ")
print(f"Hello {name} here is your cart enjoy shopping ")
menu()
task = input("Enter your choice = ").lower()
task_identifier(task)

