
import os
from datetime import datetime

# ANSI color codes for different urgencies
class Colors:
    RED = '\033[91m'      # urgent
    YELLOW = '\033[93m'   # semi-urgent
    GREEN = '\033[92m'    # non-urgent
    BLUE = '\033[94m'     # Done
    MAGENTA = '\033[95m'  # overdue
    CYAN = '\033[96m'     # category colors
    WHITE = '\033[97m'    # category colors
    BOLD = '\033[1m'      # bold text
    RESET = '\033[0m'     # Reset to default color

# Available colors for categories
CATEGORY_COLORS = {
    '1': '\033[94m',  # Blue
    '2': '\033[92m',  # Green
    '3': '\033[93m',  # Yellow
    '4': '\033[95m',  # Magenta
    '5': '\033[96m',  # Cyan
    '6': '\033[97m',  # White
    '7': '\033[91m',  # Red
}

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

# Load categories from categories.txt
def load_categories():
    if os.path.exists('CLI_VERSION/categories.txt'):
        with open('CLI_VERSION/categories.txt', 'r') as file:
            categories = {}
            for line in file:
                line = line.strip()
                if line and ' | ' in line:
                    name, color = line.split(' | ')
                    # Convert string escape sequences to actual ANSI codes
                    color = color.encode().decode('unicode_escape')
                    categories[name] = color
            return categories
    return {}

# Save categories to categories.txt
def save_categories(categories):
    with open('CLI_VERSION/categories.txt', 'w') as file:
        for name, color in categories.items():
            file.write(f"{name} | {color}\n")

# Load tasks from tasks.txt
def load_tasks():
    if os.path.exists('CLI_VERSION/tasks.txt'):
        with open('CLI_VERSION/tasks.txt', 'r') as file:
            tasks = []
            for line in file:
                line = line.strip()
                if line:
                    # Parse format: "task_name | status | due_date | category"
                    parts = line.split(' | ')
                    if len(parts) >= 2:
                        task_name = parts[0]
                        status = parts[1]
                        due_date = parts[2] if len(parts) > 2 else "No due date"
                        category = parts[3] if len(parts) > 3 else "General"
                        tasks.append({"task": task_name, "status": status, "due_date": due_date, "category": category})
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
                    # Parse format: "task_name | status | due_date | completion_date | category"
                    parts = line.split(' | ')
                    if len(parts) >= 3:
                        task_name = parts[0]
                        status = parts[1]
                        due_date = parts[2] if len(parts) > 2 else "No due date"
                        completion_date = parts[3] if len(parts) > 3 else "Unknown"
                        category = parts[4] if len(parts) > 4 else "General"
                        tasks.append({"task": task_name, "status": status, "due_date": due_date, "completion_date": completion_date, "category": category})
            return tasks
    return []

# Save active tasks to tasks.txt (excluding completed ones)
def save_tasks():
    active_tasks = [task for task in to_do_list if task['status'].lower() != 'done']
    with open('CLI_VERSION/tasks.txt', 'w') as file:
        for task in active_tasks:
            category = task.get('category', 'General')
            file.write(f"{task['task']} | {task['status']} | {task['due_date']} | {category}\n")

# Archive completed tasks to completed_tasks.txt
def archive_completed_tasks():
    global to_do_list
    completed_tasks = [task for task in to_do_list if task['status'].lower() == 'done']
    if completed_tasks:
        with open('CLI_VERSION/completed_tasks.txt', 'a') as file:
            for task in completed_tasks:
                completion_date = datetime.now().strftime("%d-%m-%Y")
                category = task.get('category', 'General')
                file.write(f"{task['task']} | {task['status']} | {task['due_date']} | {completion_date} | {category}\n")
        
        # Remove completed tasks from active list
        to_do_list = [task for task in to_do_list if task['status'].lower() != 'done']

# Initialize to_do_list from file
to_do_list = load_tasks()

print("======= To-DO List =======")

