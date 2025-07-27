# Example.py - Week 2: Variables and Data Types
# This file demonstrates variables, data types, and basic operations

"""
What are Variables?
Variables are like containers that store data.
Think of them as labeled boxes that hold different types of information.
"""

print("=== Introduction to Variables ===")
print()

# Variable Assignment
# The equals sign (=) assigns a value to a variable
my_name = "Python Student"  # String variable
my_age = 18                 # Integer variable
my_height = 5.8            # Float variable
is_student = True          # Boolean variable

print("Variable Assignment Examples:")
print("my_name =", my_name)
print("my_age =", my_age)
print("my_height =", my_height)
print("is_student =", is_student)
print()

# Variable Naming Rules and Conventions
print("=== Variable Naming Rules ===")
print("Good variable names:")

# Good examples
first_name = "Alice"        # Use snake_case
last_name = "Johnson"       # Descriptive names
student_count = 25          # Clear meaning
total_score = 95.5          # Numbers allowed

print("first_name:", first_name)
print("last_name:", last_name)
print("student_count:", student_count)
print("total_score:", total_score)
print()

# Data Types in Detail
print("=== Data Types in Python ===")
print()

# 1. Integers (int) - Whole numbers
print("1. Integers (int):")
number_of_students = 30
year = 2024
temperature = -5

print("number_of_students =", number_of_students, "- Type:", type(number_of_students))
print("year =", year, "- Type:", type(year))
print("temperature =", temperature, "- Type:", type(temperature))
print()

# 2. Floats (float) - Decimal numbers
print("2. Floats (float):")
pi = 3.14159
price = 19.99
gpa = 3.85

print("pi =", pi, "- Type:", type(pi))
print("price =", price, "- Type:", type(price))
print("gpa =", gpa, "- Type:", type(gpa))
print()

# 3. Strings (str) - Text
print("3. Strings (str):")
greeting = "Hello, World!"
course_name = "Introduction to Programming"
favorite_color = "blue"

print("greeting =", greeting, "- Type:", type(greeting))
print("course_name =", course_name, "- Type:", type(course_name))
print("favorite_color =", favorite_color, "- Type:", type(favorite_color))
print()

# 4. Booleans (bool) - True or False
print("4. Booleans (bool):")
is_raining = False
has_homework = True
is_weekend = False

print("is_raining =", is_raining, "- Type:", type(is_raining))
print("has_homework =", has_homework, "- Type:", type(has_homework))
print("is_weekend =", is_weekend, "- Type:", type(is_weekend))
print()

# Variable Reassignment
print("=== Variable Reassignment ===")
score = 85
print("Original score:", score)

score = 92  # Reassigning a new value
print("New score:", score)

score = score + 5  # Using the variable in calculation
print("Score after bonus:", score)
print()

# Basic Arithmetic Operations
print("=== Arithmetic Operations ===")
num1 = 20
num2 = 8

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(f"num1 = {num1}, num2 = {num2}")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print()

# More arithmetic examples
print("More Arithmetic Examples:")
x = 15
y = 4

print(f"x = {x}, y = {y}")
print(f"Floor Division: {x} // {y} = {x // y}")  # Integer division
print(f"Modulus (remainder): {x} % {y} = {x % y}")
print(f"Exponentiation: {x} ** 2 = {x ** 2}")
print()

# String Concatenation
print("=== String Concatenation ===")
first = "Hello"
second = "World"
space = " "
exclamation = "!"

# Concatenating strings with +
message = first + space + second + exclamation
print("Concatenated message:", message)

# More string concatenation examples
name = "Alex"
age = 20
# Note: Can't directly concatenate string and number
# greeting_msg = "Hi, I'm " + name + " and I'm " + age + " years old"  # This would cause an error

# Convert number to string for concatenation
greeting_msg = "Hi, I'm " + name + " and I'm " + str(age) + " years old"
print("Greeting message:", greeting_msg)
print()

# Using f-strings (modern Python string formatting)
print("=== F-String Formatting (Modern Way) ===")
student_name = "Sarah"
student_grade = 95.5
student_passed = True

info = f"Student: {student_name}, Grade: {student_grade}, Passed: {student_passed}"
print("Student info:", info)
print()

# Practical Example: Simple Calculator Demonstration
print("=== Simple Calculator Example ===")
number_a = 12.5
number_b = 3.2

print(f"Calculator with numbers: {number_a} and {number_b}")
print(f"Sum: {number_a} + {number_b} = {number_a + number_b}")
print(f"Difference: {number_a} - {number_b} = {number_a - number_b}")
print(f"Product: {number_a} * {number_b} = {number_a * number_b}")
print(f"Quotient: {number_a} / {number_b} = {number_a / number_b}")
print()

print("=== End of Examples ===")
print("Remember:")
print("- Variables store data")
print("- Use descriptive names")
print("- Python has many data types")
print("- Practice arithmetic operations")
print("- String concatenation combines text")
