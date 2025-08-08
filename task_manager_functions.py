import ast

def add_tasks():
    while True:
        # Get task from user
        print("-"*30)
        task = input("Add a task: ").title().strip()
        print("-"*30)

        # Create a dictionary that holds data about the task
        task_info = {"task":task, "is_completed":False}

        # Check if this data has been already in the file or not
        with open("Task_manager/tasks.txt", 'r') as file:
            found = False
            for line in file:
                if ast.literal_eval(line.strip()) == task_info:
                    found =True
        
        # Write this data into the tasks.txt file
        with open("Task_manager/tasks.txt", 'a') as file:
            if not found:    
                file.write(f"{task_info}\n")
                # write a message to the user
                print("Task added successfully!!!")
                print("-"*30)
            elif found:
                print("Task already added")
                print("-"*30)
                pass
        
        # Asking if the user wants to add another task
        while True:
            again = input("Do you want to add another task?[y/n] ").strip().lower()
            if again in ['y','n','yes','no']:
                break
            else:
                print("-"*30)
                print("Invalid input")
                print("-"*30)

        if again in ['n','no']:
            print("-"*30)
            return

def mark_tasks():
    while True:
        # Make a list of incomplete tasks and complete tasks
        incomplete_tasks = []
        complete_tasks = []
        
        # Separate tasks into incomplete and complete tasks
        with open("Task_manager/tasks.txt", 'r') as file:
            for line in file:
                    task = ast.literal_eval(line.strip())
                    if task["is_completed"] == False:
                        incomplete_tasks.append(task)
                    else:
                        complete_tasks.append(task)
        
        # Return complete tasks to the file
        with open("Task_manager/tasks.txt",'w') as file:
            for task in complete_tasks:
                file.write(f"{task}" + "\n")
        
        # Check if there are incomplete tasks
        if not incomplete_tasks: 
            print("-"*30)
            print("No tasks to be marked as complete")
            print("-"*30) 
            return
        # order these tasks
        print("-"*30)
        for i, task in enumerate(incomplete_tasks):
            print(f"{i+1}- {task["task"]}")
            print("."*30)
        
        # Get task number from user
        try:
            choice = int(input("Choose task to be marked as complete: "))
            print("-"*30)
            if choice < 1 or choice > len(incomplete_tasks):
                print("Invalid Task number")
                print("-"*30)
                with open("Task_manager/tasks.txt", 'a') as file:
                    for task in incomplete_tasks:
                        file.write(f"{task}" + "\n")
            
            # Mark task as complete
            else:
                incomplete_tasks[choice-1]["is_completed"] = True
                # Implementeng the new list into the file
                with open("Task_manager/tasks.txt", 'a') as file:
                    for task in incomplete_tasks:
                        file.write(f"{task}" + "\n")
                print("Task marked successfully!!")
                print("-"*30)
        except ValueError:
            print("-"*30)
            print("Not a task number, Please enter a number")
            print("-"*30)
            with open("E:/Youtube Channel material/Python projects/Task_manager/tasks.txtt", 'a') as file:
                for task in incomplete_tasks:
                    file.write(f"{task}" + "\n")

        # Check if user wants to mark another task
        while True:
            again = input("Do you want to mark another task?[y/n] ").strip().lower()
            if again in ['y','n','yes','no']:
                break
            else:
                print("-"*30)
                print("Invalid input")
                print("-"*30)

        if again in ['n','no']:
            print("-"*30)
            return
             
def view_tasks():
    with open("Task_manager/tasks.txt", 'r') as file:
        tasks = []
        statuses = []
        for line in file:
            task = ast.literal_eval(line.strip())
            tasks.append(task)
            # Determine completeness status
            status = "✅" if task["is_completed"] else "❌" 
            # Append new status
            statuses.append(status)
    
    # Print tasks with their new statuses
    print("-"*30)
    for i, task in enumerate(tasks):
        print(f"{i+1}- {task["task"]} {statuses[i]}")
        print("."*30)

def clear_tasks():
    print("-"*30)
    again = ""
    while again not in ["y","n","yes","no"]:
        again = input("Are you sure you want to clear all the tasks?[y/n] ").strip().lower()
        print("-"*30)
    if again in ['y','yes']:
        print("Tasks cleared successfully")
        print("-"*30)
        open("Task_manager/tasks.txt", 'w').close()
    else:
        return