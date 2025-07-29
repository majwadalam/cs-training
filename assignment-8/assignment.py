# Assignment.py - Lesson 8: To-Do List Manager with Lists
# Student Name: [Write your name here]
# Date: [Write today's date here]

"""
Assignment: Create a simple to-do list manager where users can add, remove, 
and display tasks.

Requirements:
1. Create a menu-driven interface with options:
   - Add a new task
   - Remove a task (by name or index)
   - Display all tasks
   - Mark task as complete (optional)
   - Clear all tasks
   - Show statistics (total tasks, completed, etc.)
   - Quit the program
2. Use list methods like append(), remove(), pop(), insert()
3. Handle empty list situations gracefully
4. Display tasks with numbers for easy reference
5. Validate user input and handle errors
6. Use loops to iterate through tasks
7. Include clear user prompts and feedback

Example Output:
=== To-Do List Manager ===
Welcome to your personal task manager!

Current tasks: 0

Menu Options:
1. Add a new task
2. Remove a task
3. Display all tasks
4. Mark task as complete
5. Clear all tasks
6. Show statistics
7. Quit

Choose an option (1-7): 1
Enter a new task: Buy groceries
Task "Buy groceries" added successfully!

Choose an option (1-7): 1
Enter a new task: Finish homework
Task "Finish homework" added successfully!

Choose an option (1-7): 3
=== Your Tasks ===
1. Buy groceries
2. Finish homework
Total: 2 tasks

Choose an option (1-7): 7
Thank you for using the To-Do List Manager!
"""

# TODO: Write your to-do list manager below
# Remember to use lists, list methods, and loops!

print("=== To-Do List Manager ===")
print("Welcome to your personal task manager!")
print()

# TODO: Initialize the main task list
# tasks = []
# completed_tasks = []  # Optional: track completed tasks

# TODO: Main program loop
# while True:
    # TODO: Display current status
    # print(f"Current tasks: {len(tasks)}")
    # print()
    
    # TODO: Display menu options
    # print("Menu Options:")
    # print("1. Add a new task")
    # print("2. Remove a task")
    # print("3. Display all tasks")
    # print("4. Mark task as complete")
    # print("5. Clear all tasks")
    # print("6. Show statistics")
    # print("7. Quit")
    # print()
    
    # TODO: Get user choice
    # choice = input("Choose an option (1-7): ")
    
    # TODO: Handle each menu option
    
    # Option 1: Add task
    # if choice == "1":
    #     new_task = input("Enter a new task: ").strip()
    #     if new_task:
    #         tasks.append(new_task)
    #         print(f'Task "{new_task}" added successfully!')
    #     else:
    #         print("Task cannot be empty!")
    
    # Option 2: Remove task
    # elif choice == "2":
    #     if not tasks:
    #         print("No tasks to remove!")
    #     else:
    #         # Show current tasks first
    #         # Allow removal by name or index
    
    # Option 3: Display tasks
    # elif choice == "3":
    #     if not tasks:
    #         print("No tasks in your list!")
    #     else:
    #         print("=== Your Tasks ===")
    #         for i, task in enumerate(tasks, 1):
    #             print(f"{i}. {task}")
    #         print(f"Total: {len(tasks)} tasks")
    
    # Continue with other options...

# TODO: Helper functions to organize your code

def display_tasks(task_list, title="Your Tasks"):
    """Display all tasks in a formatted list"""
    # if not task_list:
    #     print("No tasks in your list!")
    #     return
    # 
    # print(f"=== {title} ===")
    # for i, task in enumerate(task_list, 1):
    #     print(f"{i}. {task}")
    # print(f"Total: {len(task_list)} tasks")
    pass

def add_task(task_list, task):
    """Add a new task to the list"""
    # if task.strip():
    #     task_list.append(task.strip())
    #     return True
    # return False
    pass

def remove_task_by_index(task_list, index):
    """Remove task by index (1-based)"""
    # try:
    #     if 1 <= index <= len(task_list):
    #         removed_task = task_list.pop(index - 1)
    #         return removed_task
    # except (ValueError, IndexError):
    #     pass
    # return None
    pass

def remove_task_by_name(task_list, task_name):
    """Remove task by name"""
    # try:
    #     task_list.remove(task_name)
    #     return True
    # except ValueError:
    #     return False
    pass

def show_statistics(tasks, completed_tasks):
    """Show task statistics"""
    # total_tasks = len(tasks) + len(completed_tasks)
    # print(f"=== Task Statistics ===")
    # print(f"Active tasks: {len(tasks)}")
    # print(f"Completed tasks: {len(completed_tasks)}")
    # print(f"Total tasks created: {total_tasks}")
    # 
    # if total_tasks > 0:
    #     completion_rate = len(completed_tasks) / total_tasks * 100
    #     print(f"Completion rate: {completion_rate:.1f}%")
    pass

# Start your code here:

# Basic structure example:
# tasks = []
# completed_tasks = []
# 
# while True:
#     print(f"\nCurrent tasks: {len(tasks)}")
#     if completed_tasks:
#         print(f"Completed tasks: {len(completed_tasks)}")
#     print()
#     
#     print("Menu Options:")
#     print("1. Add a new task")
#     print("2. Remove a task")
#     print("3. Display all tasks")
#     print("4. Mark task as complete")
#     print("5. Clear all tasks")
#     print("6. Show statistics")
#     print("7. Quit")
#     print()
#     
#     choice = input("Choose an option (1-7): ").strip()
#     
#     if choice == "1":
#         # Add task logic
#         new_task = input("Enter a new task: ").strip()
#         if new_task:
#             tasks.append(new_task)
#             print(f'Task "{new_task}" added successfully!')
#         else:
#             print("Task cannot be empty!")
#     
#     elif choice == "2":
#         # Remove task logic
#         if not tasks:
#             print("No tasks to remove!")
#         else:
#             display_tasks(tasks)
#             print("\nRemove by:")
#             print("1. Task number")
#             print("2. Task name")
#             remove_choice = input("Choose (1 or 2): ").strip()
#             
#             if remove_choice == "1":
#                 try:
#                     task_num = int(input("Enter task number: "))
#                     if 1 <= task_num <= len(tasks):
#                         removed = tasks.pop(task_num - 1)
#                         print(f'Task "{removed}" removed successfully!')
#                     else:
#                         print("Invalid task number!")
#                 except ValueError:
#                     print("Please enter a valid number!")
#     
#     # Continue with other options...
#     
#     elif choice == "7":
#         print("Thank you for using the To-Do List Manager!")
#         break
#     
#     else:
#         print("Invalid choice! Please choose 1-7.")
#     
#     input("\nPress Enter to continue...")  # Pause before showing menu again
