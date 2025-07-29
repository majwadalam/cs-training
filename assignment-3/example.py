# Example.py - Lesson 3: Getting User Input
# This file demonstrates user input, type conversion, and interactive programs

"""
Getting User Input in Python

The input() function allows us to get information from users.
It always returns a string, so we need to convert it to other types when needed.
"""

print("=== Introduction to User Input ===")
print()

# Basic input() function
print("1. Basic Input Example:")
user_name = input("What is your name? ")
print("Hello,", user_name + "!")
print("Type of input:", type(user_name))  # Always returns string
print()

# Getting different types of input
print("=== Type Conversion Examples ===")
print()

# Getting a string (no conversion needed)
print("2. String Input:")
favorite_color = input("What is your favorite color? ")
print(f"Your favorite color is {favorite_color}")
print(f"Type: {type(favorite_color)}")
print()

# Getting an integer
print("3. Integer Input (with conversion):")
age_str = input("How old are you? ")
age = int(age_str)  # Convert string to integer
print(f"You are {age} years old")
print(f"Type: {type(age)}")
print(f"Next year you will be {age + 1}")
print()

# Shorter way to get integer input
print("4. Direct Integer Conversion:")
siblings = int(input("How many siblings do you have? "))
print(f"You have {siblings} siblings")
print(f"Type: {type(siblings)}")
print()

# Getting a float
print("5. Float Input (with conversion):")
height = float(input("What is your height in feet? "))
print(f"Your height is {height} feet")
print(f"Type: {type(height)}")
print(f"Your height in inches is approximately {height * 12}")
print()

# Multiple inputs in sequence
print("=== Interactive Program Example ===")
print("Let's create a simple profile!")
print()

# Collect information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
gpa = float(input("Enter your GPA: "))
is_student = input("Are you currently a student? (yes/no): ")

# Calculate age (simplified)
current_year = 2024
calculated_age = current_year - birth_year

# Display formatted summary
print()
print("=== Your Profile Summary ===")
print(f"Full Name: {first_name} {last_name}")
print(f"Age: {calculated_age} years old")
print(f"GPA: {gpa}")
print(f"Student Status: {is_student}")
print()

# Working with boolean-like input
print("=== Boolean Input Handling ===")
likes_pizza = input("Do you like pizza? (yes/no): ")

# Convert text to boolean logic
if likes_pizza.lower() == "yes":
    pizza_preference = True
else:
    pizza_preference = False

print(f"Likes pizza: {pizza_preference}")
print()

# Input validation examples
print("=== Input Validation Examples ===")
print()

# Simple validation for numbers
print("Example: Getting a valid number")
try:
    score = int(input("Enter your test score (0-100): "))
    print(f"Your score is: {score}")
except ValueError:
    print("Error: Please enter a valid number!")
print()

# Input with instructions
print("Example: Clear instructions for users")
phone = input("Enter your phone number (format: xxx-xxx-xxxx): ")
email = input("Enter your email address: ")

print(f"Contact Info:")
print(f"Phone: {phone}")
print(f"Email: {email}")
print()

# Multiple choice input
print("=== Multiple Choice Input ===")
print("Choose your favorite subject:")
print("1. Math")
print("2. Science")
print("3. English")
print("4. History")

choice = input("Enter your choice (1-4): ")
subjects = ["Math", "Science", "English", "History"]

try:
    choice_num = int(choice)
    if 1 <= choice_num <= 4:
        selected_subject = subjects[choice_num - 1]
        print(f"You chose: {selected_subject}")
    else:
        print("Please choose a number between 1 and 4")
except ValueError:
    print("Please enter a valid number")
print()

# String input with formatting
print("=== String Input with Formatting ===")
quote = input("Enter your favorite quote: ")
author = input("Who said this quote? ")

print()
print("Your Quote:")
print(f'"{quote}"')
print(f"- {author}")
print()

# Advanced input example
print("=== Advanced Interactive Example ===")
print("Let's calculate your BMI!")

weight = float(input("Enter your weight in pounds: "))
height_feet = int(input("Enter your height in feet: "))
height_inches = int(input("Enter additional inches: "))

# Convert to total inches and then to meters
total_inches = (height_feet * 12) + height_inches
height_meters = total_inches * 0.0254
weight_kg = weight * 0.453592

# Calculate BMI
bmi = weight_kg / (height_meters ** 2)

print(f"\nYour BMI Calculation:")
print(f"Weight: {weight} lbs ({weight_kg:.1f} kg)")
print(f"Height: {height_feet}'{height_inches}\" ({total_inches} inches, {height_meters:.2f} m)")
print(f"BMI: {bmi:.1f}")
print()

print("=== End of Examples ===")
print("Key Points to Remember:")
print("- input() always returns a string")
print("- Use int() to convert to whole numbers")
print("- Use float() to convert to decimal numbers")
print("- Always give clear instructions to users")
print("- Consider validating user input")
print("- Make your programs interactive and user-friendly")
