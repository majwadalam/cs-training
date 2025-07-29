# Example.py - Lesson 11: Advanced Functions and File Handling
# This file demonstrates advanced function concepts and file operations

"""
Advanced Function and File Handling Examples

This comprehensive example covers:
1. Advanced Function Features
   - Default parameters and keyword arguments
   - *args and **kwargs for variable arguments
   - Recursive functions
   - Lambda functions (anonymous functions)
   - Function decorators

2. File Handling Operations
   - Reading and writing files
   - JSON file operations
   - CSV file handling
   - Error handling for file operations
   - File backup and recovery

3. Practical Applications
   - Personal finance management system
   - Data persistence and recovery
   - Report generation
   - Data import/export functionality
"""

import json
import csv
import os
import datetime
from functools import wraps

# ===== ADVANCED FUNCTION CONCEPTS =====

print("=== Advanced Function Concepts ===")
print()

# 1. Default Parameters and Keyword Arguments
print("1. Default Parameters and Keyword Arguments")

def create_user_profile(name, age=25, city="Unknown", email=None, **additional_info):
    """
    Create a user profile with default values and additional info.
    
    Parameters:
    name (str): Required - user's name
    age (int): Optional - user's age (default: 25)
    city (str): Optional - user's city (default: "Unknown")
    email (str): Optional - user's email (default: None)
    **additional_info: Any additional profile information
    
    Returns:
    dict: Complete user profile
    """
    profile = {
        'name': name,
        'age': age,
        'city': city,
        'email': email,
        'created_date': str(datetime.date.today())
    }
    
    # Add any additional information provided
    profile.update(additional_info)
    
    return profile

# Examples of default parameters
print("Creating user profiles with default parameters:")
profile1 = create_user_profile("Alice")
print(f"Profile 1: {profile1}")

profile2 = create_user_profile("Bob", age=30, city="New York")
print(f"Profile 2: {profile2}")

profile3 = create_user_profile(
    "Carol", 
    email="carol@email.com",
    occupation="Engineer",
    hobby="Photography",
    phone="555-1234"
)
print(f"Profile 3: {profile3}")
print()

# 2. *args and **kwargs - Variable Arguments
print("2. Variable Arguments (*args and **kwargs)")

def calculate_statistics(*numbers, operation="mean", **options):
    """
    Calculate statistics for a variable number of values.
    
    Parameters:
    *numbers: Variable number of numeric values
    operation (str): Type of calculation ("mean", "sum", "max", "min")
    **options: Additional options for calculations
    
    Returns:
    dict: Calculation results
    """
    if not numbers:
        return {"error": "No numbers provided"}
    
    results = {
        "values": numbers,
        "count": len(numbers),
        "operation": operation
    }
    
    if operation == "mean":
        results["result"] = sum(numbers) / len(numbers)
    elif operation == "sum":
        results["result"] = sum(numbers)
    elif operation == "max":
        results["result"] = max(numbers)
    elif operation == "min":
        results["result"] = min(numbers)
    else:
        results["error"] = f"Unknown operation: {operation}"
    
    # Add any additional options to results
    results.update(options)
    
    return results

# Examples of *args and **kwargs
print("Using *args and **kwargs:")
stats1 = calculate_statistics(10, 20, 30, 40, 50)
print(f"Default calculation: {stats1}")

stats2 = calculate_statistics(5, 15, 25, 35, operation="max")
print(f"Max calculation: {stats2}")

stats3 = calculate_statistics(
    100, 200, 300,
    operation="mean",
    rounded=True,
    precision=2,
    units="dollars"
)
print(f"Enhanced calculation: {stats3}")
print()

# 3. Recursive Functions
print("3. Recursive Functions")

def calculate_factorial(n):
    """
    Calculate factorial using recursion.
    
    Parameters:
    n (int): Number to calculate factorial for
    
    Returns:
    int: Factorial of n
    """
    # Base case
    if n <= 1:
        return 1
    
    # Recursive case
    return n * calculate_factorial(n - 1)

