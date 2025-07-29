# Assignment.py - Lesson 6: Multiplication Table Generator with For Loops
# Student Name: [Write your name here]
# Date: [Write today's date here]

"""
Assignment: Create a multiplication table generator that displays tables 
for numbers 1-12 in a nicely formatted way.

Requirements:
1. Use for loops with the range() function
2. Create nested loops for generating multiplication tables
3. Display tables in a clear, formatted way
4. Allow user to choose specific table or all tables
5. Include proper headers and spacing
6. Show multiplication from 1 to 12 for each table
7. Use different range() parameters appropriately
8. Add comments explaining your loop structure

Example Output:
=== Multiplication Table Generator ===

Choose an option:
1. Display a specific table (1-12)
2. Display all tables (1-12)
3. Display tables in a range
4. Exit

Your choice: 1
Which table would you like to see? 7

=== Multiplication Table for 7 ===
7 x  1 =  7
7 x  2 = 14
7 x  3 = 21
7 x  4 = 28
7 x  5 = 35
7 x  6 = 42
7 x  7 = 49
7 x  8 = 56
7 x  9 = 63
7 x 10 = 70
7 x 11 = 77
7 x 12 = 84

Would you like to see another table? (yes/no): no
Thank you for using the Multiplication Table Generator!
"""

# TODO: Write your multiplication table generator below
# Remember to use for loops, range(), and proper formatting!

print("=== Multiplication Table Generator ===")
print("Welcome to the Multiplication Table Generator!")
print()

# TODO: Main program loop
# Use a while loop to allow multiple operations

    # TODO: Display menu options
    # 1. Specific table
    # 2. All tables  
    # 3. Range of tables
    # 4. Exit
    
    # TODO: Get user choice
    
    # TODO: Handle each menu option
    
    # Option 1: Specific table
    # if choice == "1":
    #     # Get table number from user (1-12)
    #     # Validate input
    #     # Display single multiplication table using for loop
    
    # Option 2: All tables
    # elif choice == "2":
    #     # Use nested for loops to display all tables 1-12
    #     # Outer loop: table numbers (1-12)
    #     # Inner loop: multipliers (1-12)
    
    # Option 3: Range of tables
    # elif choice == "3":
    #     # Get start and end numbers from user
    #     # Validate input
    #     # Display tables in range using nested loops
    
    # Option 4: Exit
    # elif choice == "4":
    #     # Exit the program
    
    # Invalid choice handling

# TODO: Helper function for displaying a single table
# def display_table(number):
#     # Use for loop with range(1, 13) to show table
#     # Format output nicely

# TODO: Helper function for displaying multiple tables
# def display_multiple_tables(start, end):
#     # Use nested for loops
#     # Outer loop: range(start, end + 1)
#     # Inner loop: range(1, 13)

# Start your code here:

# Hint: Structure your code like this:
# while True:
#     print("\nChoose an option:")
#     print("1. Display a specific table (1-12)")
#     print("2. Display all tables (1-12)")
#     print("3. Display tables in a range")
#     print("4. Exit")
#     
#     choice = input("\nYour choice: ")
#     
#     if choice == "1":
#         # Single table logic
#         try:
#             table_num = int(input("Which table would you like to see (1-12)? "))
#             if 1 <= table_num <= 12:
#                 print(f"\n=== Multiplication Table for {table_num} ===")
#                 for i in range(1, 13):
#                     result = table_num * i
#                     print(f"{table_num} x {i:2} = {result:3}")
#             else:
#                 print("Please enter a number between 1 and 12.")
#         except ValueError:
#             print("Please enter a valid number.")
#     
#     elif choice == "2":
#         # All tables logic
#         for table in range(1, 13):
#             print(f"\n=== Multiplication Table for {table} ===")
#             for multiplier in range(1, 13):
#                 result = table * multiplier
#                 print(f"{table} x {multiplier:2} = {result:3}")
#     
#     # Add other options...
#     
#     elif choice == "4":
#         print("Thank you for using the Multiplication Table Generator!")
#         break
