# Assignment.py - Lesson 10: Utility Functions Library
# Student Name: [Write your name here]
# Date: [Write today's date here]

"""
Assignment: Create a library of utility functions (temperature converter, 
area calculator, password validator) and a menu system to use them.

Requirements:
1. Create utility functions for:
   - Temperature conversions (Celsius/Fahrenheit/Kelvin)
   - Area calculations (rectangle, circle, triangle, square)
   - Password validation and strength checking
2. Each function should:
   - Have clear parameters and return values
   - Include input validation
   - Have descriptive names and documentation
   - Handle edge cases appropriately
3. Create a menu-driven interface to test all functions
4. Use proper variable scope (local vs global)
5. Include error handling for invalid inputs
6. Demonstrate function composition (functions calling other functions)

Example Output:
=== Utility Functions Library ===
Welcome to the Python Utility Library!

Main Menu:
1. Temperature Converter
2. Area Calculator  
3. Password Validator
4. Quit

Choose an option (1-4): 1

=== Temperature Converter ===
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Back to main menu

Choose conversion (1-5): 1
Enter temperature in Celsius: 25
25.0°C = 77.0°F

Choose conversion (1-5): 5
[Returns to main menu...]
"""

# TODO: Write your utility functions library below

print("=== Utility Functions Library ===")
print("Welcome to the Python Utility Library!")
print()

# TODO: Temperature Conversion Functions

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius
    
    Returns:
    float: Temperature in Fahrenheit
    """
    # Formula: F = (C × 9/5) + 32
    # return (celsius * 9/5) + 32
    pass

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
    float: Temperature in Celsius
    """
    # Formula: C = (F - 32) × 5/9
    # return (fahrenheit - 32) * 5/9
    pass

def celsius_to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.
    
    Parameters:
    celsius (float): Temperature in Celsius
    
    Returns:
    float: Temperature in Kelvin
    """
    # Formula: K = C + 273.15
    # return celsius + 273.15
    pass

def kelvin_to_celsius(kelvin):
    """
    Convert Kelvin to Celsius.
    
    Parameters:
    kelvin (float): Temperature in Kelvin
    
    Returns:
    float: Temperature in Celsius
    """
    # Formula: C = K - 273.15
    # return kelvin - 273.15
    pass

def validate_temperature(temp, unit):
    """
    Validate temperature based on unit.
    
    Parameters:
    temp (float): Temperature value
    unit (str): Temperature unit ('C', 'F', 'K')
    
    Returns:
    bool: True if valid, False otherwise
    """
    # Check for absolute zero limits
    # Celsius: >= -273.15
    # Fahrenheit: >= -459.67
    # Kelvin: >= 0
    pass

# TODO: Area Calculation Functions

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): Length of rectangle
    width (float): Width of rectangle
    
    Returns:
    float: Area of rectangle
    """
    # Formula: Area = length × width
    # return length * width
    pass

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
    radius (float): Radius of circle
    
    Returns:
    float: Area of circle
    """
    # Formula: Area = π × radius²
    # pi = 3.14159
    # return pi * radius * radius
    pass

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.
    
    Parameters:
    base (float): Base of triangle
    height (float): Height of triangle
    
    Returns:
    float: Area of triangle
    """
    # Formula: Area = (base × height) / 2
    # return (base * height) / 2
    pass

def calculate_square_area(side):
    """
    Calculate the area of a square.
    
    Parameters:
    side (float): Side length of square
    
    Returns:
    float: Area of square
    """
    # Formula: Area = side²
    # return side * side
    pass

def validate_dimensions(dimensions):
    """
    Validate that all dimensions are positive.
    
    Parameters:
    dimensions (list): List of dimension values
    
    Returns:
    bool: True if all positive, False otherwise
    """
    # Check that all values are positive numbers
    pass

# TODO: Password Validation Functions

def check_password_length(password, min_length=8):
    """
    Check if password meets minimum length requirement.
    
    Parameters:
    password (str): Password to check
    min_length (int): Minimum required length
    
    Returns:
    bool: True if meets requirement, False otherwise
    """
    # return len(password) >= min_length
    pass

def check_password_uppercase(password):
    """
    Check if password contains uppercase letters.
    
    Parameters:
    password (str): Password to check
    
    Returns:
    bool: True if contains uppercase, False otherwise
    """
    # Check if any character is uppercase
    pass

def check_password_lowercase(password):
    """
    Check if password contains lowercase letters.
    
    Parameters:
    password (str): Password to check
    
    Returns:
    bool: True if contains lowercase, False otherwise
    """
    # Check if any character is lowercase
    pass

