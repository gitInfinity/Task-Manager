# Task Manager

A simple command-line task management application that helps you organize and track your daily tasks.

## Features

- **Add Tasks**: Create new tasks and add them to your task list
- **View Tasks**: Display all your tasks with their current status
- **Mark Completed**: Update task status to completed
- **Clear All**: Remove all tasks at once
- **Persistent Storage**: Tasks are saved to a JSON file for data persistence

## Requirements

- Python 3.12 or higher
- No external dependencies

## Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd task-manager
   ```

## Usage

Run the application:

```bash
uv run main.py
```

Or with standard Python:

```bash
python main.py
```

### Menu Options

When the application starts, you'll see the following menu:

```
Task Manager
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Clear All Tasks
5. Exit
```

**Option 1**: Add a new task by entering its name  
**Option 2**: View all your current tasks with their status  
**Option 3**: Mark a task as completed by entering its name  
**Option 4**: Delete all tasks from your list  
**Option 5**: Exit the application  

## Task Status

Each task has a status that can be:
- `in-progress`: Task is currently being worked on
- `Completed`: Task has been finished
- `Delayed`: Task has been delayed

## Data Storage

Tasks are stored in `tasks.json` in the following format:

```json
[
    {
        "name": "Buy groceries",
        "status": "in-progress"
    },
    {
        "name": "Clean the house",
        "status": "Completed"
    }
]
```

## Project Structure

```
task-manager/
├── main.py          # CLI entry point
├── Task.py          # Core task management logic
├── tasks.json       # Task data storage
├── pyproject.toml   # Project configuration
└── README.md        # This file
```

## License

This is an open project. Feel free to use and modify as needed.
