# Example.py - Lesson 9: Lists - Advanced Operations and List Comprehensions
# This file demonstrates advanced list operations and list comprehensions

"""
Advanced List Operations in Python

This lesson covers more sophisticated list operations including advanced
methods, list comprehensions, nested lists, and complex data processing
techniques that make Python particularly powerful for data manipulation.
"""

print("=== Advanced List Methods ===")
print()

# Sorting lists
print("1. Sorting Lists:")
numbers = [64, 25, 12, 22, 11, 90, 88, 76, 50, 25]
fruits = ["banana", "apple", "cherry", "date", "elderberry"]

print(f"Original numbers: {numbers}")
print(f"Original fruits: {fruits}")
print()

# Basic sorting
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"Sorted numbers: {numbers_copy}")

fruits_copy = fruits.copy()
fruits_copy.sort()
print(f"Sorted fruits: {fruits_copy}")
print()

# Reverse sorting
numbers_desc = numbers.copy()
numbers_desc.sort(reverse=True)
print(f"Numbers (descending): {numbers_desc}")

fruits_desc = fruits.copy()
fruits_desc.sort(reverse=True)
print(f"Fruits (reverse alphabetical): {fruits_desc}")
print()

# Custom sorting with key function
print("2. Custom Sorting:")
words = ["Python", "is", "awesome", "and", "powerful"]
print(f"Original words: {words}")

# Sort by length
words_by_length = words.copy()
words_by_length.sort(key=len)
print(f"Sorted by length: {words_by_length}")

# Sort by length (descending)
words_by_length_desc = words.copy()
words_by_length_desc.sort(key=len, reverse=True)
print(f"Sorted by length (desc): {words_by_length_desc}")
print()

# Reverse method
print("3. Reversing Lists:")
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Original: {colors}")

colors.reverse()
print(f"After reverse(): {colors}")

# Alternative ways to reverse
colors_sliced = ["red", "green", "blue", "yellow", "purple"]
reversed_sliced = colors_sliced[::-1]
print(f"Using slicing [::-1]: {reversed_sliced}")
print()

# Count and index methods
print("4. Count and Index Methods:")
grades = [85, 90, 78, 85, 92, 88, 85, 95, 90, 85]
print(f"Grades: {grades}")
print()

print(f"Count of 85: {grades.count(85)}")
print(f"Count of 90: {grades.count(90)}")
print(f"Count of 100: {grades.count(100)}")

print(f"First index of 85: {grades.index(85)}")
print(f"First index of 90: {grades.index(90)}")

# Find all indices of a value
target = 85
indices = []
for i, grade in enumerate(grades):
    if grade == target:
        indices.append(i)
print(f"All indices of {target}: {indices}")
print()

# List Comprehensions
print("=== List Comprehensions ===")
print()

print("5. Basic List Comprehensions:")

# Traditional way
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x ** 2)
print(f"Squares (traditional): {squares_traditional}")

# List comprehension way
squares_comprehension = [x ** 2 for x in range(1, 6)]
print(f"Squares (comprehension): {squares_comprehension}")
print()

print("6. List Comprehensions with Conditions:")
numbers = range(1, 21)

# Even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers 1-20: {evens}")

# Odd numbers squared
odd_squares = [x ** 2 for x in numbers if x % 2 == 1]
print(f"Odd squares 1-20: {odd_squares}")

# Numbers divisible by 3
div_by_3 = [x for x in numbers if x % 3 == 0]
print(f"Divisible by 3: {div_by_3}")
print()

print("7. String Processing with List Comprehensions:")
words = ["hello", "world", "python", "programming", "lists"]

# Uppercase all words
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")

# Words longer than 5 characters
long_words = [word for word in words if len(word) > 5]
print(f"Long words: {long_words}")

# First letter of each word
first_letters = [word[0] for word in words]
print(f"First letters: {first_letters}")

# Word lengths
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")
print()

# Nested Lists
print("=== Nested Lists ===")
print()

print("8. Creating and Accessing Nested Lists:")

# Student data: [name, age, [grades]]
students = [
    ["Alice", 18, [85, 92, 88, 95]],
    ["Bob", 19, [78, 85, 90, 87]],
    ["Carol", 18, [92, 88, 95, 90]],
    ["David", 20, [75, 80, 85, 82]],
    ["Eve", 19, [95, 98, 92, 96]]
]

print("Student data:")
for student in students:
    name, age, grades = student
    avg_grade = sum(grades) / len(grades)
    print(f"{name} (age {age}): {grades} - Average: {avg_grade:.1f}")
print()

print("9. Processing Nested Lists:")

# Find student with highest average
best_student = None
highest_avg = 0

for student in students:
    name, age, grades = student
    avg = sum(grades) / len(grades)
    if avg > highest_avg:
        highest_avg = avg
        best_student = name

