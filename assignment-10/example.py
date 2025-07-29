# Example.py - Lesson 10: Functions - Basics
# This file demonstrates function definition, calling, parameters, and return values

"""
Functions in Python

Functions are reusable blocks of code that perform specific tasks.
They help organize code, reduce repetition, and make programs more modular
and easier to understand and maintain.
"""

print("=== Introduction to Functions ===")
print()

# Basic function definition and calling
print("1. Basic Function Definition:")

def greet():
    """A simple function that prints a greeting."""
    print("Hello, welcome to Python functions!")

def say_goodbye():
    """A simple function that prints a goodbye message."""
    print("Goodbye! Thanks for learning functions!")

# Calling functions
print("Calling greet():")
greet()

print("\nCalling say_goodbye():")
say_goodbye()
print()

# Functions with parameters
print("=== Functions with Parameters ===")
print()

print("2. Functions with Single Parameter:")

def greet_person(name):
    """Greet a person by name."""
    print(f"Hello, {name}! Nice to meet you!")

def calculate_square(number):
    """Calculate the square of a number."""
    result = number * number
    print(f"The square of {number} is {result}")

# Calling functions with arguments
greet_person("Alice")
greet_person("Bob")
calculate_square(5)
calculate_square(8)
print()

print("3. Functions with Multiple Parameters:")

def add_numbers(a, b):
    """Add two numbers and print the result."""
    result = a + b
    print(f"{a} + {b} = {result}")

def introduce_person(name, age, city):
    """Introduce a person with their details."""
    print(f"This is {name}, who is {age} years old and lives in {city}.")

# Calling with multiple arguments
add_numbers(10, 5)
add_numbers(3.5, 2.8)
introduce_person("Carol", 25, "New York")
introduce_person("David", 30, "Los Angeles")
print()

# Functions with return values
print("=== Functions with Return Values ===")
print()

print("4. Functions that Return Values:")

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def get_full_name(first, last):
    """Combine first and last name and return the full name."""
    return f"{first} {last}"

def is_even(number):
    """Check if a number is even and return True or False."""
    return number % 2 == 0

# Using return values
product = multiply(6, 7)
print(f"Product: {product}")

full_name = get_full_name("John", "Smith")
print(f"Full name: {full_name}")

print(f"Is 8 even? {is_even(8)}")
print(f"Is 7 even? {is_even(7)}")
print()

print("5. Functions with Calculations:")

def calculate_area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    pi = 3.14159
    area = pi * radius * radius
    return area

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Using calculation functions
rect_area = calculate_area_rectangle(10, 5)
print(f"Rectangle area (10x5): {rect_area}")

circle_area = calculate_circle_area(3)
print(f"Circle area (radius 3): {circle_area:.2f}")

temp_celsius = fahrenheit_to_celsius(100)
print(f"100°F in Celsius: {temp_celsius:.1f}°C")
print()

# Variable scope
print("=== Variable Scope ===")
print()

print("6. Local vs Global Variables:")

# Global variable
global_counter = 0

def increment_local():
    """Function with local variable."""
    local_counter = 10
    local_counter += 1
    print(f"Local counter inside function: {local_counter}")

def increment_global():
    """Function that modifies global variable."""
    global global_counter
    global_counter += 1
    print(f"Global counter inside function: {global_counter}")

def show_scope_example(x):
    """Demonstrate variable scope."""
    y = x * 2  # Local variable
    print(f"Inside function - x: {x}, y: {y}")
    return y

print(f"Global counter before: {global_counter}")
increment_local()
increment_global()
print(f"Global counter after: {global_counter}")

result = show_scope_example(5)
print(f"Returned value: {result}")
# print(y)  # This would cause an error - y is not accessible here
print()

# Functions calling other functions
print("=== Functions Calling Other Functions ===")
print()

print("7. Function Composition:")

def get_username():
    """Get username from user input simulation."""
    return "student123"  # Simulated input

def validate_username(username):
    """Check if username is valid."""
    if len(username) >= 3 and username.isalnum():
        return True
    return False

def process_login():
    """Complete login process using other functions."""
    username = get_username()
    if validate_username(username):
        return f"Welcome, {username}!"
    else:
        return "Invalid username!"

login_result = process_login()
print(login_result)
print()

print("8. Mathematical Functions:")

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract second number from first."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide first number by second."""
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"

def calculate(num1, num2, operation):
    """Perform calculation based on operation."""
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == "divide":
        return divide(num1, num2)
    else:
        return "Unknown operation!"

