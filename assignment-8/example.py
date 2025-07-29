# Example.py - Lesson 8: Lists - Introduction and Basic Operations
# This file demonstrates lists and basic list operations in Python

"""
Lists in Python

Lists are ordered collections of items that can hold different types of data.
They are mutable (changeable) and one of the most versatile data structures
in Python. Lists are perfect for storing related items that you need to
process as a group.
"""

print("=== Introduction to Lists ===")
print()

# Creating lists
print("1. Creating Lists:")

# Empty list
empty_list = []
empty_list2 = list()

# List with initial values
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, 3.14, True, "world"]

print(f"Empty list: {empty_list}")
print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed_list}")
print()

# List properties
print("2. List Properties:")
print(f"Length of fruits: {len(fruits)}")
print(f"Type of fruits: {type(fruits)}")
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Is 'kiwi' in fruits? {'kiwi' in fruits}")
print()

# Accessing list elements
print("=== Accessing List Elements ===")
print()

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors list: {colors}")
print()

print("3. Indexing:")
print(f"First color: colors[0] = {colors[0]}")
print(f"Second color: colors[1] = {colors[1]}")
print(f"Last color: colors[-1] = {colors[-1]}")
print(f"Second to last: colors[-2] = {colors[-2]}")
print()

print("4. List slicing:")
print(f"First three colors: {colors[:3]}")
print(f"Last two colors: {colors[-2:]}")
print(f"Middle colors: {colors[1:4]}")
print(f"Every second color: {colors[::2]}")
print(f"Reversed list: {colors[::-1]}")
print()

# Modifying lists
print("=== Modifying Lists ===")
print()

shopping_list = ["milk", "bread", "eggs"]
print(f"Original shopping list: {shopping_list}")
print()

print("5. Changing elements by index:")
shopping_list[1] = "whole wheat bread"
print(f"After changing bread: {shopping_list}")
print()

print("6. Adding elements:")

# append() - add to end
shopping_list.append("butter")
print(f"After append('butter'): {shopping_list}")

# insert() - add at specific position
shopping_list.insert(1, "cheese")
print(f"After insert(1, 'cheese'): {shopping_list}")

# Adding multiple items
shopping_list.extend(["apples", "bananas"])
print(f"After extend(['apples', 'bananas']): {shopping_list}")
print()

print("7. Removing elements:")

# remove() - remove first occurrence of item
shopping_list.remove("eggs")
print(f"After remove('eggs'): {shopping_list}")

# pop() - remove and return last item
last_item = shopping_list.pop()
print(f"Popped item: {last_item}")
print(f"After pop(): {shopping_list}")

# pop(index) - remove and return item at index
second_item = shopping_list.pop(1)
print(f"Popped item at index 1: {second_item}")
print(f"After pop(1): {shopping_list}")

# del - delete by index
del shopping_list[0]
print(f"After del shopping_list[0]: {shopping_list}")
print()

# Lists with loops
print("=== Lists with Loops ===")
print()

subjects = ["Math", "Science", "English", "History", "Art"]
print(f"Subjects: {subjects}")
print()

print("8. Iterating through lists:")
print("Simple iteration:")
for subject in subjects:
    print(f"- {subject}")
print()

print("9. Iteration with index:")
for i in range(len(subjects)):
    print(f"{i + 1}. {subjects[i]}")
print()

print("10. Using enumerate:")
for index, subject in enumerate(subjects, 1):
    print(f"{index}. {subject}")
print()

# List operations and methods
print("=== List Methods and Operations ===")
print()

grades = [85, 92, 78, 96, 88]
print(f"Grades: {grades}")
print()

print("11. List methods:")
print(f"Sum of grades: {sum(grades)}")
print(f"Average grade: {sum(grades) / len(grades):.1f}")
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")
print(f"Count of 88: {grades.count(88)}")

# Finding index of element
if 92 in grades:
    print(f"Index of 92: {grades.index(92)}")
print()

# Copying lists
print("12. Copying lists:")
original = [1, 2, 3, 4, 5]
copy1 = original[:]  # Slice copy
copy2 = original.copy()  # Method copy
copy3 = list(original)  # Constructor copy

