# todo.py
 
# Initialize an empty list to store tasks
tasks = []
 
def display_tasks():
    """Display the current tasks."""
    if not tasks:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print()
 
def add_task(task):
    """Add a new task."""
    tasks.append(task)
    print(f"Added task: '{task}'")
 
def remove_task(index):
    """Remove a task by its index."""
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Removed task: '{removed_task}'")
    else:
        print("Invalid task number.")
 
def main():
    """Main function to run the To-Do List application."""
    while True:
        print("To-Do List")
        display_tasks()
        print("Options:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
 
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
 
if __name__ == "__main__":
    main()