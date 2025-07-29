# Assignment.py - Lesson 5: Number Guessing Game with While Loops
# Student Name: [Write your name here]
# Date: [Write today's date here]

"""
Assignment: Build a number guessing game where the computer picks a random 
number and the user has to guess it, with hints after each guess.

Requirements:
1. Generate a random number between 1 and 100
2. Use a while loop to keep asking for guesses until correct
3. Provide "higher" or "lower" hints after each incorrect guess
4. Count and display the number of attempts
5. Include input validation (handle non-numeric input)
6. Congratulate the user when they win
7. Ask if they want to play again (another while loop)
8. Use break and/or continue statements appropriately
9. Add comments explaining your loop logic

Example Output:
=== Number Guessing Game ===
I'm thinking of a number between 1 and 100.
Can you guess what it is?

Attempt 1: Enter your guess: 50
Too high! Try a lower number.

Attempt 2: Enter your guess: 25
Too low! Try a higher number.

Attempt 3: Enter your guess: 37
Too low! Try a higher number.

Attempt 4: Enter your guess: 43
Congratulations! You guessed it!
The number was 43 and it took you 4 attempts.

Would you like to play again? (yes/no): no
Thanks for playing!
"""

# Import random module for generating random numbers
import random

# TODO: Write your number guessing game below
# Remember to use while loops, input validation, and clear feedback!

print("=== Number Guessing Game ===")
print("Welcome to the Number Guessing Game!")
print()

# TODO: Main game loop (for playing multiple rounds)
# Use a while loop to allow multiple games

    # TODO: Game setup
    # Generate random number between 1 and 100
    # Initialize variables (attempts, guessed correctly flag, etc.)
    
    # TODO: Display game instructions
    
    # TODO: Main guessing loop
    # Use while loop to keep asking for guesses until correct
    
        # TODO: Get user input with validation
        # Handle non-numeric input using try/except
        
        # TODO: Check the guess
        # Provide feedback (higher/lower/correct)
        # Update attempt counter
        
        # TODO: Handle correct guess
        # Break out of loop when correct
        
    # TODO: Display final results
    # Show number of attempts and congratulate
    
    # TODO: Ask to play again
    # Get user input for another round

# TODO: End game message

# Start your code here:

# Hint: Structure your code like this:
# play_again = "yes"
# while play_again.lower() == "yes":
#     # Game setup
#     secret_number = random.randint(1, 100)
#     attempts = 0
#     guessed_correctly = False
#     
#     # Game instructions
#     print("I'm thinking of a number between 1 and 100.")
#     
#     # Main guessing loop
#     while not guessed_correctly:
#         # Your guessing logic here
#         pass
#     
#     # Ask to play again
#     play_again = input("Would you like to play again? (yes/no): ")
