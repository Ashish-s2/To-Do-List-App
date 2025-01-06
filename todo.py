# This is a simple Python to-do list app

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    show_tasks()
    if tasks:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
