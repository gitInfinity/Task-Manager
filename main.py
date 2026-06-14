
from Task import Task

def main():
    task_manager = Task("tasks.json")
    print("\nTask Manager")
    print("1. Add Task - all or specific task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Delay Task")
    print("6. Clear All Tasks")
    print("7. Exit\n")

    while True:
        
        choice = input("Enter your choice: \n")
        
        if choice == '1':
            task_name = input("Enter task name:\n")
            task_manager.addTask(task_name)
            print(f"Task '{task_name}' added.\n")
        
        elif choice == '2':
            tasks = task_manager.getTasks()
            if tasks:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task['name']} - {task['status']}")
            else:
                print("No tasks found.\n")
            print("\n")
        
        elif choice == '3':
            task_name = input("Enter the name of the task to mark as completed: \n")
            task_manager.taskCompleted(task_name)
            print(f"Task '{task_name}' marked as completed.\n")
        
        elif choice == '4':
            task_name = input("Enter the name of the task to delete: \n")
            task_manager.deleteTask(task_name)
            print(f"Task '{task_name}' deleted.\n")
        
        elif choice == '5':
            task_name = input("Enter the name of the task to delay: \n")
            task_manager.delayTask(task_name)
            print(f"Task '{task_name}' marked as delayed.\n")
        
        elif choice == '6':
            task_manager.clearTasks()
            print("All tasks cleared.\n")
        
        elif choice == '7':
            print("Exiting Task Manager.\n")
            break
        
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
