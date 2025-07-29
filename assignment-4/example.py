# Example.py - Lesson 4: Conditional Statements (if, elif, else)
# This file demonstrates decision-making in programs using conditional statements

"""
Conditional Statements in Python

Conditional statements allow programs to make decisions and execute 
different code based on different conditions. This is fundamental 
to creating intelligent, responsive programs.
"""

print("=== Introduction to Conditional Statements ===")
print()

# Basic if statement
print("1. Basic if Statement:")
age = 18

if age >= 18:
    print("You are an adult!")

print(f"Your age: {age}")
print()

# if-else statement
print("2. if-else Statement:")
temperature = 75

if temperature > 80:
    print("It's hot outside!")
else:
    print("It's not too hot outside.")

print(f"Temperature: {temperature}°F")
print()

# Comparison Operators
print("=== Comparison Operators ===")
print()

score = 85
passing_score = 70

print(f"Your score: {score}")
print(f"Passing score: {passing_score}")
print()

# Different comparison operators
print("Comparison Results:")
print(f"{score} == {passing_score}: {score == passing_score}")  # Equal to
print(f"{score} != {passing_score}: {score != passing_score}")  # Not equal to
print(f"{score} > {passing_score}: {score > passing_score}")    # Greater than
print(f"{score} < {passing_score}: {score < passing_score}")    # Less than
print(f"{score} >= {passing_score}: {score >= passing_score}")  # Greater than or equal
print(f"{score} <= {passing_score}: {score <= passing_score}")  # Less than or equal
print()

# if-elif-else statement
print("=== if-elif-else Statements ===")
print()

grade = 87

print(f"Numerical grade: {grade}")

if grade >= 90:
    letter_grade = "A"
    message = "Excellent work!"
elif grade >= 80:
    letter_grade = "B" 
    message = "Good job!"
elif grade >= 70:
    letter_grade = "C"
    message = "Satisfactory work."
elif grade >= 60:
    letter_grade = "D"
    message = "Below average. Study harder!"
else:
    letter_grade = "F"
    message = "Failing grade. See instructor."

print(f"Letter grade: {letter_grade}")
print(f"Feedback: {message}")
print()

# Logical Operators
print("=== Logical Operators ===")
print()

# AND operator
print("4. AND Operator:")
has_license = True
has_car = True

if has_license and has_car:
    print("You can drive!")
else:
    print("You cannot drive yet.")

print(f"Has license: {has_license}, Has car: {has_car}")
print()

# OR operator
print("5. OR Operator:")
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You don't have to work today!")
else:
    print("It's a work day.")

print(f"Weekend: {is_weekend}, Holiday: {is_holiday}")
print()

# NOT operator
print("6. NOT Operator:")
is_raining = False

if not is_raining:
    print("Great weather for a walk!")
else:
    print("Better stay inside.")

print(f"Is raining: {is_raining}")
print()

# Complex logical expressions
print("7. Complex Logical Expressions:")
age = 20
has_id = True
is_student = True

# Multiple conditions
if (age >= 18 and has_id) or is_student:
    print("You can enter the venue!")
else:
    print("Sorry, you cannot enter.")

print(f"Age: {age}, Has ID: {has_id}, Student: {is_student}")
print()

# Nested if statements
print("=== Nested if Statements ===")
print()

weather = "sunny"
temperature = 78

print(f"Weather: {weather}, Temperature: {temperature}°F")

if weather == "sunny":
    print("It's a sunny day!")
    if temperature > 75:
        print("Perfect weather for outdoor activities!")
        if temperature > 85:
            print("Remember to stay hydrated!")
        else:
            print("Comfortable temperature for activities.")
    else:
        print("A bit cool, but still nice!")
else:
    print("Weather conditions are different.")
print()

# String comparisons
print("=== String Comparisons ===")
print()

user_input = "yes"
user_input_lower = user_input.lower()  # Convert to lowercase for comparison

if user_input_lower == "yes" or user_input_lower == "y":
    print("You agreed!")
elif user_input_lower == "no" or user_input_lower == "n":
    print("You declined.")
else:
    print("Please answer yes or no.")

print(f"User input: '{user_input}'")
print()

# Number range checking
print("=== Number Range Checking ===")
print()

test_score = 76

print(f"Test score: {test_score}")

# Check multiple ranges
if 90 <= test_score <= 100:
    grade_level = "Excellent (A)"
elif 80 <= test_score < 90:
    grade_level = "Good (B)"
elif 70 <= test_score < 80:
    grade_level = "Average (C)"
elif 60 <= test_score < 70:
    grade_level = "Below Average (D)"
elif 0 <= test_score < 60:
    grade_level = "Failing (F)"
else:
    grade_level = "Invalid score"

print(f"Grade level: {grade_level}")
print()

# Interactive example with user input
print("=== Interactive Decision Making ===")
print()

# Simulate user input for demonstration
user_age = 19
user_grade = 88

print(f"Simulated input - Age: {user_age}, Grade: {user_grade}")

# Age-based decisions
if user_age < 13:
    category = "Child"
elif user_age < 18:
    category = "Teenager" 
elif user_age < 65:
    category = "Adult"
else:
    category = "Senior"

# Grade-based decisions with nested conditions
if user_grade >= 90:
    achievement = "Honor Roll"
    if user_grade >= 97:
        achievement = "High Honor Roll"
elif user_grade >= 80:
    achievement = "Good Standing"
else:
    achievement = "Needs Improvement"

print(f"Category: {achievement} {category}")
print()

# Boolean variable usage
print("=== Boolean Variables in Conditions ===")
print()

is_enrolled = True
is_full_time = False
has_prerequisites = True

# Using boolean variables directly
if is_enrolled:
    print("Student is enrolled.")
    
    if is_full_time:
        print("Full-time student benefits apply.")
    else:
        print("Part-time student status.")
    
    if has_prerequisites:
        print("Can register for advanced courses.")
    else:
        print("Must complete prerequisites first.")

print(f"Enrolled: {is_enrolled}, Full-time: {is_full_time}, Prerequisites: {has_prerequisites}")
print()

print("=== End of Examples ===")
print("Key Points to Remember:")
print("- Use if for the first condition")
print("- Use elif for additional conditions")
print("- Use else for when all conditions are false")
print("- Comparison operators: ==, !=, <, >, <=, >=")
print("- Logical operators: and, or, not")
print("- Nested if statements for complex decisions")
print("- Indentation is crucial in Python!")
