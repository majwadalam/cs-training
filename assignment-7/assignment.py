# Assignment.py - Lesson 7: Text Analyzer with String Methods
# Student Name: [Write your name here]
# Date: [Write today's date here]

"""
Assignment: Build a text analyzer that counts words, characters, and performs 
various text transformations on user input.

Requirements:
1. Get text input from the user
2. Perform comprehensive text analysis including:
   - Character count (with and without spaces)
   - Word count and sentence count
   - Character frequency analysis
   - Vowel and consonant counting
3. Text transformations:
   - Convert to uppercase, lowercase, title case
   - Remove extra whitespace
   - Replace specific words or characters
4. Text properties checking:
   - Check for digits, alphabetic characters
   - Find longest and shortest words
   - Identify common words
5. Display results in a formatted report
6. Use multiple string methods and techniques
7. Include proper error handling

Example Output:
=== Text Analyzer ===
Enter your text to analyze: The quick brown fox jumps over the lazy dog!

=== Text Analysis Report ===
Original Text: "The quick brown fox jumps over the lazy dog!"

Basic Statistics:
- Total characters: 44
- Characters (no spaces): 35
- Words: 9
- Sentences: 1
- Average word length: 3.9

Character Analysis:
- Vowels: 12
- Consonants: 23
- Digits: 0
- Punctuation: 1

Text Transformations:
- Uppercase: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG!
- Lowercase: the quick brown fox jumps over the lazy dog!
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog!

Word Analysis:
- Longest word: "quick" (5 letters)
- Shortest word: "the" (3 letters)
- Most common word: "the" (appears 2 times)

=== End of Analysis ===
"""

# TODO: Write your text analyzer below
# Remember to use string methods, indexing, slicing, and loops!

print("=== Text Analyzer ===")
print("Welcome to the Text Analyzer!")
print("This program will analyze any text you provide.")
print()

# TODO: Main program loop
# while True:
    # TODO: Get text input from user
    # text = input("Enter your text to analyze (or 'quit' to exit): ")
    
    # TODO: Check for exit condition
    # if text.lower() == 'quit':
    #     break
    
    # TODO: Basic text statistics
    # Calculate total characters, characters without spaces, words, sentences
    
    # TODO: Character analysis
    # Count vowels, consonants, digits, punctuation
    # Create character frequency dictionary
    
    # TODO: Text transformations
    # Show uppercase, lowercase, title case versions
    # Clean up extra whitespace
    
    # TODO: Word analysis
    # Find longest and shortest words
    # Count word frequencies
    # Identify most common words
    
    # TODO: Display formatted report
    # Use f-strings and proper formatting

# TODO: Functions to help organize your code

def count_vowels_consonants(text):
    """Count vowels and consonants in text"""
    # vowels = "aeiouAEIOU"
    # vowel_count = 0
    # consonant_count = 0
    # for char in text:
    #     if char.isalpha():
    #         if char in vowels:
    #             vowel_count += 1
    #         else:
    #             consonant_count += 1
    # return vowel_count, consonant_count
    pass

def get_word_stats(text):
    """Get statistics about words in the text"""
    # words = text.split()
    # if not words:
    #     return None, None, {}
    # 
    # # Find longest and shortest words
    # longest = max(words, key=len)
    # shortest = min(words, key=len)
    # 
    # # Count word frequencies
    # word_freq = {}
    # for word in words:
    #     clean_word = word.lower().strip('.,!?;:"')
    #     word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
    # 
    # return longest, shortest, word_freq
    pass

def analyze_characters(text):
    """Analyze character types in text"""
    # char_freq = {}
    # digits = 0
    # punctuation = 0
    # 
    # for char in text:
    #     char_freq[char] = char_freq.get(char, 0) + 1
    #     if char.isdigit():
    #         digits += 1
    #     elif not char.isalnum() and not char.isspace():
    #         punctuation += 1
    # 
    # return char_freq, digits, punctuation
    pass

# Start your code here:

# Basic structure example:
# while True:
#     user_text = input("\nEnter your text to analyze (or 'quit' to exit): ")
#     
#     if user_text.lower().strip() == 'quit':
#         print("Thank you for using the Text Analyzer!")
#         break
#     
#     if not user_text.strip():
#         print("Please enter some text to analyze.")
#         continue
#     
#     print(f"\n=== Text Analysis Report ===")
#     print(f'Original Text: "{user_text}"')
#     print()
#     
#     # Basic statistics
#     total_chars = len(user_text)
#     chars_no_spaces = len(user_text.replace(' ', ''))
#     words = user_text.split()
#     word_count = len(words)
#     sentence_count = user_text.count('.') + user_text.count('!') + user_text.count('?')
#     
#     print("Basic Statistics:")
#     print(f"- Total characters: {total_chars}")
#     print(f"- Characters (no spaces): {chars_no_spaces}")
#     print(f"- Words: {word_count}")
#     print(f"- Sentences: {sentence_count}")
#     if word_count > 0:
#         avg_word_length = chars_no_spaces / word_count
#         print(f"- Average word length: {avg_word_length:.1f}")
#     print()
#     
#     # Continue with more analysis...