def fibonacci_sequence(n, memo={}):
    """
    Generate Fibonacci number using recursion with memoization.
    
    Parameters:
    n (int): Position in Fibonacci sequence
    memo (dict): Memoization dictionary for efficiency
    
    Returns:
    int: Fibonacci number at position n
    """
    # Base cases
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    
    # Recursive case with memoization
    memo[n] = fibonacci_sequence(n - 1, memo) + fibonacci_sequence(n - 2, memo)
    return memo[n]

def find_files_recursively(directory, extension="", current_depth=0, max_depth=3):
    """
    Recursively find files in directory structure.
    
    Parameters:
    directory (str): Directory to search
    extension (str): File extension to filter by
    current_depth (int): Current recursion depth
    max_depth (int): Maximum recursion depth
    
    Returns:
    list: List of found files
    """
    files_found = []
    
    # Safety check for recursion depth
    if current_depth > max_depth:
        return files_found
    
    try:
        # Get all items in current directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            
            if os.path.isfile(item_path):
                # It's a file - check if it matches our criteria
                if not extension or item.endswith(extension):
                    files_found.append(item_path)
            
            elif os.path.isdir(item_path):
                # It's a directory - recurse into it
                subdirectory_files = find_files_recursively(
                    item_path, 
                    extension, 
                    current_depth + 1, 
                    max_depth
                )
                files_found.extend(subdirectory_files)
    
    except PermissionError:
        print(f"Permission denied: {directory}")
    
    return files_found

# Examples of recursive functions
print("Recursive function examples:")
print(f"Factorial of 5: {calculate_factorial(5)}")
print(f"Factorial of 8: {calculate_factorial(8)}")

print(f"Fibonacci number at position 10: {fibonacci_sequence(10)}")
print(f"Fibonacci number at position 15: {fibonacci_sequence(15)}")

# Note: File search example would work if we had a directory structure
print("File search example (would search current directory for .py files):")
current_dir = os.getcwd()
py_files = find_files_recursively(current_dir, ".py", max_depth=1)
print(f"Python files found: {len(py_files)}")
for file in py_files[:3]:  # Show first 3 files
    print(f"  - {file}")
print()

# 4. Lambda Functions (Anonymous Functions)
print("4. Lambda Functions")

# Simple lambda examples
square = lambda x: x ** 2
add_numbers = lambda a, b: a + b
is_even = lambda n: n % 2 == 0

print("Simple lambda functions:")
print(f"Square of 7: {square(7)}")
print(f"Add 15 + 25: {add_numbers(15, 25)}")
print(f"Is 12 even? {is_even(12)}")
print(f"Is 13 even? {is_even(13)}")

# Lambda with built-in functions
numbers = [1, 5, 3, 9, 2, 8, 4, 7, 6]
print(f"\nOriginal numbers: {numbers}")

# Sorting with lambda
sorted_numbers = sorted(numbers, key=lambda x: x)
print(f"Sorted ascending: {sorted_numbers}")

sorted_desc = sorted(numbers, key=lambda x: -x)
print(f"Sorted descending: {sorted_desc}")

# Filtering with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

large_numbers = list(filter(lambda x: x > 5, numbers))
print(f"Numbers > 5: {large_numbers}")

# Mapping with lambda
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Complex lambda with data structures
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 92, "age": 19},
    {"name": "Carol", "grade": 78, "age": 21},
    {"name": "David", "grade": 95, "age": 20}
]

print(f"\nStudent data sorting:")
print("Original order:")
for student in students:
    print(f"  {student['name']}: Grade {student['grade']}, Age {student['age']}")

# Sort by grade (highest first)
sorted_by_grade = sorted(students, key=lambda s: -s['grade'])
print("\nSorted by grade (highest first):")
for student in sorted_by_grade:
    print(f"  {student['name']}: Grade {student['grade']}")

