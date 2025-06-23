# To-Do List CLI Application v3.0

An advanced command-line interface (CLI) to-do list manager with category management, enhanced organization, and productivity tracking features.

## What's New in Version 3.0

### Major New Features
- **Category Management**: Create, edit, and delete task categories with custom colors
- **Category Filtering**: View tasks filtered by specific categories
- **Enhanced Task Organization**: Tasks grouped by category in all views
- **Visual Category Indicators**: Color-coded category headers for quick recognition
- **Category Statistics**: View task distribution across categories
- **Improved Task Editing**: Edit category assignments for existing tasks
- **Expanded Color System**: More color options for categories and statuses

### Enhanced Features
- **Refined User Interface**: Better organized display with category sections
- **More Robust Data Storage**: Category information stored separately
- **Improved Task Management**: Category assignment during task creation/editing
- **Enhanced Statistics**: Added category-based analytics
- **Better Error Handling**: More validation for category operations

## Features

### Core Functionality
- **View Tasks**: Display all tasks grouped by category with color coding
- **Add Tasks**: Create new tasks with status, due date, and category assignment
- **Edit Tasks**: Modify task details including name, status, due date, and category
- **Delete Tasks**: Remove tasks from your list with confirmation
- **Mark Complete**: Change task status to "Done" and automatically archive
- **Search Tasks**: Find tasks by keyword search
- **Task Statistics**: View comprehensive analytics about your productivity

### Advanced Features
- **Category System**: Organize tasks into custom categories with colors
- **Category Management**: Full CRUD operations for categories
- **Category Filtering**: View tasks by specific categories
- **Due Date Tracking**: Set optional due dates for better time management
- **Overdue Alerts**: Visual warnings for tasks past their due date
- **Smart Sorting**: Tasks automatically organized by due date and urgency
- **Task Archiving**: Historical record of completed tasks with completion dates
- **Color-Coded Interface**: Visual indicators for statuses and categories
- **Persistent Storage**: Automatic saving with separate files for active, completed, and category data

## Installation

No additional dependencies required - uses Python standard library only.

## Usage

Run the application:
```bash

## Menu Options
**View To-Do List** - Display all tasks grouped by category with color coding

**View Incompleted Tasks** - Show only active/pending tasks by category

**View Completed Tasks** - Show archived completed tasks with completion dates

**Add Task** - Create a new task with name, status, due date, and category

**Edit Task** - Modify an existing task's details including category

**Delete Task** - Remove a task from the list

**Mark Task as Complete** - Complete a task and move it to archive

**Search Tasks** - Find tasks by keyword

**Show Statistics** - View detailed task and category analytics

**Manage Categories** - Create, edit, or delete categories

**Filter by Category** - View tasks from a specific category

**Save and Quit** - Exit the application and save all changes

## Task Status Options
**urgent** - High priority tasks

**semi-urgent** - Medium priority tasks

**non-urgent** - Low priority tasks

**Done** - Completed tasks

# Due Date Format
Enter dates in DD-MM-YYYY format (e.g., 25-12-2024) or press Enter for no due date.

## File Structure

CLI_VERSION/
├── main.py              # Main application file (v2.0)
├── v3code.py            # Version 3.0 main application file
├── tasks.txt            # Active tasks storage
├── completed_tasks.txt  # Archived completed tasks
├── categories.txt       # Category definitions and colors
└── README.md            # Documentation
Data Storage
Active Tasks (tasks.txt)
Tasks are stored in pipe-separated format:

text
task_name | status | due_date | category
Completed Tasks (completed_tasks.txt)
Archived tasks include completion date:

text
task_name | status | due_date | completion_date | category
Categories (categories.txt)
Category definitions with color codes:

text
category_name | ANSI_color_code
Color Coding System
Task Status Colors
<span style="color: red;">Red: Urgent tasks</span>

<span style="color: gold;">Yellow: Semi-urgent tasks</span>

<span style="color: green;">Green: Non-urgent tasks</span>

<span style="color: blue;">Blue: Completed tasks</span>

<span style="color: magenta; font-weight: bold;">Magenta: Overdue tasks (bold)</span>

## Category Colors
Available category colors (displayed in the application):

Blue

Green

Yellow

Magenta

Cyan

White

Red

Example Usage
Start the application

Select option 10 to create a new category ("Work" with blue color)

Select option 4 to add a new task

Description: "Finish project report"

Status: "urgent"

Due date: "15-01-2025"

Category: "Work"

View your tasks with option 1 (grouped by category)

Use option 9 to check statistics (including category breakdown)

Mark tasks complete with option 7 (automatically archived)

Filter by "Work" category with option 11

Save and exit with option 12

Statistics Features
The statistics panel shows:

Active tasks count

Completed (archived) tasks count

Total all-time tasks

Current urgent tasks

Overdue tasks count

All-time completion rate percentage

Task distribution by category

Notes
The application automatically creates necessary files if they don't exist

All changes are saved automatically when you modify tasks or categories

Completed tasks are automatically moved to the archive

Tasks are automatically sorted by due date and then by urgency

Overdue tasks are highlighted in magenta with [OVERDUE] indicator

Category changes automatically update all affected tasks

Invalid inputs will prompt you to try again

Version History
v1.0: Basic task management with JSON storage

v2.0: Enhanced with due dates, archiving, statistics, search, and color coding

v3.0: Added category management system with filtering and enhanced organization

Built with Python standard library - no external dependencies required
