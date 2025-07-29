# Example.py - Lesson 5: Loops - While Loops
# This file demonstrates repetition in programming using while loops

"""
While Loops in Python

While loops allow us to repeat code as long as a condition is true.
They are essential for creating programs that can handle repetitive tasks
and continue running until a specific goal is achieved.
"""

import random  # We'll use this for generating random numbers

print("=== Introduction to While Loops ===")
print()

# Basic while loop
print("1. Basic While Loop:")
count = 1

while count <= 5:
    print(f"Count: {count}")
    count = count + 1  # Important: update the variable to avoid infinite loop

print("Loop finished!")
print()

# While loop with user input
print("2. While Loop with User Input:")
user_input = ""

while user_input != "quit":
    user_input = input("Type 'quit' to exit, or anything else to continue: ")
    if user_input != "quit":
        print(f"You typed: {user_input}")

print("You chose to quit!")
print()

# Input validation with while loop
print("=== Input Validation with While Loops ===")
print()

print("3. Getting a Valid Number:")
valid_number = False

while not valid_number:
    try:
        age = int(input("Enter your age (must be a number): "))
        if age < 0:
            print("Age cannot be negative. Please try again.")
        elif age > 150:
            print("Age seems too high. Please try again.")
        else:
            valid_number = True
            print(f"Thank you! Your age is {age}")
    except ValueError:
        print("That's not a valid number. Please try again.")

print()

# While loop with range checking
print("4. Range Validation:")
score = -1  # Initialize with invalid value

while score < 0 or score > 100:
    try:
        score = float(input("Enter a score between 0 and 100: "))
        if score < 0 or score > 100:
            print("Score must be between 0 and 100. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

print(f"Valid score entered: {score}")
print()

# Using break statement
print("=== Break Statement ===")
print()

print("5. Using break to exit early:")
counter = 1

while True:  # Infinite loop condition
    print(f"Counter: {counter}")
    counter += 1
    
    if counter > 5:
        print("Breaking out of loop!")
        break  # Exit the loop immediately

print("Loop ended with break.")
print()

# Using continue statement
print("6. Using continue to skip iterations:")
number = 0

while number < 10:
    number += 1
    
    if number % 2 == 0:  # If number is even
        continue  # Skip the rest of this iteration
    
    print(f"Odd number: {number}")

print("Finished printing odd numbers.")
print()

# Practical example: Simple menu system
print("=== Practical Example: Menu System ===")
print()

menu_choice = ""

while menu_choice != "4":
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Quit")
    
    menu_choice = input("Choose an option (1-4): ")
    
    if menu_choice == "1":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f"Result: {a + b}")
    elif menu_choice == "2":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f"Result: {a - b}")
    elif menu_choice == "3":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f"Result: {a * b}")
    elif menu_choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")

print()

# Number guessing game example
print("=== Number Guessing Game Example ===")
print()

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
guess = 0
attempts = 0
max_attempts = 5

print("I'm thinking of a number between 1 and 10.")
print(f"You have {max_attempts} attempts to guess it!")

while guess != secret_number and attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
            
        if attempts == max_attempts and guess != secret_number:
            print(f"Game over! The number was {secret_number}.")
            
    except ValueError:
        print("Please enter a valid number.")

print()

# Accumulator pattern with while loop
print("=== Accumulator Pattern ===")
print()

print("7. Sum of numbers from 1 to 10:")
total = 0
current = 1

while current <= 10:
    total += current  # Add current number to total
    current += 1      # Move to next number

print(f"Sum of 1 to 10: {total}")
print()

# Countdown example
print("8. Countdown Example:")
countdown = 5

while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
    
print("Blast off! 🚀")
print()

# While loop with multiple conditions
print("=== Multiple Conditions ===")
print()

print("9. Login Simulation:")
attempts = 0
max_login_attempts = 3
logged_in = False

while attempts < max_login_attempts and not logged_in:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == "admin" and password == "password123":
        logged_in = True
        print("Login successful!")
    else:
        attempts += 1
        remaining = max_login_attempts - attempts
        if remaining > 0:
            print(f"Invalid credentials. {remaining} attempts remaining.")
        else:
            print("Too many failed attempts. Account locked.")

print()

# Nested while loops (simple example)
print("10. Nested While Loops:")
outer = 1

while outer <= 3:
    print(f"Outer loop: {outer}")
    inner = 1
    
    while inner <= 3:
        print(f"  Inner loop: {inner}")
        inner += 1
    
    outer += 1

print()

print("=== End of Examples ===")
print("Key Points to Remember:")
print("- While loops repeat as long as the condition is True")
print("- Always update variables to avoid infinite loops")
print("- Use break to exit loops early")
print("- Use continue to skip iterations")
print("- While loops are great for input validation")
print("- Be careful with loop conditions")
print("- Test your loops with different inputs")