print(f"Highest average: {best_student} with {highest_avg:.1f}")

# Students with average above 85
high_performers = []
for student in students:
    name, age, grades = student
    avg = sum(grades) / len(grades)
    if avg >= 85:
        high_performers.append(name)

print(f"High performers (≥85): {high_performers}")
print()

# Matrix operations
print("10. Matrix (2D List) Operations:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)
print()

# Sum of all elements
total = sum(sum(row) for row in matrix)
print(f"Sum of all elements: {total}")

# Sum of each row
row_sums = [sum(row) for row in matrix]
print(f"Row sums: {row_sums}")

# Sum of each column
col_sums = [sum(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0]))]
print(f"Column sums: {col_sums}")
print()

# Advanced List Comprehensions
print("=== Advanced List Comprehensions ===")
print()

print("11. Nested List Comprehensions:")

# Create multiplication table
mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Multiplication table (5x5):")
for row in mult_table:
    print(row)
print()

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in nested for num in row]
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")
print()

print("12. Complex List Comprehensions:")

# Student names with grades above 90
high_grade_students = [student[0] for student in students 
                      if any(grade > 90 for grade in student[2])]
print(f"Students with any grade > 90: {high_grade_students}")

# Average grades for all students
averages = [sum(student[2]) / len(student[2]) for student in students]
print(f"All averages: {[round(avg, 1) for avg in averages]}")

# Students sorted by average grade
students_by_avg = sorted(students, key=lambda s: sum(s[2]) / len(s[2]), reverse=True)
print("Students by average (highest first):")
for student in students_by_avg:
    name, age, grades = student
    avg = sum(grades) / len(grades)
    print(f"  {name}: {avg:.1f}")
print()

# Searching in Lists
print("=== Searching in Lists ===")
print()

data = [10, 25, 8, 42, 15, 33, 7, 18, 29, 36]
print(f"Data: {data}")
print()

print("13. Linear Search:")
def linear_search(lst, target):
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1

target = 42
index = linear_search(data, target)
print(f"Linear search for {target}: index {index}")

# Find all occurrences
target = 15
all_indices = [i for i, x in enumerate(data) if x == target]
print(f"All indices of {target}: {all_indices}")
print()

print("14. Binary Search (on sorted list):")
sorted_data = sorted(data)
print(f"Sorted data: {sorted_data}")

def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

target = 25
index = binary_search(sorted_data, target)
print(f"Binary search for {target}: index {index}")
print()

# Data Analysis with Lists
print("=== Data Analysis with Lists ===")
print()

sales_data = [
    ["January", 15000],
    ["February", 18000],
    ["March", 22000],
    ["April", 19000],
    ["May", 25000],
    ["June", 28000]
]

print("15. Sales Data Analysis:")
print("Monthly sales:")
for month, sales in sales_data:
    print(f"  {month}: ${sales:,}")
print()

# Extract sales amounts
sales_amounts = [sales for month, sales in sales_data]
print(f"Sales amounts: {sales_amounts}")

# Statistics
total_sales = sum(sales_amounts)
avg_sales = total_sales / len(sales_amounts)
max_sales = max(sales_amounts)
min_sales = min(sales_amounts)

print(f"Total sales: ${total_sales:,}")
print(f"Average sales: ${avg_sales:,.0f}")
print(f"Highest month: ${max_sales:,}")
print(f"Lowest month: ${min_sales:,}")

# Months above average
above_avg_months = [month for month, sales in sales_data if sales > avg_sales]
print(f"Months above average: {above_avg_months}")
print()

# Performance comparison
print("16. Performance Analysis:")
import time

# Compare list comprehension vs traditional loop
def time_operation(operation_name, operation):
    start_time = time.time()
    result = operation()
    end_time = time.time()
    print(f"{operation_name}: {end_time - start_time:.6f} seconds")
    return result

large_list = list(range(100000))

# Traditional loop
def traditional_squares():
    result = []
    for x in large_list:
        if x % 2 == 0:
            result.append(x ** 2)
    return result

# List comprehension
def comprehension_squares():
    return [x ** 2 for x in large_list if x % 2 == 0]

print("Performance comparison (even squares of 100,000 numbers):")
result1 = time_operation("Traditional loop", traditional_squares)
result2 = time_operation("List comprehension", comprehension_squares)
print(f"Results are equal: {result1 == result2}")
print()

print("=== End of Examples ===")
print("Key Points to Remember:")
print("- sort() modifies the list, sorted() returns a new list")
print("- List comprehensions are often faster and more readable")
print("- Nested lists can represent complex data structures")
print("- Use key functions for custom sorting")
print("- List comprehensions can replace many loops")
print("- Practice with real data for better understanding")
print("- Consider performance for large data sets")