# Sort by age, then by grade
sorted_by_age_grade = sorted(students, key=lambda s: (s['age'], -s['grade']))
print("\nSorted by age, then grade:")
for student in sorted_by_age_grade:
    print(f"  {student['name']}: Age {student['age']}, Grade {student['grade']}")

# Filter high-performing students
high_performers = list(filter(lambda s: s['grade'] >= 90, students))
print(f"\nHigh performers (grade >= 90): {[s['name'] for s in high_performers]}")
print()

# 5. Function Decorators
print("5. Function Decorators")

def timing_decorator(func):
    """Decorator to measure function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def logging_decorator(func):
    """Decorator to log function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

def validation_decorator(func):
    """Decorator to validate function inputs."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Basic validation example
        if args and isinstance(args[0], (int, float)) and args[0] < 0:
            raise ValueError("Negative numbers not allowed")
        return func(*args, **kwargs)
    return wrapper

# Examples of decorated functions
@timing_decorator
@logging_decorator
def calculate_power(base, exponent):
    """Calculate base raised to the power of exponent."""
    result = 1
    for i in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1/result

@validation_decorator
@timing_decorator
def calculate_square_root(number):
    """Calculate square root using Newton's method."""
    if number == 0:
        return 0
    
    # Newton's method for square root
    guess = number / 2
    for _ in range(10):  # 10 iterations for approximation
        guess = (guess + number / guess) / 2
    
    return guess

print("Decorated function examples:")
print("Calculating 2^8:")
result1 = calculate_power(2, 8)
print(f"Result: {result1}")
print()

print("Calculating square root of 16:")
result2 = calculate_square_root(16)
print(f"Result: {result2}")
print()

# ===== FILE HANDLING OPERATIONS =====

print("=== File Handling Operations ===")
print()

# 1. Basic File Operations
print("1. Basic File Operations")

def write_text_file(filename, content, mode='w'):
    """
    Write content to a text file.
    
    Parameters:
    filename (str): Name of the file to write
    content (str): Content to write to file
    mode (str): File mode ('w' for write, 'a' for append)
    
    Returns:
    bool: True if successful, False otherwise
    """
    try:
        with open(filename, mode, encoding='utf-8') as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
        return True
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
        return False

def read_text_file(filename):
    """
    Read content from a text file.
    
    Parameters:
    filename (str): Name of the file to read
    
    Returns:
    str: File content or None if error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"Successfully read from {filename}")
        return content
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

def read_text_file_lines(filename):
    """
    Read file content as a list of lines.
    
    Parameters:
    filename (str): Name of the file to read
    
    Returns:
    list: List of lines or None if error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # Remove newline characters
        lines = [line.strip() for line in lines]
        print(f"Successfully read {len(lines)} lines from {filename}")
        return lines
    except Exception as e:
        print(f"Error reading lines from {filename}: {e}")
        return None

# Example: Basic file operations
sample_content = """This is a sample text file.
It contains multiple lines of text.
We can read and write this file using Python.
File handling is an important skill for data persistence."""

print("Basic file operations example:")
write_text_file("sample.txt", sample_content)

content = read_text_file("sample.txt")
if content:
    print(f"File content (first 100 chars): {content[:100]}...")

lines = read_text_file_lines("sample.txt")
if lines:
    print(f"File has {len(lines)} lines")
    print(f"First line: {lines[0]}")
print()

# 2. JSON File Operations
print("2. JSON File Operations")

def save_data_to_json(data, filename, backup=True):
    """
    Save data to a JSON file with optional backup.
    
    Parameters:
    data: Data to save (must be JSON serializable)
    filename (str): JSON file name
    backup (bool): Whether to create a backup
    
    Returns:
    bool: True if successful, False otherwise
    """
    try:
        # Create backup if requested
        if backup and os.path.exists(filename):
            backup_filename = filename.replace('.json', '_backup.json')
            import shutil
            shutil.copy2(filename, backup_filename)
            print(f"Created backup: {backup_filename}")
        
        # Save data to JSON file
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        
        print(f"Successfully saved data to {filename}")
        return True
    
    except Exception as e:
        print(f"Error saving to {filename}: {e}")
        return False

