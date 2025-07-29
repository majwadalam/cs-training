# Example.py - Lesson 7: Strings and String Methods
# This file demonstrates string manipulation and methods in Python

"""
Strings in Python

Strings are sequences of characters. They are one of the most commonly used
data types in programming. Python provides many built-in methods to work
with strings effectively.
"""

print("=== Introduction to Strings ===")
print()

# Basic string creation
print("1. Creating Strings:")
message = "Hello, World!"
name = 'Alice'
paragraph = """This is a 
multi-line string
that spans several lines."""

print(f"Single quotes: {name}")
print(f"Double quotes: {message}")
print(f"Triple quotes:\n{paragraph}")
print()

# String indexing
print("=== String Indexing ===")
print()

text = "Python Programming"
print(f"Original string: '{text}'")
print(f"Length: {len(text)}")
print()

print("2. Accessing individual characters:")
print(f"First character: text[0] = '{text[0]}'")
print(f"Second character: text[1] = '{text[1]}'")
print(f"Last character: text[-1] = '{text[-1]}'")
print(f"Second to last: text[-2] = '{text[-2]}'")
print()

print("3. Iterating through characters:")
for i, char in enumerate(text):
    if i < 5:  # Show first 5 for brevity
        print(f"Index {i}: '{char}'")
print("...")
print()

# String slicing
print("=== String Slicing ===")
print()

sentence = "Learning Python is fun and rewarding"
print(f"Original: '{sentence}'")
print()

print("4. Basic slicing:")
print(f"First 8 characters: '{sentence[:8]}'")
print(f"Last 9 characters: '{sentence[-9:]}'")
print(f"Middle part: '{sentence[9:15]}'")
print(f"Every second character: '{sentence[::2]}'")
print(f"Reverse string: '{sentence[::-1]}'")
print()

print("5. More slicing examples:")
word = "Programming"
print(f"Word: '{word}'")
print(f"word[2:6]: '{word[2:6]}'")
print(f"word[::3]: '{word[::3]}'")
print(f"word[1:-1]: '{word[1:-1]}'")
print()

# String methods - Case conversion
print("=== String Methods - Case Conversion ===")
print()

sample_text = "hello WORLD! this Is A Test."
print(f"Original: '{sample_text}'")
print()

print("6. Case conversion methods:")
print(f".upper(): '{sample_text.upper()}'")
print(f".lower(): '{sample_text.lower()}'")
print(f".title(): '{sample_text.title()}'")
print(f".capitalize(): '{sample_text.capitalize()}'")
print(f".swapcase(): '{sample_text.swapcase()}'")
print()

# String methods - Whitespace handling
print("=== String Methods - Whitespace ===")
print()

messy_string = "   Hello, World!   \n\t"
print(f"Original: '{messy_string}'")
print()

print("7. Whitespace methods:")
print(f".strip(): '{messy_string.strip()}'")
print(f".lstrip(): '{messy_string.lstrip()}'")
print(f".rstrip(): '{messy_string.rstrip()}'")
print()

# String methods - Find and replace
print("=== String Methods - Find and Replace ===")
print()

text_sample = "Python is great. Python is powerful. Python is fun."
print(f"Original: '{text_sample}'")
print()

print("8. Search and replace methods:")
print(f".count('Python'): {text_sample.count('Python')}")
print(f".find('great'): {text_sample.find('great')}")
print(f".find('amazing'): {text_sample.find('amazing')}")  # Returns -1 if not found
print(f".replace('Python', 'Java'): '{text_sample.replace('Python', 'Java')}'")
print(f".replace('is', 'was', 1): '{text_sample.replace('is', 'was', 1)}'")  # Replace only first occurrence
print()

# String methods - Split and join
print("=== String Methods - Split and Join ===")
print()

csv_data = "apple,banana,orange,grape,kiwi"
sentence_data = "The quick brown fox jumps over the lazy dog"

print(f"CSV data: '{csv_data}'")
print(f"Sentence: '{sentence_data}'")
print()

print("9. Split method:")
fruits = csv_data.split(',')
words = sentence_data.split()
print(f"csv_data.split(','): {fruits}")
print(f"sentence.split(): {words}")
print()

print("10. Join method:")
joined_fruits = ' | '.join(fruits)
joined_words = '-'.join(words)
print(f"' | '.join(fruits): '{joined_fruits}'")
print(f"'-'.join(words): '{joined_words}'")
print()