def check_password_digits(password):
    """
    Check if password contains digits.
    
    Parameters:
    password (str): Password to check
    
    Returns:
    bool: True if contains digits, False otherwise
    """
    # Check if any character is a digit
    pass

def check_password_special_chars(password):
    """
    Check if password contains special characters.
    
    Parameters:
    password (str): Password to check
    
    Returns:
    bool: True if contains special chars, False otherwise
    """
    # special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    # Check if any character is in special_chars
    pass

def calculate_password_strength(password):
    """
    Calculate overall password strength score.
    
    Parameters:
    password (str): Password to evaluate
    
    Returns:
    dict: Dictionary with score and feedback
    """
    # score = 0
    # feedback = []
    # 
    # # Check each requirement and add to score
    # if check_password_length(password):
    #     score += 1
    # else:
    #     feedback.append("Use at least 8 characters")
    # 
    # # Continue for other checks...
    # 
    # # Determine strength level
    # if score >= 4:
    #     strength = "Strong"
    # elif score >= 3:
    #     strength = "Medium"
    # elif score >= 2:
    #     strength = "Weak"
    # else:
    #     strength = "Very Weak"
    # 
    # return {
    #     'score': score,
    #     'strength': strength,
    #     'feedback': feedback
    # }
    pass

# TODO: Menu System Functions

def display_main_menu():
    """Display the main menu options."""
    # print("\nMain Menu:")
    # print("1. Temperature Converter")
    # print("2. Area Calculator")
    # print("3. Password Validator")
    # print("4. Quit")
    pass

def temperature_converter_menu():
    """Handle temperature converter submenu."""
    # while True:
    #     print("\n=== Temperature Converter ===")
    #     print("1. Celsius to Fahrenheit")
    #     print("2. Fahrenheit to Celsius")
    #     print("3. Celsius to Kelvin")
    #     print("4. Kelvin to Celsius")
    #     print("5. Back to main menu")
    #     
    #     choice = input("\nChoose conversion (1-5): ").strip()
    #     
    #     if choice == "1":
    #         # Get input and convert C to F
    #     elif choice == "2":
    #         # Get input and convert F to C
    #     # ... handle other choices
    #     elif choice == "5":
    #         break
    #     else:
    #         print("Invalid choice!")
    pass

def area_calculator_menu():
    """Handle area calculator submenu."""
    # Similar structure to temperature menu
    pass

def password_validator_menu():
    """Handle password validator submenu."""
    # Get password input and show strength analysis
    pass

def get_float_input(prompt):
    """
    Get valid float input from user.
    
    Parameters:
    prompt (str): Input prompt message
    
    Returns:
    float: Valid float value or None if cancelled
    """
    # while True:
    #     try:
    #         value = float(input(prompt))
    #         return value
    #     except ValueError:
    #         print("Please enter a valid number!")
    #         retry = input("Try again? (y/n): ").lower()
    #         if retry != 'y':
    #             return None
    pass

def main():
    """Main program function."""
    # while True:
    #     display_main_menu()
    #     choice = input("\nChoose an option (1-4): ").strip()
    #     
    #     if choice == "1":
    #         temperature_converter_menu()
    #     elif choice == "2":
    #         area_calculator_menu()
    #     elif choice == "3":
    #         password_validator_menu()
    #     elif choice == "4":
    #         print("Thank you for using the Utility Library!")
    #         break
    #     else:
    #         print("Invalid choice! Please choose 1-4.")
    pass

# Start your code here:

# Example structure to get you started:
# def celsius_to_fahrenheit(celsius):
#     """Convert Celsius to Fahrenheit."""
#     return (celsius * 9/5) + 32
# 
# def main():
#     """Main program function."""
#     while True:
#         print("\nMain Menu:")
#         print("1. Temperature Converter")
#         print("2. Area Calculator")
#         print("3. Password Validator")
#         print("4. Quit")
#         
#         choice = input("\nChoose an option (1-4): ").strip()
#         
#         if choice == "1":
#             try:
#                 temp = float(input("Enter temperature in Celsius: "))
#                 result = celsius_to_fahrenheit(temp)
#                 print(f"{temp}°C = {result:.1f}°F")
#             except ValueError:
#                 print("Invalid input! Please enter a number.")
#         
#         elif choice == "4":
#             print("Thank you for using the Utility Library!")
#             break
#         
#         else:
#             print("Invalid choice! Please choose 1-4.")
# 
# # Run the program
# if __name__ == "__main__":
#     main()
