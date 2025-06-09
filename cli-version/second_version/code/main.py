
import os
from datetime import datetime

# ANSI color codes for different urgencies
class Colors:
    RED = '\033[91m'      # urgent
    YELLOW = '\033[93m'   # semi-urgent
    GREEN = '\033[92m'    # non-urgent
    BLUE = '\033[94m'     # Done
    MAGENTA = '\033[95m'  # overdue
    BOLD = '\033[1m'      # bold text
    RESET = '\033[0m'     # Reset to default color

def get_color_for_status(status, due_date=None):
    """Return the appropriate color code for a task status"""
    # Check if overdue first (for non-completed tasks)
    if due_date and status.lower() != "done" and is_overdue(due_date):
        return Colors.MAGENTA + Colors.BOLD
    
    status_lower = status.lower()
    if status_lower == "urgent":
        return Colors.RED
    elif status_lower == "semi-urgent":
        return Colors.YELLOW
    elif status_lower == "non-urgent":
        return Colors.GREEN
    elif status_lower == "done":
        return Colors.BLUE
    else:
        return Colors.RESET

def parse_date(date_string):
    """Parse date string and return datetime object. Return None for invalid dates."""
    if date_string == "No due date":
        return None
    try:
        return datetime.strptime(date_string, "%d-%m-%Y")
    except ValueError:
        return None

def is_overdue(due_date_str):
    """Check if a task is overdue"""
    if due_date_str == "No due date":
        return False
    due_date = parse_date(due_date_str)
    if due_date is None:
        return False
    return due_date < datetime.now()

def get_urgency_priority(status):
    """Return numeric priority for urgency (lower number = higher priority)"""
    status_lower = status.lower()
    if status_lower == "urgent":
        return 1
    elif status_lower == "semi-urgent":
        return 2
    elif status_lower == "non-urgent":
        return 3
    elif status_lower == "done":
        return 4
    else:
        return 5

def sort_tasks(tasks):
    """Sort tasks by due date first, then by urgency"""
    def sort_key(task):
        due_date = parse_date(task['due_date'])
        urgency_priority = get_urgency_priority(task['status'])
        
        # Tasks with no due date go to the end
        if due_date is None:
            return (datetime.max, urgency_priority)
        else:
            return (due_date, urgency_priority)
    
    return sorted(tasks, key=sort_key)

# Load tasks from tasks.txt
def load_tasks():
    if os.path.exists('CLI_VERSION/tasks.txt'):
        with open('CLI_VERSION/tasks.txt', 'r') as file:
            tasks = []
            for line in file:
                line = line.strip()
                if line:
                    # Parse format: "task_name | status | due_date"
                    parts = line.split(' | ')
                    if len(parts) >= 2:
                        task_name = parts[0]
                        status = parts[1]
                        due_date = parts[2] if len(parts) > 2 else "No due date"
                        tasks.append({"task": task_name, "status": status, "due_date": due_date})
            return tasks
    return []

# Load archived (completed) tasks from completed_tasks.txt
def load_archived_tasks():
    if os.path.exists('CLI_VERSION/completed_tasks.txt'):
        with open('CLI_VERSION/completed_tasks.txt', 'r') as file:
            tasks = []
            for line in file:
                line = line.strip()
                if line:
                    # Parse format: "task_name | status | due_date | completion_date"
                    parts = line.split(' | ')
                    if len(parts) >= 3:
                        task_name = parts[0]
                        status = parts[1]
                        due_date = parts[2] if len(parts) > 2 else "No due date"
                        completion_date = parts[3] if len(parts) > 3 else "Unknown"
                        tasks.append({"task": task_name, "status": status, "due_date": due_date, "completion_date": completion_date})
            return tasks
    return []

# Save active tasks to tasks.txt (excluding completed ones)
def save_tasks():
    active_tasks = [task for task in to_do_list if task['status'].lower() != 'done']
    with open('CLI_VERSION/tasks.txt', 'w') as file:
        for task in active_tasks:
            file.write(f"{task['task']} | {task['status']} | {task['due_date']}\n")

# Archive completed tasks to completed_tasks.txt
def archive_completed_tasks():
    global to_do_list
    completed_tasks = [task for task in to_do_list if task['status'].lower() == 'done']
    if completed_tasks:
        with open('CLI_VERSION/completed_tasks.txt', 'a') as file:
            for task in completed_tasks:
                completion_date = datetime.now().strftime("%d-%m-%Y")
                file.write(f"{task['task']} | {task['status']} | {task['due_date']} | {completion_date}\n")
        
        # Remove completed tasks from active list
        to_do_list = [task for task in to_do_list if task['status'].lower() != 'done']