# String methods - Start/End checking
print("=== String Methods - Start/End Checking ===")
print()

filename = "document.txt"
url = "https://www.example.com"
print(f"Filename: '{filename}'")
print(f"URL: '{url}'")
print()

print("11. Start/End methods:")
print(f"filename.startswith('doc'): {filename.startswith('doc')}")
print(f"filename.endswith('.txt'): {filename.endswith('.txt')}")
print(f"url.startswith('https'): {url.startswith('https')}")
print(f"url.endswith('.com'): {url.endswith('.com')}")
print()

# String property checking
print("=== String Property Checking ===")
print()

test_strings = ["123", "abc", "ABC123", "   ", "Hello123", "12.34"]
print("12. Testing string properties:")

for s in test_strings:
    print(f"'{s}':")
    print(f"  .isdigit(): {s.isdigit()}")
    print(f"  .isalpha(): {s.isalpha()}")
    print(f"  .isalnum(): {s.isalnum()}")
    print(f"  .isspace(): {s.isspace()}")
    print(f"  .isupper(): {s.isupper()}")
    print(f"  .islower(): {s.islower()}")
    print()

# String formatting
print("=== String Formatting ===")
print()

name = "Alice"
age = 25
score = 87.5

print("13. Different formatting methods:")

# f-strings (recommended)
print(f"f-string: Hello {name}, you are {age} years old and scored {score:.1f}")

# .format() method
print("format(): Hello {}, you are {} years old and scored {:.1f}".format(name, age, score))

# Named placeholders
print("Named format: Hello {name}, you are {age} years old and scored {score:.1f}".format(
    name=name, age=age, score=score))

# % formatting (older style)
print("% formatting: Hello %s, you are %d years old and scored %.1f" % (name, age, score))
print()

# Advanced f-string formatting
print("14. Advanced f-string formatting:")
number = 1234.5678
print(f"Number: {number}")
print(f"Two decimal places: {number:.2f}")
print(f"Comma separator: {number:,.2f}")
print(f"Percentage: {0.875:.1%}")
print(f"Padded: '{name:>10}'")  # Right-aligned in 10 characters
print(f"Centered: '{name:^10}'")  # Centered in 10 characters
print()

# Strings with loops
print("=== Strings with Loops ===")
print()

text_to_analyze = "Hello Python World!"
print(f"Analyzing: '{text_to_analyze}'")
print()

print("15. Character analysis:")
vowels = "aeiouAEIOU"
consonants = 0
vowel_count = 0
digits = 0
spaces = 0

for char in text_to_analyze:
    if char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    elif char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonants += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print()

# Practical examples
print("=== Practical Examples ===")
print()

print("16. Email validation (simple):")
emails = ["user@example.com", "invalid-email", "test@domain.org", "@missing.com"]

for email in emails:
    if "@" in email and "." in email and not email.startswith("@"):
        print(f"'{email}': Valid format")
    else:
        print(f"'{email}': Invalid format")
print()

print("17. Word frequency counter:")
sample_paragraph = "The quick brown fox jumps over the lazy dog. The dog was lazy but the fox was quick."
words = sample_paragraph.lower().replace(".", "").replace(",", "").split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word frequencies:")
for word, count in word_freq.items():
    print(f"  '{word}': {count}")
print()

print("18. Text cleaning:")
messy_text = "  Hello,    WORLD!!!   How   are   YOU???  "
print(f"Original: '{messy_text}'")

# Clean the text step by step
cleaned = messy_text.strip()  # Remove leading/trailing whitespace
cleaned = cleaned.lower()     # Convert to lowercase
cleaned = cleaned.replace("!", "")  # Remove exclamation marks
cleaned = cleaned.replace("?", "")  # Remove question marks
cleaned = " ".join(cleaned.split())  # Remove extra spaces

print(f"Cleaned: '{cleaned}'")
print()

print("=== End of Examples ===")
print("Key Points to Remember:")
print("- Strings are sequences of characters")
print("- Use indexing and slicing to access parts of strings")
print("- String methods don't modify the original string")
print("- f-strings are the preferred formatting method")
print("- String methods can be chained together")
print("- Use appropriate string methods for text processing")
print("- Practice with real text data for better understanding")