# Using mathematical functions
print(f"5 + 3 = {calculate(5, 3, 'add')}")
print(f"10 - 4 = {calculate(10, 4, 'subtract')}")
print(f"6 * 7 = {calculate(6, 7, 'multiply')}")
print(f"15 / 3 = {calculate(15, 3, 'divide')}")
print()

# Functions with validation
print("=== Functions with Input Validation ===")
print()

print("9. Input Validation Functions:")

def is_positive_number(num):
    """Check if a number is positive."""
    return num > 0

def get_valid_age(age_input):
    """Validate and return age if valid."""
    try:
        age = int(age_input)
        if 0 <= age <= 150:
            return age
        else:
            return None
    except ValueError:
        return None

def calculate_grade_average(grades):
    """Calculate average of grades with validation."""
    if not grades:  # Empty list
        return 0
    
    valid_grades = []
    for grade in grades:
        if 0 <= grade <= 100:
            valid_grades.append(grade)
    
    if valid_grades:
        return sum(valid_grades) / len(valid_grades)
    else:
        return 0

# Testing validation functions
print(f"Is 5 positive? {is_positive_number(5)}")
print(f"Is -3 positive? {is_positive_number(-3)}")

valid_age = get_valid_age("25")
print(f"Valid age from '25': {valid_age}")

invalid_age = get_valid_age("abc")
print(f"Valid age from 'abc': {invalid_age}")

grades = [85, 92, 78, 95, 88]
average = calculate_grade_average(grades)
print(f"Grade average: {average:.1f}")
print()

# Practical examples
print("=== Practical Function Examples ===")
print()

print("10. Utility Functions:")

def format_currency(amount):
    """Format a number as currency."""
    return f"${amount:.2f}"

def calculate_tip(bill_amount, tip_percentage):
    """Calculate tip amount."""
    tip = bill_amount * (tip_percentage / 100)
    return tip

def calculate_total_with_tip(bill_amount, tip_percentage):
    """Calculate total bill including tip."""
    tip = calculate_tip(bill_amount, tip_percentage)
    total = bill_amount + tip
    return total

def generate_receipt(bill_amount, tip_percentage):
    """Generate a formatted receipt."""
    tip = calculate_tip(bill_amount, tip_percentage)
    total = calculate_total_with_tip(bill_amount, tip_percentage)
    
    receipt = f"""
    === RECEIPT ===
    Bill Amount: {format_currency(bill_amount)}
    Tip ({tip_percentage}%): {format_currency(tip)}
    Total: {format_currency(total)}
    ===============
    """
    return receipt

# Using utility functions
bill = 50.00
tip_percent = 18

receipt = generate_receipt(bill, tip_percent)
print(receipt)

print("11. Text Processing Functions:")

def count_words(text):
    """Count the number of words in text."""
    words = text.split()
    return len(words)

def count_vowels(text):
    """Count vowels in text."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def reverse_text(text):
    """Reverse the given text."""
    return text[::-1]

def analyze_text(text):
    """Analyze text and return statistics."""
    word_count = count_words(text)
    vowel_count = count_vowels(text)
    char_count = len(text)
    
    return {
        'words': word_count,
        'vowels': vowel_count,
        'characters': char_count,
        'reversed': reverse_text(text)
    }

# Testing text functions
sample_text = "Python programming is fun and powerful"
analysis = analyze_text(sample_text)

print(f"Text: '{sample_text}'")
print(f"Words: {analysis['words']}")
print(f"Vowels: {analysis['vowels']}")
print(f"Characters: {analysis['characters']}")
print(f"Reversed: '{analysis['reversed']}'")
print()

# Function documentation
print("12. Function Documentation:")

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).
    
    Parameters:
    weight_kg (float): Weight in kilograms
    height_m (float): Height in meters
    
    Returns:
    float: BMI value
    
    Example:
    >>> bmi = calculate_bmi(70, 1.75)
    >>> print(f"BMI: {bmi:.1f}")
    BMI: 22.9
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    Determine BMI category based on value.
    
    Parameters:
    bmi (float): BMI value
    
    Returns:
    str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Using documented functions
weight = 70  # kg
height = 1.75  # meters

bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

print(f"Weight: {weight} kg, Height: {height} m")
print(f"BMI: {bmi:.1f} ({category})")
print()

print("=== End of Examples ===")
print("Key Points to Remember:")
print("- Functions are defined with 'def' keyword")
print("- Use parameters to pass data into functions")
print("- Use 'return' to send data back from functions")
print("- Variables inside functions are local by default")
print("- Functions help organize and reuse code")
print("- Good function names describe what they do")
print("- Document your functions with docstrings")
print("- Test functions with different inputs")
