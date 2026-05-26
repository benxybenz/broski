def exit():
     print("That is all the tasks for today thankyou ")
     print(f"Have a great day {name}")
     

def task_remover(choice):
     task_to_remove = input("Enter the task you want to remove = ")
     a.remove(task_to_remove)
     task_restarter(choice)    


def task_view(choice):
    print("The task are as follows : ")
    count = 1
    for i in a:
        print(f"{count}.",i)
        count=count+1
    task_restarter(choice)
    exit()

     
def task_restarter(choice):
     menu(tasks)
     choice = input("Enter your choice again = ")
     task_identifier(choice)


def task_add(choice):
    count = "Yes"
    task_no = 1
    while count != "No":
            m = input(f"{task_no}. Enter task = ")
            task_no = task_no+1
            a.append(m)
            count = input("Do you want to continue(Yes/No) = ").capitalize()
    if count == "No":
         task_restarter(choice)


def task_identifier(choice):
    if choice == "add":
         task_add(choice)
    elif choice == "view":
         task_view(choice)
    elif choice == "remove":
         task_remover(choice)
    else :
         exit()
    
 
def menu(tasks):
    print(tasks [0])
    print(tasks [1])
    print(tasks [2])
    print(tasks [3])


a = []
tasks = ['1) add', '2) view' , '3) remove', '4) exit']
name = input("Enter name = ").capitalize()
print(f"Hello {name}")
print("Menu :")
menu(tasks)
choice = input("Enter your choice = ").lower()
task_identifier(choice)