# Function to view to-do list with categories
def view_to_do_list():
    print("")
    print("Current to-do list: ")
    if len(to_do_list) == 0:
        print("")
        print("You have no pending tasks :)")
        print(" ")
    else:
        categories = load_categories()
        sorted_tasks = sort_tasks(to_do_list)
        
        # Group tasks by category
        tasks_by_category = {}
        for task in sorted_tasks:
            category = task.get('category', 'General')
            if category not in tasks_by_category:
                tasks_by_category[category] = []
            tasks_by_category[category].append(task)
        
        task_counter = 1
        for category_name, tasks in tasks_by_category.items():
            # Display category header with color
            category_color = categories.get(category_name, Colors.RESET)
            print(f"\n{category_color}{Colors.BOLD}=== {category_name} ==={Colors.RESET}")
            
            for task in tasks:
                color = get_color_for_status(task['status'], task['due_date'])
                overdue_text = " [OVERDUE]" if is_overdue(task['due_date']) and task['status'].lower() != "done" else ""
                print(f"{task_counter}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){overdue_text}{Colors.RESET}")
                task_counter += 1
            print("")

# Function to view incompleted tasks with categories
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
            categories = load_categories()
            sorted_incomplete_tasks = sort_tasks(incomplete_tasks)
            
            # Group tasks by category
            tasks_by_category = {}
            for task in sorted_incomplete_tasks:
                category = task.get('category', 'General')
                if category not in tasks_by_category:
                    tasks_by_category[category] = []
                tasks_by_category[category].append(task)
            
            task_counter = 1
            for category_name, tasks in tasks_by_category.items():
                # Display category header with color
                category_color = categories.get(category_name, Colors.RESET)
                print(f"\n{category_color}{Colors.BOLD}=== {category_name} ==={Colors.RESET}")
                
                for task in tasks:
                    color = get_color_for_status(task['status'], task['due_date'])
                    overdue_text = " [OVERDUE]" if is_overdue(task['due_date']) and task['status'].lower() != "done" else ""
                    print(f"{task_counter}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){overdue_text}{Colors.RESET}")
                    task_counter += 1
    print(" ")

# Function to view completed tasks (from archive) with categories
def view_completed_tasks():
    print("")
    print("Completed tasks (archived): ")
    archived_tasks = load_archived_tasks()
    if len(archived_tasks) == 0:
        print("You have no completed tasks.")
        print(" ")
    else:
        categories = load_categories()
        
        # Group tasks by category
        tasks_by_category = {}
        for task in archived_tasks:
            category = task.get('category', 'General')
            if category not in tasks_by_category:
                tasks_by_category[category] = []
            tasks_by_category[category].append(task)
        
        task_counter = 1
        for category_name, tasks in tasks_by_category.items():
            # Display category header with color
            category_color = categories.get(category_name, Colors.RESET)
            print(f"\n{category_color}{Colors.BOLD}=== {category_name} ==={Colors.RESET}")
            
            for task in tasks:
                color = get_color_for_status(task['status'])
                completion_date = task.get('completion_date', 'Unknown')
                print(f"{task_counter}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}) [Completed: {completion_date}]{Colors.RESET}")
                task_counter += 1
    print(" ")

# Function to add task with category selection
def add_task():
    print("")
    task = input("Enter the task you want to add: ")
    status_of_task = input("Enter the status of the task (urgent, non-urgent, semi-urgent): ")
    due_date = input("Enter the due date (DD-MM-YYYY) or press Enter for no due date: ")
    if not due_date.strip():
        due_date = "No due date"
    
    # Category selection
    categories = load_categories()
    print("\nAvailable categories:")
    print("1. General")
    category_list = ["General"]
    
    if categories:
        for i, (name, color) in enumerate(categories.items(), 2):
            print(f"{i}. {color}{name}{Colors.RESET}")
            category_list.append(name)
    
    print(f"{len(category_list) + 1}. Create new category")
    
    try:
        choice = int(input("Select a category (number): "))
        if 1 <= choice <= len(category_list):
            category = category_list[choice - 1]
        elif choice == len(category_list) + 1:
            category = create_new_category()
        else:
            print("Invalid choice. Using 'General' category.")
            category = "General"
    except ValueError:
        print("Invalid input. Using 'General' category.")
        category = "General"
    
    to_do_list.append({"task": task, "status": status_of_task, "due_date": due_date, "category": category})
    save_tasks()
    print("")
    print("Task added successfully\n")
    print("")
    print("Current to-do list: ")
    view_to_do_list()
    
    next_task = input("Do you want to add another task? (yes/no): ")
    if next_task.lower() == "yes":
        add_task()

