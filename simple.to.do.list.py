tasks = []

def display_menu():
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Quit Task")

def add_task():
    task = input("Enter a task: ").strip()
    if task: #Ensures task is not empty
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Invalid input. Task cannot be empty.")
    print("Current task:", tasks)
    

def view_task():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    
    view_task()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task}' deleted successfulyy!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():

    while True:
        display_menu()
        choice = input("what would you like to do?: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("invalid choice. Please try again.")

main()
