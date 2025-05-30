
# To-Do List CLI Application

A simple command-line interface (CLI) to-do list manager built in Python. This application allows you to manage your tasks with various status levels and provides persistent storage.

## Features

- **View Tasks**: Display all tasks, completed tasks, or incomplete tasks
- **Add Tasks**: Create new tasks with custom status levels
- **Edit Tasks**: Modify existing task names and statuses
- **Delete Tasks**: Remove tasks from your list
- **Mark Complete**: Change task status to "Done"
- **Persistent Storage**: Tasks are automatically saved to a file
- **Status Categories**: Organize tasks by urgency (urgent, semi-urgent, non-urgent)

## Installation

No additional dependencies required - uses Python standard library only.

## Usage

Run the application:
```bash
python CLI_VERSION/main.py
```

### Menu Options

1. **View To-Do List** - Display all tasks with their current status
2. **View Incompleted Tasks** - Show only tasks that are not marked as "Done"
3. **View Completed Tasks** - Show only tasks marked as "Done"
4. **Add Task** - Create a new task with custom name and status
5. **Edit Task** - Modify an existing task's name or status
6. **Delete Task** - Remove a task from the list
7. **Mark Task as Complete** - Change a task's status to "Done"
8. **Save and Quit** - Exit the application and save all changes

### Task Status Options

- **urgent** - High priority tasks
- **semi-urgent** - Medium priority tasks  
- **non-urgent** - Low priority tasks
- **Done** - Completed tasks

## File Structure

```
CLI_VERSION/
├── main.py     # Main application file
├── tasks.txt   # JSON file storing all tasks (auto-generated)
└── README.md   # This documentation
```

## Data Storage

Tasks are stored in `CLI_VERSION/tasks.txt` as JSON format. Each task contains:
- `task`: The task description
- `status`: The current status of the task

Example task structure:
```json
[
  {
    "task": "Complete project documentation",
    "status": "urgent"
  },
  {
    "task": "Review code",
    "status": "Done"
  }
]
```

## Example Usage

1. Start the application
2. Select option 4 to add a new task
3. Enter task description: "Buy groceries"
4. Enter status: "urgent"
5. View your tasks with option 1
6. Mark tasks complete with option 7
7. Save and exit with option 8

## Notes

- The application will create the `tasks.txt` file automatically if it doesn't exist
- All changes are saved automatically when you modify tasks
- Invalid menu choices will prompt you to try again
- Task numbers are displayed starting from 1 for user convenience