print(f"Original: {original}")
print(f"Slice copy: {copy1}")
print(f"Method copy: {copy2}")
print(f"Constructor copy: {copy3}")

# Demonstrate that they are different objects
original.append(6)
print(f"After modifying original: {original}")
print(f"Copy remains unchanged: {copy1}")
print()

# List concatenation
print("13. List concatenation:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"Combined (list1 + list2): {combined}")

# In-place concatenation
list1 += [7, 8, 9]
print(f"list1 after += [7, 8, 9]: {list1}")
print()

# Practical examples
print("=== Practical Examples ===")
print()

print("14. Student grade management:")
student_grades = []

# Adding grades
student_grades.append(85)
student_grades.append(92)
student_grades.extend([78, 88, 95])

print(f"All grades: {student_grades}")
print(f"Number of grades: {len(student_grades)}")
print(f"Average: {sum(student_grades) / len(student_grades):.1f}")

# Find grades above average
average = sum(student_grades) / len(student_grades)
above_average = []
for grade in student_grades:
    if grade > average:
        above_average.append(grade)

print(f"Grades above average: {above_average}")
print()

print("15. Inventory management:")
inventory = ["laptop", "mouse", "keyboard", "monitor"]
print(f"Current inventory: {inventory}")

# Add new item
new_item = "printer"
inventory.append(new_item)
print(f"Added {new_item}: {inventory}")

# Remove sold item
sold_item = "mouse"
if sold_item in inventory:
    inventory.remove(sold_item)
    print(f"Sold {sold_item}: {inventory}")

# Check if item is available
item_to_check = "keyboard"
if item_to_check in inventory:
    print(f"{item_to_check} is available")
    position = inventory.index(item_to_check) + 1
    print(f"It's item #{position} in the list")
print()

print("16. Menu creation:")
menu_items = []
menu_items.append("Hamburger - $8.99")
menu_items.append("Pizza - $12.50")
menu_items.append("Salad - $7.25")
menu_items.append("Soup - $5.50")

print("Restaurant Menu:")
for i, item in enumerate(menu_items, 1):
    print(f"{i}. {item}")
print()

# List comprehension preview (basic)
print("17. Creating lists with patterns:")
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares of 1-5: {squares}")

even_numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)
print(f"Even numbers 1-10: {even_numbers}")
print()

# Nested lists (introduction)
print("18. Nested lists (introduction):")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")
print(f"First row: {matrix[0]}")
print(f"Element at row 1, column 2: {matrix[1][2]}")

# Students and their grades
students_data = [
    ["Alice", 85, 92, 88],
    ["Bob", 78, 85, 90],
    ["Carol", 92, 88, 95]
]

print("Student grades:")
for student_info in students_data:
    name = student_info[0]
    grades = student_info[1:]
    average = sum(grades) / len(grades)
    print(f"{name}: {grades} (Average: {average:.1f})")
print()

print("=== Common List Patterns ===")
print()

print("19. Building lists incrementally:")
user_inputs = []
print("Simulating user input collection:")
sample_inputs = ["apple", "banana", "cherry"]

for inp in sample_inputs:
    user_inputs.append(inp)
    print(f"Added '{inp}': {user_inputs}")
print()

print("20. Processing list data:")
numbers_list = [10, 25, 8, 42, 15, 33, 7]
print(f"Numbers: {numbers_list}")

# Find specific values
large_numbers = []
for num in numbers_list:
    if num > 20:
        large_numbers.append(num)

print(f"Numbers > 20: {large_numbers}")

# Calculate statistics
total = sum(numbers_list)
count = len(numbers_list)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average:.1f}")
print()

print("=== End of Examples ===")
print("Key Points to Remember:")
print("- Lists are ordered and mutable collections")
print("- Use [] to create lists and access elements")
print("- append() adds to end, insert() adds at position")
print("- remove() removes by value, pop() removes by index")
print("- Use for loops to iterate through lists")
print("- Lists can hold any type of data")
print("- len() gives the number of items in a list")
print("- Practice with real-world examples for better understanding")
