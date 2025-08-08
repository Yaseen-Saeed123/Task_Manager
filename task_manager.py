import task_manager_functions as tm

# Make an intro
print("="*30)
print("Senson Mo task manager")
print("="*30)

# Make a message
message = " 1- Add Task to task list \n \
2- Mark tasks as complete \n \
3- View tasks \n \
4- Clear tasks \n \
5- Quit"

# Main while loop of the program
while True:
    print(message)
    print("-"*30)
    action = input("What do you want to do? ").lower().strip()
    if action in ['1', 'add tasks to task list']:
        tm.add_tasks()
    elif action in ['2', 'mark tasks as complete']:
        tm.mark_tasks()
    elif action in ['3', 'view tasks']:
        tm.view_tasks()
    elif action in ['4', 'clear tasks']:
        tm.clear_tasks()
    elif action in ['5', 'quit']:
        break
    else:
        print("-"*30)
        print("Invalid input! Enter a number from 1 to 5")
        print("-"*30)