# Initialize to_do_list from file
to_do_list = load_tasks()

print("======= To-DO List =======")

# Function to view to-do list
def view_to_do_list():
    print("")
    print("current to-do list: ")
    if len(to_do_list) == 0:
        print("")
        print("you have no pending tasks :)")
        print(" ")
    else:
        sorted_tasks = sort_tasks(to_do_list)
        for index, task in enumerate(sorted_tasks,1):
            color = get_color_for_status(task['status'], task['due_date'])
            overdue_text = " [OVERDUE]" if is_overdue(task['due_date']) and task['status'].lower() != "done" else ""
            print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){overdue_text}{Colors.RESET}")
            print("")

# function to view incompleted tasks
def view_incompleted_tasks():
    print("")
    print("Incompleted tasks: ")
    if len(to_do_list) == 0:
        print("You have no incompleted tasks.")
        print(" ")
    else:
        incomplete_tasks = [task for task in to_do_list if task['status'].lower() != "done"]
        if len(incomplete_tasks) == 0:
            print("You have no incompleted tasks.")
        else:
            sorted_incomplete_tasks = sort_tasks(incomplete_tasks)
            for index, task in enumerate(sorted_incomplete_tasks, 1):
                color = get_color_for_status(task['status'])
                print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){Colors.RESET}")
    print(" ")

# function to view completed tasks (from archive)
def view_completed_tasks():
    print("")
    print("Completed tasks (archived): ")
    archived_tasks = load_archived_tasks()
    if len(archived_tasks) == 0:
        print("You have no completed tasks.")
        print(" ")
    else:
        for index, task in enumerate(archived_tasks, 1):
            color = get_color_for_status(task['status'])
            completion_date = task.get('completion_date', 'Unknown')
            print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}) [Completed: {completion_date}]{Colors.RESET}")
    print(" ")

# function to add task
def add_task():
    print("")
    task = input("enter the task you want to add: ")
    status_of_task = input("enter the status of the task (urgent, non-urgent, semi-urgent): ")
    due_date = input("enter the due date (DD-MM-YYYY) or press Enter for no due date: ")
    if not due_date.strip():
        due_date = "No due date"
    to_do_list.append({"task": task, "status": status_of_task, "due_date": due_date})
    save_tasks()
    print("")
    print("task added successfully\n")
    print("")
    print("current to-do list: ")
    sorted_tasks = sort_tasks(to_do_list)
    for item in sorted_tasks:
        color = get_color_for_status(item['status'])
        print(f"- Task: {color}{item['task']}, Status: {item['status']}, Due: {item['due_date']}{Colors.RESET}")
    print(" ")
    next_task = input("do you want to add another task? (yes/no): ")
    if next_task == "yes":
        add_task()

# function to edit task
def edit_task():
    if len(to_do_list) == 0:
        print("Your to-do list is empty.")
        print(" ")
        return
    
    # Display tasks with original indices for accurate selection
    print("")
    print("current to-do list: ")
    for index, task in enumerate(to_do_list, 1):
        color = get_color_for_status(task['status'], task['due_date'])
        overdue_text = " [OVERDUE]" if is_overdue(task['due_date']) and task['status'].lower() != "done" else ""
        print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){overdue_text}{Colors.RESET}")
        print("")
    
    try:
        search_index = int(input("Enter the number of the task you want to edit: ")) - 1
        if 0 <= search_index < len(to_do_list):
            new_task_name = input("Enter the new task name: ")
            new_status = input("Enter the new status of the task (urgent, non-urgent, semi-urgent, Done): ")
            new_due_date = input("Enter the new due date (DD-MM-YYYY) or press Enter to keep current: ")
            if not new_due_date.strip():
                new_due_date = to_do_list[search_index]['due_date']
            to_do_list[search_index]['task'] = new_task_name
            to_do_list[search_index]['status'] = new_status
            to_do_list[search_index]['due_date'] = new_due_date
            save_tasks() 
            print("Task updated successfully.")
            print(" ")
        else:
            print("Invalid task number. Please try again.")
            print(" ")
    except ValueError:
        print("Please enter a valid number.")
        print(" ")

