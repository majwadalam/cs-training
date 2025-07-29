# Example.py - Lesson 6: Loops - For Loops and Range
# This file demonstrates for loops and the range() function in Python

"""
For Loops in Python

For loops are used to iterate over sequences (like numbers, strings, lists).
They are particularly useful when you know how many times you want to repeat something
or when you want to process each item in a collection.
"""

print("=== Introduction to For Loops ===")
print()

# Basic for loop with range
print("1. Basic For Loop:")
for i in range(5):
    print(f"Iteration {i}")

print("Loop finished!")
print()

# For loop counting from 1
print("2. Counting from 1 to 5:")
for number in range(1, 6):  # Start at 1, stop before 6
    print(f"Number: {number}")

print()

# The range() function in detail
print("=== Understanding the range() Function ===")
print()

print("3. Different ways to use range():")

# range(stop) - starts at 0
print("range(4):", end=" ")
for i in range(4):
    print(i, end=" ")
print()

# range(start, stop) - custom start and stop
print("range(2, 7):", end=" ")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step) - custom step
print("range(0, 10, 2):", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Counting backwards
print("range(10, 0, -1):", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()
print()

# Practical examples
print("=== Practical For Loop Examples ===")
print()

print("4. Sum of numbers from 1 to 10:")
total = 0
for num in range(1, 11):
    total += num
    print(f"Adding {num}, total so far: {total}")

print(f"Final sum: {total}")
print()

print("5. Multiplication table for 7:")
number = 7
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result}")

print()

# For loop with strings
print("6. Iterating over a string:")
word = "Python"
for letter in word:
    print(f"Letter: {letter}")

print()

# Counting and accumulating
print("7. Counting even and odd numbers:")
even_count = 0
odd_count = 0

for num in range(1, 21):
    if num % 2 == 0:
        even_count += 1
        print(f"{num} is even")
    else:
        odd_count += 1
        print(f"{num} is odd")

print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")
print()

# Nested for loops
print("=== Nested For Loops ===")
print()

print("8. Simple nested loop pattern:")
for row in range(3):
    for col in range(4):
        print(f"({row},{col})", end=" ")
    print()  # New line after each row

print()

print("9. Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        product = i * j
        print(f"{i}x{j}={product:2}", end="  ")
    print()  # New line after each row

print()

print("10. Number pattern:")
for row in range(1, 6):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()  # New line after each row

print()

# Advanced range examples
print("=== Advanced Range Examples ===")
print()

print("11. Skip counting by 3:")
for i in range(3, 31, 3):
    print(i, end=" ")
print()
print()

print("12. Countdown from 20 to 0 by 2s:")
for i in range(20, -1, -2):
    print(i, end=" ")
print()
print()

# Comparing for loops vs while loops
print("=== For Loop vs While Loop ===")
print()

print("13. Same task with for loop and while loop:")

print("For loop version:")
for i in range(5):
    print(f"Count: {i}")

print("\nWhile loop version:")
i = 0
while i < 5:
    print(f"Count: {i}")
    i += 1

print()

# Practical application: Grade processing
print("=== Practical Application: Processing Multiple Items ===")
print()

print("14. Processing test scores:")
test_scores = [85, 92, 78, 96, 88, 73, 91]

total_score = 0
highest_score = 0
lowest_score = 100

for i in range(len(test_scores)):
    score = test_scores[i]
    total_score += score
    
    if score > highest_score:
        highest_score = score
    
    if score < lowest_score:
        lowest_score = score
    
    print(f"Test {i+1}: {score}")

average_score = total_score / len(test_scores)
print(f"Average: {average_score:.1f}")
print(f"Highest: {highest_score}")
print(f"Lowest: {lowest_score}")
print()

# Creating patterns with loops
print("15. Creating patterns:")

print("Star triangle:")
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()

print()

print("Number square:")
for row in range(1, 5):
    for col in range(1, 5):
        print(row * col, end="\t")
    print()

print()

# Using enumerate for index and value
print("16. Using enumerate (advanced):")
fruits = ["apple", "banana", "orange", "grape"]

for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

print()

# Break and continue in for loops
print("=== Break and Continue in For Loops ===")
print()

print("17. Using break in for loop:")
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break
    print(i)

print()

print("18. Using continue in for loop:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

print()

# Comprehensive example: Times tables
print("=== Comprehensive Example: Times Tables ===")
print()

print("19. Complete multiplication table (1-5):")
print("     ", end="")
for col in range(1, 6):
    print(f"{col:4}", end="")
print()

for row in range(1, 6):
    print(f"{row:2} | ", end="")
    for col in range(1, 6):
        product = row * col
        print(f"{product:4}", end="")
    print()

print()

print("=== End of Examples ===")
print("Key Points to Remember:")
print("- For loops are great when you know the number of iterations")
print("- range() generates sequences of numbers")
print("- range(start, stop, step) gives you full control")
print("- Nested loops create patterns and tables")
print("- For loops are often more readable than while loops")
print("- Use break and continue to control loop flow")
print("- Practice with different range parameters")
