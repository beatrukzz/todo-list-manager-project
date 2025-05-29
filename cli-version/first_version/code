import os
# Load tasks from tasks.txt
def load_tasks():
    if os.path.exists('CLI_VERSION/tasks.txt'):
        with open('CLI_VERSION/tasks.txt', 'r') as file:
            tasks = []
            for line in file:
                line = line.strip()
                if line:
                    # Parse format: "task_name | status"
                    if ' | ' in line:
                        task_name, status = line.split(' | ', 1)
                        tasks.append({"task": task_name, "status": status})
            return tasks
    return []
# Save tasks to tasks.txt
def save_tasks():
    with open('CLI_VERSION/tasks.txt', 'w') as file:
        for task in to_do_list:
            file.write(f"{task['task']} | {task['status']}\n")
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
    for index, task in enumerate(to_do_list,1):
      print(f"{index}. {task['task']} - {task['status']}")
      print("")
# function to view incompleted tasks
def view_incompleted_tasks():
    print("")
    print("Incompleted tasks: ")
    if len(to_do_list) == 0:
        print("You have no incompleted tasks.")
        print(" ")
    else:
        incomplete_tasks = [task for task in to_do_list if task['status'] != "Done"]
        if len(incomplete_tasks) == 0:
            print("You have no incompleted tasks.")
        else:
            for index, task in enumerate(incomplete_tasks, 1):
                print(f"{index}. {task['task']} - {task['status']}")
    print(" ")
# function to view completed tasks
def view_completed_tasks():
    print("")
    print("Completed tasks: ")
    if len(to_do_list) == 0:
        print("You have no completed tasks.")
        print(" ")
    else:
        completed_tasks = [task for task in to_do_list if task['status'] == "Done"]
        if len(completed_tasks) == 0:
            print("You have no completed tasks.")
        else:
            for index, task in enumerate(completed_tasks, 1):
                print(f"{index}. {task['task']} - {task['status']}")
    print(" ")
# function to add task
def add_task():
    print("")
    task = input("enter the task you want to add: ")
    status_of_task = input("enter the status of the task (urgent, non-urgent, semi-urgent): ")
    to_do_list.append({"task": task, "status": status_of_task})
    save_tasks()
    print("")
    print("task added successfully\n")
    print("")
    print("current to-do list: ")
    for item in to_do_list:
        print(f"- Task: {item['task']}, Status: {item['status']}")
    print(" ")
    next_task = input("do you want to add another task? (yes/no): ")
    if next_task == "yes":
        add_task()
    else:
        display_menu()
        return
# function to edit task
def edit_task():
    if len(to_do_list) == 0:
        print("Your to-do list is empty.")
        print(" ")
        display_menu()
    else:
        try:
            search_index = int(input("Enter the number of the task you want to edit: ")) - 1
            if 0 <= search_index < len(to_do_list):
                new_task_name = input("Enter the new task name: ")
                new_status = input("Enter the new status of the task (urgent, non-urgent, semi-urgent, Done): ")
                to_do_list[search_index]['task'] = new_task_name
                to_do_list[search_index]['status'] = new_status
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
    display_menu()
  else:
    try:
        search_index = int(input("enter the number of the task you want to delete: ")) - 1
        if 0 <= search_index < len(to_do_list):
            deleted_task = to_do_list.pop(search_index)
            print(f"Task Removed: {deleted_task['task']}")
            save_tasks()
            print(" ")
        else:
            print("Invalid task number. Please try again.")
            print(" ")
            next_task_to_be_deleted = input("do you want to delete another task? (yes/no): ")
            if next_task_to_be_deleted == "yes":
               delete_task()
               print("")
            else:
               display_menu()
               print("")
               view_current_to_do_list = input("do you want to view the current to-do list? (yes/no): ")
               if view_current_to_do_list == "yes":
                  view_to_do_list()
                  print("")
               else:
                  display_menu()
                  print("")

    except ValueError:
        print("Please enter a valid number.")
        print(" ")
        delete_task()
        print("")
        return      
# function to mark task as complete
def mark_task_as_complete():
    if len(to_do_list) == 0:
        print("your to-do list is empty")
        print(" ")
        display_menu()
    else:
        try:
            print("")
            search_index = int(input("enter the number of the task you want to mark as complete: ")) - 1
            if 0 <= search_index < len(to_do_list):
                to_do_list[search_index]['status'] = "Done"
                print(f"Task {to_do_list[search_index]['task']} marked as Done.")
                save_tasks()
                print(" ")
                view_current_to_do_list = input("do you want to view your current to-do list? (yes/no): ")
                if view_current_to_do_list == "yes":
                    view_to_do_list()
                    print("")
                    display_menu()
                    print("")
                else:
                    display_menu()
                mark_another_task = input("do you want to mark another task as complete? (yes/no): ")
                if mark_another_task == "yes":
                    mark_task_as_complete()
                    print("")
                    display_menu()
                    print("")
                else:
                    display_menu()
                    print("")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:  
            print("")
            print("Please enter a valid number.")
            print(" ")
# Function to save and quit
def save_and_quit():
    save_tasks()
    exit()
# function to display main menu
def display_menu():
    print("")
    while(True):
        print("1 - View To-Do List")
        print("2 - View incompleted Tasks")
        print("3 - View completed Tasks")
        print("4 - Add Task")
        print("5 - Edit Task")
        print("6 - Delete Task")
        print("7 - Mark Task as Complete")
        print("8 - save and quit")
        print("      ")
        print("plese enter the number corresponding to your choice")

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
          print("exsiting and saving......")
          save_and_quit()
          exit()
        else:
          print("Invalid choice. Please try again.")
display_menu()