# function to delete task
def delete_task():
    if len(to_do_list) == 0:
        print("your to-do list is empty")
        print(" ")
        return
    
    # Display tasks with original indices for accurate selection
    print("")
    print("current to-do list: ")
    for index, task in enumerate(to_do_list, 1):
        color = get_color_for_status(task['status'], task['due_date'])
        overdue_text = " [OVERDUE]" if is_overdue(task['due_date']) and task['status'].lower() != "done" else ""
        print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){overdue_text}{Colors.RESET}")
        print("")
    
    try:
        search_index = int(input("enter the number of the task you want to delete: ")) - 1
        if 0 <= search_index < len(to_do_list):
            deleted_task = to_do_list.pop(search_index)
            print(f"Task Removed: {deleted_task['task']}")
            save_tasks()
            print(" ")
            
            next_task_to_be_deleted = input("do you want to delete another task? (yes/no): ")
            if next_task_to_be_deleted == "yes":
                delete_task()
        else:
            print("Invalid task number. Please try again.")
            print(" ")
    except ValueError:
        print("Please enter a valid number.")
        print(" ")

# function to show task statistics
def show_statistics():
    archived_tasks = load_archived_tasks()
    active_tasks = len(to_do_list)
    completed_count = len(archived_tasks)
    total_all_time = active_tasks + completed_count
    
    if total_all_time == 0:
        print("You have no tasks.")
        print(" ")
        return
    
    urgent = len([task for task in to_do_list if task['status'].lower() == "urgent"])
    overdue = len([task for task in to_do_list if is_overdue(task['due_date'])])
    
    print("\n=== Task Statistics ===")
    print(f"Active tasks: {active_tasks}")
    print(f"Completed (archived): {completed_count}")
    print(f"Total all-time tasks: {total_all_time}")
    print(f"Urgent tasks: {urgent}")
    print(f"Overdue tasks: {Colors.MAGENTA}{overdue}{Colors.RESET}")
    if total_all_time > 0:
        completion_rate = (completed_count / total_all_time) * 100
        print(f"All-time completion rate: {completion_rate:.1f}%")
    print(" ")

# function to search tasks
def search_tasks():
    if len(to_do_list) == 0:
        print("Your to-do list is empty.")
        print(" ")
        return
    
    search_term = input("Enter search term: ").lower()
    matching_tasks = [task for task in to_do_list if search_term in task['task'].lower()]
    
    if not matching_tasks:
        print("No tasks found matching your search.")
        print(" ")
        return
    
    print(f"\nTasks matching '{search_term}':")
    sorted_matches = sort_tasks(matching_tasks)
    for index, task in enumerate(sorted_matches, 1):
        color = get_color_for_status(task['status'])
        print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){Colors.RESET}")
    print(" ")

# function to mark task as complete
def mark_task_as_complete():
    if len(to_do_list) == 0:
        print("your to-do list is empty")
        print(" ")
        return
    
    # Display tasks with original indices for accurate selection
    print("")
    print("current to-do list: ")
    for index, task in enumerate(to_do_list, 1):
        color = get_color_for_status(task['status'], task['due_date'])
        overdue_text = " [OVERDUE]" if is_overdue(task['due_date']) and task['status'].lower() != "done" else ""
        print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){overdue_text}{Colors.RESET}")
        print("")
    
    try:
        search_index = int(input("enter the number of the task you want to mark as complete: ")) - 1
        if 0 <= search_index < len(to_do_list):
            to_do_list[search_index]['status'] = "Done"
            task_name = to_do_list[search_index]['task']
            print(f"Task '{task_name}' marked as Done and will be archived.")
            
            # Archive completed tasks and save remaining active tasks
            archive_completed_tasks()
            save_tasks()
            print(" ")
            
            mark_another_task = input("do you want to mark another task as complete? (yes/no): ")
            if mark_another_task == "yes":
                mark_task_as_complete()
        else:
            print("Invalid task number. Please try again.")
    except ValueError:  
        print("")
        print("Please enter a valid number.")
        print(" ")

# Function to save and quit
def save_and_quit():
    archive_completed_tasks()
    save_tasks()
    print("Tasks saved successfully. Goodbye!")
    exit()

# function to display main menu
def display_menu():
    print("")
    while True:
        print("1 - View To-Do List")
        print("2 - View incompleted Tasks")
        print("3 - View completed Tasks")
        print("4 - Add Task")
        print("5 - Edit Task")
        print("6 - Delete Task")
        print("7 - Mark Task as Complete")
        print("8 - Search Tasks")
        print("9 - Show Statistics")
        print("10 - save and quit")
        print("      ")
        print("please enter the number corresponding to your choice")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_to_do_list()
            elif choice == 2:
                view_incompleted_tasks()
            elif choice == 3:
                view_completed_tasks()
            elif choice == 4:
                add_task()
            elif choice == 5:
                edit_task()
            elif choice == 6:
                delete_task()
            elif choice == 7:
                mark_task_as_complete()
            elif choice == 8:
                search_tasks()
            elif choice == 9:
                show_statistics()
            elif choice == 10:
                print("exiting and saving......")
                save_and_quit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

display_menu()
