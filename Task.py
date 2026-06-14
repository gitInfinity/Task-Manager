import json
from pathlib import Path

class Task:
    def __init__(self, filename = "tasks.json"):
        """Initialize the Task class with a filename for storing tasks."""
        self.filename = filename
        filepath = Path(self.filename)
        if not filepath.exists():
            print(f"Creating new task file: {self.filename}")
            filepath.touch()
        self.file = filepath

    
    def addTask(self, name):
        """Add a task to the task file. If task already exists, it is not added again."""
        print(f"Adding task: {name} to {self.filename}")
        new_task = {
                    "name": name,
                    "status": "in-progress"
                }
        if self.file.stat().st_size == 0:
            with open(self.filename, 'w') as file:
                json.dump([new_task], file, indent=4)
            file.close()
            
        with open(self.filename, 'r') as file:
            tasks = json.load(file)
        
        # Check if task already exists
        for task in tasks:
            if task['name'] == name:
                print(f"Task '{name}' already exists.")
                file.close()
                return

        tasks.append(new_task)
        
        with open(self.filename, 'w') as file:
            json.dump(tasks, file, indent=4)
            
        file.close()
        
    def getTasks(self, name=None):
        """Retrieve all tasks from the task file, unless a specific task is provided."""
        if self.file.stat().st_size == 0:
            print(f"No tasks found in {self.filename}")
            return
        with open(self.filename, 'r') as file:
            tasks = json.load(file)
        
        if name is None:
            file.close()
            return tasks
        else:
            for task in tasks:
                if task['name'] == name:
                    file.close()
                    return task
            file.close()
            return None
        
    def taskCompleted(self, task_name):
        """Mark a specific task as complete."""
        if self.file.stat().st_size == 0:
            print(f"No tasks found in {self.filename}")
            return
        with open(self.filename, 'r') as file:
            tasks = json.load(file)
        
        for task in tasks:
            if task['name'].lower() == task_name.lower():
                task['status'] = "Completed"
                break
        
        with open(self.filename, 'w') as file:
            json.dump(tasks, file, indent=4)
        
        file.close()
        
    def delayTask(self, task_name):
        """Mark a specific task as delayed."""
        if self.file.stat().st_size == 0:
            print(f"No tasks found in {self.filename}")
            return
        with open(self.filename, 'r') as file:
            tasks = json.load(file)
        
        for task in tasks:
            if task['name'].lower() == task_name.lower():
                task['status'] = "Delayed"
                break
        
        with open(self.filename, 'w') as file:
            json.dump(tasks, file, indent=4)
        
        file.close()
    
    def deleteTask(self, task_name):
        """Delete a specific task from the task file."""
        if self.file.stat().st_size == 0:
            print(f"No tasks found in {self.filename}")
            return
        with open(self.filename, 'r') as file:
            tasks = json.load(file)
        
        tasks = [task for task in tasks if task['name'].lower() != task_name.lower()]
        
        with open(self.filename, 'w') as file:
            json.dump(tasks, file, indent=4)
        
        file.close()
    
    def clearTasks(self):
        """Clear all tasks from the task file."""
        with open(self.filename, 'w') as file:
            json.dump([], file, indent=4)
        
        file.close()
        
        