def load_data_from_json(filename, default_value=None):
    """
    Load data from a JSON file.
    
    Parameters:
    filename (str): JSON file name
    default_value: Value to return if file doesn't exist or has errors
    
    Returns:
    Data from JSON file or default_value
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"Successfully loaded data from {filename}")
        return data
    
    except FileNotFoundError:
        print(f"File {filename} not found, using default value")
        return default_value
    
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filename}: {e}")
        return default_value
    
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return default_value

# Example: JSON operations
sample_data = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@email.com"},
        {"id": 2, "name": "Bob", "email": "bob@email.com"}
    ],
    "settings": {
        "theme": "dark",
        "language": "english",
        "notifications": True
    },
    "created_date": str(datetime.datetime.now())
}

print("JSON file operations example:")
save_data_to_json(sample_data, "sample_data.json")

loaded_data = load_data_from_json("sample_data.json", {})
if loaded_data:
    print(f"Loaded {len(loaded_data)} top-level keys")
    print(f"Users: {len(loaded_data.get('users', []))}")
    print(f"Theme: {loaded_data.get('settings', {}).get('theme', 'unknown')}")

# Test loading non-existent file
missing_data = load_data_from_json("missing_file.json", {"error": "file not found"})
print(f"Missing file result: {missing_data}")
print()

# 3. CSV File Operations
print("3. CSV File Operations")

def save_data_to_csv(data, filename, headers=None):
    """
    Save data to a CSV file.
    
    Parameters:
    data (list): List of dictionaries or list of lists
    filename (str): CSV file name
    headers (list): Column headers (optional)
    
    Returns:
    bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            if data and isinstance(data[0], dict):
                # Data is list of dictionaries
                if not headers:
                    headers = list(data[0].keys())
                
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
            
            else:
                # Data is list of lists
                writer = csv.writer(file)
                if headers:
                    writer.writerow(headers)
                writer.writerows(data)
        
        print(f"Successfully saved CSV data to {filename}")
        return True
    
    except Exception as e:
        print(f"Error saving CSV to {filename}: {e}")
        return False