# Function to create a new category
def create_new_category():
    category_name = input("Enter new category name: ")
    
    print("\nAvailable colors:")
    for key, color in CATEGORY_COLORS.items():
        print(f"{key}. {color}Sample Text{Colors.RESET}")
    
    try:
        color_choice = input("Choose a color (1-7): ")
        if color_choice in CATEGORY_COLORS:
            selected_color = CATEGORY_COLORS[color_choice]
        else:
            print("Invalid choice. Using default color.")
            selected_color = Colors.RESET
    except:
        print("Invalid input. Using default color.")
        selected_color = Colors.RESET
    
    # Save the new category
    categories = load_categories()
    categories[category_name] = selected_color
    save_categories(categories)
    
    print(f"Category '{category_name}' created successfully!")
    return category_name

# Function to manage categories
def manage_categories():
    while True:
        print("\n=== Category Management ===")
        categories = load_categories()
        
        if categories:
            print("Current categories:")
            category_list = list(categories.keys())
            for i, (name, color) in enumerate(categories.items(), 1):
                print(f"{i}. {color}{name}{Colors.RESET}")
        else:
            print("No categories created yet.")
        
        print(f"\n{len(categories) + 1}. Create new category")
        if categories:
            print(f"{len(categories) + 2}. Edit category")
            print(f"{len(categories) + 3}. Delete category")
        print("0. Back to main menu")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                break
            elif choice == len(categories) + 1:
                create_new_category()
            elif categories and choice == len(categories) + 2:
                edit_category(categories)
            elif categories and choice == len(categories) + 3:
                delete_category(categories)
            elif 1 <= choice <= len(categories):
                category_name = list(categories.keys())[choice - 1]
                print(f"Selected category: {categories[category_name]}{category_name}{Colors.RESET}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function to edit category
def edit_category(categories):
    if not categories:
        print("No categories to edit.")
        return
    
    print("\nSelect category to edit:")
    category_list = list(categories.keys())
    for i, (name, color) in enumerate(categories.items(), 1):
        print(f"{i}. {color}{name}{Colors.RESET}")
    
    try:
        choice = int(input("Enter category number: ")) - 1
        if 0 <= choice < len(category_list):
            old_name = category_list[choice]
            new_name = input(f"Enter new name for '{old_name}' (or press Enter to keep current): ")
            if not new_name.strip():
                new_name = old_name
            
            print("\nAvailable colors:")
            for key, color in CATEGORY_COLORS.items():
                print(f"{key}. {color}Sample Text{Colors.RESET}")
            
            color_choice = input("Choose new color (1-7) or press Enter to keep current: ")
            if color_choice in CATEGORY_COLORS:
                new_color = CATEGORY_COLORS[color_choice]
            else:
                new_color = categories[old_name]
            
            # Update category
            del categories[old_name]
            categories[new_name] = new_color
            
            # Update tasks with old category name
            for task in to_do_list:
                if task.get('category') == old_name:
                    task['category'] = new_name
            
            save_categories(categories)
            save_tasks()
            print(f"Category updated successfully!")
        else:
            print("Invalid category number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete category
def delete_category(categories):
    if not categories:
        print("No categories to delete.")
        return
    
    print("\nSelect category to delete:")
    category_list = list(categories.keys())
    for i, (name, color) in enumerate(categories.items(), 1):
        print(f"{i}. {color}{name}{Colors.RESET}")
    
    try:
        choice = int(input("Enter category number: ")) - 1
        if 0 <= choice < len(category_list):
            category_to_delete = category_list[choice]
            
            # Check if any tasks use this category
            tasks_with_category = [task for task in to_do_list if task.get('category') == category_to_delete]
            
            if tasks_with_category:
                print(f"Warning: {len(tasks_with_category)} tasks use this category.")
                move_choice = input("Move these tasks to 'General' category? (yes/no): ")
                if move_choice.lower() == 'yes':
                    for task in tasks_with_category:
                        task['category'] = 'General'
                    save_tasks()
                else:
                    print("Category deletion cancelled.")
                    return
            
            del categories[category_to_delete]
            save_categories(categories)
            print(f"Category '{category_to_delete}' deleted successfully!")
        else:
            print("Invalid category number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to filter tasks by category
def filter_by_category():
    categories = load_categories()
    
    print("\nSelect category to filter by:")
    print("1. General")
    category_list = ["General"]
    
    if categories:
        for i, (name, color) in enumerate(categories.items(), 2):
            print(f"{i}. {color}{name}{Colors.RESET}")
            category_list.append(name)
    
    try:
        choice = int(input("Enter category number: ")) - 1
        if 0 <= choice < len(category_list):
            selected_category = category_list[choice]
            filtered_tasks = [task for task in to_do_list if task.get('category') == selected_category]
            
            if not filtered_tasks:
                print(f"No tasks found in category '{selected_category}'.")
                return
            
            print(f"\nTasks in category '{selected_category}':")
            sorted_filtered = sort_tasks(filtered_tasks)
            for index, task in enumerate(sorted_filtered, 1):
                color = get_color_for_status(task['status'], task['due_date'])
                overdue_text = " [OVERDUE]" if is_overdue(task['due_date']) and task['status'].lower() != "done" else ""
                print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}){overdue_text}{Colors.RESET}")
            print(" ")
        else:
            print("Invalid category number.")
    except ValueError:
        print("Please enter a valid number.")

# function to edit task
def edit_task():
    if len(to_do_list) == 0:
        print("Your to-do list is empty.")
        print(" ")
        return
    
    # Display tasks with original indices for accurate selection
    print("")
    print("Current to-do list: ")
    for index, task in enumerate(to_do_list, 1):
        color = get_color_for_status(task['status'], task['due_date'])
        overdue_text = " [OVERDUE]" if is_overdue(task['due_date']) and task['status'].lower() != "done" else ""
        category = task.get('category', 'General')
        print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}) [Category: {category}]{overdue_text}{Colors.RESET}")
        print("")
    
    try:
        search_index = int(input("Enter the number of the task you want to edit: ")) - 1
        if 0 <= search_index < len(to_do_list):
            new_task_name = input("Enter the new task name: ")
            new_status = input("Enter the new status of the task (urgent, non-urgent, semi-urgent, Done): ")
            new_due_date = input("Enter the new due date (DD-MM-YYYY) or press Enter to keep current: ")
            if not new_due_date.strip():
                new_due_date = to_do_list[search_index]['due_date']
            
            # Category selection
            categories = load_categories()
            print("\nAvailable categories:")
            print("1. General")
            category_list = ["General"]
            
            if categories:
                for i, (name, color) in enumerate(categories.items(), 2):
                    print(f"{i}. {color}{name}{Colors.RESET}")
                    category_list.append(name)
            
            print(f"{len(category_list) + 1}. Keep current category ({to_do_list[search_index].get('category', 'General')})")
            
            try:
                choice = int(input("Select a category (number): "))
                if 1 <= choice <= len(category_list):
                    new_category = category_list[choice - 1]
                elif choice == len(category_list) + 1:
                    new_category = to_do_list[search_index].get('category', 'General')
                else:
                    print("Invalid choice. Keeping current category.")
                    new_category = to_do_list[search_index].get('category', 'General')
            except ValueError:
                print("Invalid input. Keeping current category.")
                new_category = to_do_list[search_index].get('category', 'General')
            
            to_do_list[search_index]['task'] = new_task_name
            to_do_list[search_index]['status'] = new_status
            to_do_list[search_index]['due_date'] = new_due_date
            to_do_list[search_index]['category'] = new_category
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
    
    # Category statistics
    categories = load_categories()
    category_stats = {}
    for task in to_do_list:
        category = task.get('category', 'General')
        category_stats[category] = category_stats.get(category, 0) + 1
    
    print("\n=== Task Statistics ===")
    print(f"Active tasks: {active_tasks}")
    print(f"Completed (archived): {completed_count}")
    print(f"Total all-time tasks: {total_all_time}")
    print(f"Urgent tasks: {urgent}")
    print(f"Overdue tasks: {Colors.MAGENTA}{overdue}{Colors.RESET}")
    if total_all_time > 0:
        completion_rate = (completed_count / total_all_time) * 100
        print(f"All-time completion rate: {completion_rate:.1f}%")
    
    if category_stats:
        print("\n=== Tasks by Category ===")
        for category, count in category_stats.items():
            color = categories.get(category, Colors.RESET)
            print(f"{color}{category}: {count} tasks{Colors.RESET}")
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
        category = task.get('category', 'General')
        print(f"{index}. {color}{task['task']} - {task['status']} (Due: {task['due_date']}) [Category: {category}]{Colors.RESET}")
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
        print("10 - Manage Categories")
        print("11 - Filter by Category")
        print("12 - Save and quit")
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
                manage_categories()
            elif choice == 11:
                filter_by_category()
            elif choice == 12:
                print("exiting and saving......")
                save_and_quit()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

display_menu()
