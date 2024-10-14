import json
import os

TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(title, description):
    tasks = load_tasks()
    task = {'title': title, 'description': description, 'completed': False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added.")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{i}. {task['title']} - {status}\n   {task['description']}")
    else:
        print("No tasks available.")

# Mark a task as complete
def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Invalid task number.")

# Main menu
def main_menu():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task Title: ")
            description = input("Task Description: ")
            add_task(title, description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            list_tasks()
            task_number = int(input("Enter task number to mark as complete: "))
            complete_task(task_number)
        elif choice == '4':
            list_tasks()
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()