def load_data_from_csv(filename, has_headers=True):
    """
    Load data from a CSV file.
    
    Parameters:
    filename (str): CSV file name
    has_headers (bool): Whether the file has header row
    
    Returns:
    list: List of dictionaries (if has_headers) or list of lists
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            if has_headers:
                reader = csv.DictReader(file)
                data = list(reader)
            else:
                reader = csv.reader(file)
                data = list(reader)
        
        print(f"Successfully loaded {len(data)} rows from {filename}")
        return data
    
    except Exception as e:
        print(f"Error loading CSV from {filename}: {e}")
        return []

# Example: CSV operations
csv_data = [
    {"name": "Alice", "age": 25, "city": "New York", "salary": 50000},
    {"name": "Bob", "age": 30, "city": "San Francisco", "salary": 75000},
    {"name": "Carol", "age": 28, "city": "Chicago", "salary": 60000},
    {"name": "David", "age": 32, "city": "Boston", "salary": 65000}
]

print("CSV file operations example:")
save_data_to_csv(csv_data, "employees.csv")

loaded_csv = load_data_from_csv("employees.csv")
if loaded_csv:
    print(f"Loaded {len(loaded_csv)} employee records")
    for employee in loaded_csv[:2]:  # Show first 2 records
        print(f"  {employee['name']}: {employee['age']} years old, ${employee['salary']}")
print()

# 4. Error Handling for File Operations
print("4. Advanced Error Handling")

def robust_file_operation(operation, filename, data=None, **kwargs):
    """
    Perform file operations with comprehensive error handling.
    
    Parameters:
    operation (str): Type of operation ('read', 'write', 'append', 'delete')
    filename (str): File name
    data: Data to write (for write operations)
    **kwargs: Additional options
    
    Returns:
    dict: Operation result with status and data/error info
    """
    result = {
        'success': False,
        'operation': operation,
        'filename': filename,
        'data': None,
        'error': None,
        'timestamp': str(datetime.datetime.now())
    }
    
    try:
        if operation == 'read':
            with open(filename, 'r', encoding='utf-8') as file:
                result['data'] = file.read()
        
        elif operation == 'write':
            mode = kwargs.get('mode', 'w')
            with open(filename, mode, encoding='utf-8') as file:
                file.write(str(data))
        
        elif operation == 'append':
            with open(filename, 'a', encoding='utf-8') as file:
                file.write(str(data))
        
        elif operation == 'delete':
            if os.path.exists(filename):
                os.remove(filename)
            else:
                raise FileNotFoundError(f"File {filename} does not exist")
        
        else:
            raise ValueError(f"Unknown operation: {operation}")
        
        result['success'] = True
        print(f"Successfully completed {operation} operation on {filename}")
    
    except FileNotFoundError:
        result['error'] = f"File {filename} not found"
        print(f"Error: {result['error']}")
    
    except PermissionError:
        result['error'] = f"Permission denied for {filename}"
        print(f"Error: {result['error']}")
    
    except OSError as e:
        result['error'] = f"OS error: {e}"
        print(f"Error: {result['error']}")
    
    except Exception as e:
        result['error'] = f"Unexpected error: {e}"
        print(f"Error: {result['error']}")
    
    return result

# Example: Error handling
print("Error handling examples:")

# Successful operation
success_result = robust_file_operation('write', 'test_file.txt', 'Hello, World!')
print(f"Write result: {success_result['success']}")

# Try to read the file we just created
read_result = robust_file_operation('read', 'test_file.txt')
if read_result['success']:
    print(f"Read content: {read_result['data']}")

# Try to read a non-existent file
error_result = robust_file_operation('read', 'non_existent_file.txt')
print(f"Error result: {error_result['error']}")
print()

# ===== PRACTICAL EXAMPLE: MINI FINANCE TRACKER =====

print("=== Practical Example: Mini Finance Tracker ===")
print()

class FinanceTracker:
    """A simple finance tracker demonstrating advanced functions and file handling."""
    
    def __init__(self, data_file="finance_data.json"):
        self.data_file = data_file
        self.transactions = []
        self.categories = set()
        self.load_data()
    
    @logging_decorator
    def load_data(self):
        """Load transaction data from file."""
        data = load_data_from_json(self.data_file, {"transactions": [], "categories": []})
        self.transactions = data.get("transactions", [])
        self.categories = set(data.get("categories", ["Food", "Transport", "Entertainment", "Utilities"]))
        print(f"Loaded {len(self.transactions)} transactions and {len(self.categories)} categories")
    
    @logging_decorator
    def save_data(self):
        """Save transaction data to file."""
        data = {
            "transactions": self.transactions,
            "categories": list(self.categories),
            "last_updated": str(datetime.datetime.now())
        }
        return save_data_to_json(data, self.data_file)
    
    def add_transaction(self, amount, category, description="", transaction_type="expense", **kwargs):
        """Add a new transaction with flexible parameters."""
        transaction = {
            "id": len(self.transactions) + 1,
            "date": str(datetime.date.today()),
            "amount": float(amount),
            "category": category,
            "type": transaction_type,
            "description": description,
            **kwargs  # Include any additional fields
        }
        
        self.transactions.append(transaction)
        self.categories.add(category)
        print(f"Added {transaction_type}: ${amount} for {category}")
        return transaction
    
    def get_transactions_by_category(self, category_filter=None):
        """Get transactions filtered by category using lambda functions."""
        if category_filter:
            filtered = list(filter(lambda t: t['category'] == category_filter, self.transactions))
        else:
            filtered = self.transactions
        
        return sorted(filtered, key=lambda t: t['date'], reverse=True)
    
    def calculate_totals_by_category(self):
        """Calculate spending totals by category."""
        totals = {}
        
        for transaction in self.transactions:
            category = transaction['category']
            amount = transaction['amount']
            transaction_type = transaction['type']
            
            if category not in totals:
                totals[category] = {"income": 0, "expense": 0, "net": 0}
            
            if transaction_type == "income":
                totals[category]["income"] += amount
            else:
                totals[category]["expense"] += amount
            
            totals[category]["net"] = totals[category]["income"] - totals[category]["expense"]
        
        return totals
    
    def generate_report(self, format="text"):
        """Generate a financial report."""
        if not self.transactions:
            return "No transactions to report."
        
        totals = self.calculate_totals_by_category()
        total_income = sum(t["income"] for t in totals.values())
        total_expense = sum(t["expense"] for t in totals.values())
        net_total = total_income - total_expense
        
        if format == "text":
            report = ["=== Financial Report ==="]
            report.append(f"Total Income: ${total_income:.2f}")
            report.append(f"Total Expenses: ${total_expense:.2f}")
            report.append(f"Net Balance: ${net_total:.2f}")
            report.append("\nBy Category:")
            
            for category, amounts in sorted(totals.items()):
                report.append(f"  {category}:")
                report.append(f"    Income: ${amounts['income']:.2f}")
                report.append(f"    Expense: ${amounts['expense']:.2f}")
                report.append(f"    Net: ${amounts['net']:.2f}")
            
            return "\n".join(report)
        
        elif format == "csv":
            csv_data = [["Category", "Income", "Expense", "Net"]]
            for category, amounts in sorted(totals.items()):
                csv_data.append([
                    category,
                    f"{amounts['income']:.2f}",
                    f"{amounts['expense']:.2f}",
                    f"{amounts['net']:.2f}"
                ])
            return csv_data
    
    def export_to_csv(self, filename="financial_report.csv"):
        """Export report to CSV file."""
        csv_data = self.generate_report(format="csv")
        return save_data_to_csv(csv_data, filename)

# Demonstrate the finance tracker
print("Finance Tracker Demonstration:")

# Create tracker instance
tracker = FinanceTracker("demo_finance.json")

# Add some sample transactions
tracker.add_transaction(50.00, "Food", "Grocery shopping", "expense")
tracker.add_transaction(2500.00, "Salary", "Monthly salary", "income")
tracker.add_transaction(30.00, "Transport", "Gas for car", "expense")
tracker.add_transaction(15.00, "Entertainment", "Movie tickets", "expense")
tracker.add_transaction(100.00, "Utilities", "Electric bill", "expense")

# Generate and display report
report = tracker.generate_report()
print(report)

# Save data
tracker.save_data()

# Export to CSV
tracker.export_to_csv("sample_financial_report.csv")
print("\nFinancial report exported to CSV")
print()

# Clean up example files (optional)
example_files = [
    "sample.txt", "sample_data.json", "employees.csv", 
    "test_file.txt", "demo_finance.json", "sample_financial_report.csv"
]

print("Cleaning up example files...")
for filename in example_files:
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Removed: {filename}")
    except Exception as e:
        print(f"Could not remove {filename}: {e}")

print("\n=== Advanced Functions and File Handling Examples Complete ===")
print("Key concepts demonstrated:")
print("- Default parameters and keyword arguments")
print("- *args and **kwargs for flexible functions")
print("- Recursive functions with practical applications")
print("- Lambda functions for data processing")
print("- Function decorators for enhanced functionality")
print("- File operations with robust error handling")
print("- JSON and CSV file processing")
print("- Data persistence and recovery")
print("- Real-world application combining all concepts")
