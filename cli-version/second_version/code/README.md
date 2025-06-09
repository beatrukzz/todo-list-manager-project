
# To-Do List CLI Application v2.0

An enhanced command-line interface (CLI) to-do list manager built in Python with advanced features for task management, due date tracking, and comprehensive organization capabilities.

## What's New in Version 2.0

### Major New Features
- **Due Date Management**: Set and track due dates for tasks (DD-MM-YYYY format)
- **Overdue Detection**: Automatic detection and highlighting of overdue tasks
- **Task Archiving**: Completed tasks are automatically archived with completion dates
- **Advanced Statistics**: Comprehensive task analytics and completion tracking
- **Smart Task Sorting**: Tasks automatically sorted by due date and urgency
- **Search Functionality**: Find tasks quickly with keyword search
- **Color-Coded Interface**: Visual status indicators with ANSI color coding

### Enhanced Features
- **Improved Data Storage**: Separate files for active and completed tasks
- **Better Error Handling**: More robust input validation and error messages
- **Enhanced Display**: Clear visual indicators for overdue and urgent tasks
- **Automatic Archiving**: Completed tasks are moved to archive with timestamps

## Features

### Core Functionality
- **View Tasks**: Display all tasks, completed tasks, or incomplete tasks with color coding
- **Add Tasks**: Create new tasks with custom status levels and due dates
- **Edit Tasks**: Modify existing task names, statuses, and due dates
- **Delete Tasks**: Remove tasks from your list with confirmation
- **Mark Complete**: Change task status to "Done" and automatically archive
- **Search Tasks**: Find tasks by keyword search
- **Task Statistics**: View comprehensive analytics about your productivity

### Advanced Features
- **Due Date Tracking**: Set optional due dates for better time management
- **Overdue Alerts**: Visual warnings for tasks past their due date
- **Smart Sorting**: Tasks automatically organized by due date and urgency
- **Task Archiving**: Historical record of completed tasks with completion dates
- **Color-Coded Status**: Visual status indicators for quick recognition
- **Persistent Storage**: Automatic saving with separate active and archive files

## Installation

No additional dependencies required - uses Python standard library only.

## Usage

Run the application:
```bash
python CLI_VERSION/main.py
```

### Menu Options

1. **View To-Do List** - Display all tasks with color-coded status and overdue indicators
2. **View Incompleted Tasks** - Show only active/pending tasks
3. **View Completed Tasks** - Show archived completed tasks with completion dates
4. **Add Task** - Create a new task with name, status, and optional due date
5. **Edit Task** - Modify an existing task's details
6. **Delete Task** - Remove a task from the list
7. **Mark Task as Complete** - Complete a task and move it to archive
8. **Search Tasks** - Find tasks by keyword
9. **Show Statistics** - View detailed task analytics
10. **Save and Quit** - Exit the application and save all changes

### Task Status Options

- **urgent** - High priority tasks
- **semi-urgent** - Medium priority tasks
- **non-urgent** - Low priority tasks
- **Done** - Completed tasks

### Due Date Format

Enter dates in DD-MM-YYYY format (e.g., 25-12-2024) or press Enter for no due date.

## File Structure

```
CLI_VERSION/
├── main.py              # Main application file
├── tasks.txt           # Active tasks storage
├── completed_tasks.txt # Archived completed tasks
└── README.md           # This documentation
```

## Data Storage

### Active Tasks (`tasks.txt`)
Tasks are stored in pipe-separated format:
```
task_name | status | due_date
```

### Completed Tasks (`completed_tasks.txt`)
Archived tasks include completion date:
```
task_name | status | due_date | completion_date
```

## Color Coding

- <span style="color: red;">**Red**: Urgent tasks</span>
- <span style="color: gold;">**Yellow**: Semi-urgent tasks</span>
- <span style="color: green;">**Green**: Non-urgent tasks</span>
- <span style="color: blue;">**Blue**: Completed tasks</span>
- <span style="color: magenta; font-weight: bold;">**Magenta**: Overdue tasks (bold)</span>

## Example Usage

1. Start the application
2. Select option 4 to add a new task
3. Enter task description: "Submit project report"
4. Enter status: "urgent"
5. Enter due date: "15-01-2025"
6. View your tasks with option 1 (sorted by due date)
7. Use option 9 to check statistics
8. Mark tasks complete with option 7 (automatically archived)
9. Save and exit with option 10

## Statistics Features

The statistics panel shows:
- Active tasks count
- Completed (archived) tasks count
- Total all-time tasks
- Current urgent tasks
- Overdue tasks count
- All-time completion rate percentage

## Notes

- The application automatically creates necessary files if they don't exist
- All changes are saved automatically when you modify tasks
- Completed tasks are automatically moved to the archive
- Tasks are automatically sorted by due date and then by urgency
- Overdue tasks are highlighted in magenta with [OVERDUE] indicator
- Invalid menu choices and dates will prompt you to try again
- Task numbers are displayed starting from 1 for user convenience

## Version History

- **v1.0**: Basic task management with JSON storage
- **v2.0**: Enhanced with due dates, archiving, statistics, search, and color coding

---

*Built with Python standard library - no external dependencies required*
