# Assignment.py - Lesson 11: Personal Finance Manager
# Student Name: [Write your name here]
# Date: [Write today's date here]

"""
Assignment: Personal Finance Manager with Advanced Functions and File Handling

Create a comprehensive personal finance management system that demonstrates:
1. Advanced function concepts (default parameters, *args/**kwargs, recursion, lambda, decorators)
2. File handling operations (JSON, CSV, error handling, data persistence)
3. Real-world application of programming concepts

Your finance manager should be able to:
- Track income and expenses with categories
- Save and load data from files
- Generate reports and export to CSV
- Handle errors gracefully
- Provide a user-friendly menu interface

Requirements:
- Use advanced function features
- Implement proper file handling with error management
- Create a menu-driven interface
- Include data validation and error handling
- Demonstrate function decorators and lambda functions
"""

import json
import csv
import os
import datetime
from functools import wraps

# TODO: Implement Function Decorators

def log_action(func):
    """
    Decorator to log function calls to a file.
    
    This decorator should:
    1. Log the function name, arguments, and timestamp
    2. Log the result or any errors
    3. Write logs to 'finance_log.txt'
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Implement logging functionality
        # Log format: [TIMESTAMP] FUNCTION_NAME called with args: X, kwargs: Y
        # Then call the function and log the result
        # Handle any exceptions and log them too
        pass
    return wrapper

def validate_input(input_type):
    """
    Decorator to validate function inputs.
    
    Parameters:
    input_type (str): Type of validation ('positive_number', 'non_empty_string', 'valid_date')
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Implement input validation based on input_type
            # For 'positive_number': ensure first argument is positive
            # For 'non_empty_string': ensure first argument is non-empty string
            # For 'valid_date': ensure date format is correct
            # Raise appropriate exceptions for invalid inputs
            pass
        return wrapper
    return decorator

# TODO: Personal Finance Manager Class

class PersonalFinanceManager:
    """
    A comprehensive personal finance management system.
    
    Features:
    - Track income and expenses with categories
    - Save/load data to/from JSON files
    - Generate reports and export to CSV
    - Category management with budgets
    - Search and filter transactions
    """
    
    def __init__(self, data_file="personal_finance.json", backup_dir="backups"):
        """
        Initialize the finance manager.
        
        Parameters:
        data_file (str): Main data file name
        backup_dir (str): Directory for backup files
        """
        self.data_file = data_file
        self.backup_dir = backup_dir
        self.transactions = []
        self.categories = set(["Food", "Transport", "Entertainment", "Utilities", "Healthcare", "Shopping"])
        self.budgets = {}
        
        # TODO: Create backup directory if it doesn't exist
        # TODO: Load existing data
        pass
    
    # TODO: File Operations with Error Handling
    
    @log_action
    def load_data(self):
        """
        Load all data from JSON file.
        
        Should load:
        - transactions list
        - categories set
        - budgets dictionary
        
        Use default values if file doesn't exist or has errors.
        """
        # TODO: Implement data loading with error handling
        # Try to load from main file
        # If that fails, try to load from most recent backup
        # If that fails, use default empty data
        # Handle JSON decode errors, file not found, etc.
        pass
    
    @log_action
    def save_data(self, create_backup=True):
        """
        Save all data to JSON file with optional backup.
        
        Parameters:
        create_backup (bool): Whether to create a backup before saving
        
        Returns:
        bool: True if successful, False otherwise
        """
        # TODO: Implement data saving with backup
        # Create backup if requested
        # Save current data to main file
        # Handle write errors and permissions
        pass
    
    def create_backup(self):
        """Create a timestamped backup of current data."""
        # TODO: Create backup with timestamp in filename
        # Format: personal_finance_backup_YYYY-MM-DD_HH-MM-SS.json
        pass
    
    # TODO: Transaction Management with Advanced Functions
    
    @log_action
    @validate_input('positive_number')
    def add_transaction(self, amount, category, description="", transaction_type="expense", **additional_info):
        """
        Add a new transaction with flexible parameters.
        
        Parameters:
        amount (float): Transaction amount (must be positive)
        category (str): Transaction category
        description (str): Optional description
        transaction_type (str): 'income' or 'expense'
        **additional_info: Any additional transaction fields
        
        Returns:
        dict: The created transaction
        """
        # TODO: Create transaction dictionary
        # Include: id, date, amount, category, type, description
        # Add any additional_info fields
        # Validate amount is positive
        # Add category to categories set
        # Append to transactions list
        # Return the transaction
        pass
    
    def add_multiple_transactions(self, *transactions):
        """
        Add multiple transactions at once using *args.
        
        Parameters:
        *transactions: Variable number of transaction dictionaries
        
        Returns:
        list: List of added transactions
        """
        # TODO: Use *args to add multiple transactions
        # Each transaction should be a dictionary with required fields
        # Call add_transaction for each one
        # Return list of successfully added transactions
        pass
    
    # TODO: Search and Filter Functions with Lambda
    
    def search_transactions(self, **search_criteria):
        """
        Search transactions using flexible criteria with **kwargs.
        
        Parameters:
        **search_criteria: Flexible search parameters
        
        Supported criteria:
        - category: specific category
        - min_amount, max_amount: amount range
        - start_date, end_date: date range
        - transaction_type: 'income' or 'expense'
        - description_contains: text in description
        
        Returns:
        list: Filtered transactions
        """
        # TODO: Implement flexible search using **kwargs
        # Start with all transactions
        # Apply filters based on provided criteria
        # Use lambda functions where appropriate
        # Return filtered results
        pass
    
    def get_transactions_by_category(self, category=None, sort_by="date", reverse=True):
        """
        Get transactions filtered and sorted by category.
        
        Parameters:
        category (str): Category to filter by (None for all)
        sort_by (str): Field to sort by ('date', 'amount', 'description')
        reverse (bool): Sort in descending order
        
        Returns:
        list: Filtered and sorted transactions
        """
        # TODO: Filter transactions by category using lambda
        # Sort using lambda functions for different fields
        # Return sorted results
        pass
    
    def get_top_expenses(self, limit=5, category=None):
        """
        Get top expenses using lambda functions for sorting.
        
        Parameters:
        limit (int): Number of top expenses to return
        category (str): Optional category filter
        
        Returns:
        list: Top expense transactions
        """
        # TODO: Filter expenses (transaction_type == 'expense')
        # Filter by category if provided
        # Sort by amount (highest first) using lambda
        # Return top 'limit' transactions
        pass
    
    # TODO: Analysis and Reporting Functions
    
    def calculate_category_totals(self, transaction_type=None):
        """
        Calculate totals by category with optional type filter.
        
        Parameters:
        transaction_type (str): Optional filter ('income', 'expense', or None for both)
        
        Returns:
        dict: Category totals
        """
        # TODO: Group transactions by category
        # Calculate totals for each category
        # Apply transaction_type filter if provided
        # Return dictionary of {category: total}
        pass
    
    def calculate_monthly_summary(self, year=None, month=None):
        """
        Calculate monthly financial summary.
        
        Parameters:
        year (int): Year (default: current year)
        month (int): Month (default: current month)
        
        Returns:
        dict: Monthly summary with income, expenses, net
        """
        # TODO: Filter transactions for specific month/year
        # Calculate total income and expenses
        # Calculate net (income - expenses)
        # Include transaction count and category breakdown
        pass
    
    # TODO: Budget Management
    
    def set_budget(self, category, monthly_limit, alert_threshold=0.8):
        """
        Set a budget for a category.
        
        Parameters:
        category (str): Category name
        monthly_limit (float): Monthly spending limit
        alert_threshold (float): Threshold for warnings (0.0-1.0)
        """
        # TODO: Set budget for category
        # Store in budgets dictionary
        # Add category to categories set
        pass
    
    def check_budget_status(self, category=None):
        """
        Check budget status for categories.
        
        Parameters:
        category (str): Specific category (None for all)
        
        Returns:
        dict: Budget status information
        """
        # TODO: Calculate current month spending by category
        # Compare with budget limits
        # Return status including warnings for categories over threshold
        pass
    
    # TODO: Report Generation
    
    def generate_summary_report(self, format="text", include_budgets=True):
        """
        Generate a comprehensive financial summary report.
        
        Parameters:
        format (str): Output format ('text' or 'dict')
        include_budgets (bool): Whether to include budget information
        
        Returns:
        str or dict: Formatted report
        """
        # TODO: Generate comprehensive report including:
        # - Total income and expenses
        # - Category breakdowns
        # - Budget status (if include_budgets=True)
        # - Recent transactions
        # - Monthly trends
        pass
    
    def export_transactions_to_csv(self, filename=None, category=None, start_date=None, end_date=None):
        """
        Export transactions to CSV file with optional filtering.
        
        Parameters:
        filename (str): Output filename (default: auto-generated)
        category (str): Optional category filter
        start_date (str): Optional start date filter
        end_date (str): Optional end date filter
        
        Returns:
        bool: True if successful, False otherwise
        """
        # TODO: Filter transactions based on parameters
        # Generate filename if not provided
        # Write to CSV with proper headers
        # Handle any file errors
        pass
    
    # TODO: Data Import Functions
    
    def import_transactions_from_csv(self, filename, mapping=None):
        """
        Import transactions from CSV file.
        
        Parameters:
        filename (str): CSV file to import
        mapping (dict): Optional column mapping
        
        Returns:
        dict: Import results (success count, errors, etc.)
        """
        # TODO: Read CSV file
        # Parse each row into transaction format
        # Handle different column names with mapping
        # Validate data and add transactions
        # Return import summary
        pass
    
    # TODO: Advanced Features with Recursion
    
    def find_similar_transactions(self, target_transaction, similarity_threshold=0.8):
        """
        Find transactions similar to a target transaction using recursive comparison.
        
        Parameters:
        target_transaction (dict): Transaction to find similarities to
        similarity_threshold (float): Minimum similarity score (0.0-1.0)
        
        Returns:
        list: Similar transactions with similarity scores
        """
        # TODO: Implement similarity calculation
        # Compare category, amount range, description keywords
        # Use recursive function to check nested similarities
        # Return transactions above threshold
        pass
    
    # TODO: Menu System
    
    def display_main_menu(self):
        """Display the main menu options."""
        # TODO: Print main menu with numbered options
        pass
    
    def run_interactive_menu(self):
        """Run the interactive menu system."""
        # TODO: Main loop for interactive menu
        # Handle user input and call appropriate functions
        # Include error handling for invalid choices
        # Provide help and usage information
        pass
    
    # TODO: Utility Functions
    
    def get_user_input(self, prompt, input_type="string", validation_func=None):
        """
        Get validated user input.
        
        Parameters:
        prompt (str): Input prompt
        input_type (str): Expected type ('string', 'float', 'int', 'date')
        validation_func (function): Optional validation function
        
        Returns:
        Validated input value or None if cancelled
        """
        # TODO: Get input from user with type conversion
        # Validate input using validation_func if provided
        # Handle conversion errors and allow retry
        pass
    
    def get_date_input(self, prompt="Enter date (YYYY-MM-DD): "):
        """Get a valid date input from user."""
        # TODO: Get date input and validate format
        # Return datetime.date object or None
        pass
    
    def confirm_action(self, message):
        """Get yes/no confirmation from user."""
        # TODO: Get y/n input and return boolean
        pass

# TODO: Main Program

def main():
    """
    Main program function demonstrating the Personal Finance Manager.
    
    This function should:
    1. Create a PersonalFinanceManager instance
    2. Add some sample data for demonstration
    3. Show various features and capabilities
    4. Run the interactive menu (optional)
    """
    print("=== Personal Finance Manager ===")
    print("Advanced Functions and File Handling Demonstration")
    print()
    
    # TODO: Create finance manager instance
    # finance_manager = PersonalFinanceManager()
    
    # TODO: Add sample transactions for demonstration
    # Use add_transaction and add_multiple_transactions
    
    # TODO: Demonstrate search and filtering capabilities
    # Show lambda functions in action
    
    # TODO: Demonstrate budget management
    # Set budgets and check status
    
    # TODO: Generate and display reports
    # Show both text and CSV export
    
    # TODO: Demonstrate file operations
    # Save data, create backup, load data
    
    # TODO: Optional: Run interactive menu
    # finance_manager.run_interactive_menu()
    
    print("Demonstration complete!")

# TODO: Helper Functions for Testing

def create_sample_data():
    """Create sample transaction data for testing."""
    # TODO: Return list of sample transactions
    # Include various categories, amounts, dates
    # Mix of income and expense transactions
    pass

def test_advanced_functions():
    """Test advanced function features."""
    # TODO: Test decorators, lambda functions, *args/**kwargs
    # Demonstrate each feature with examples
    pass

def test_file_operations():
    """Test file handling capabilities."""
    # TODO: Test JSON save/load, CSV export/import
    # Test error handling with invalid files
    pass

# Example usage and starter code:

# Uncomment the following lines to start working:

# def add_transaction(self, amount, category, description="", transaction_type="expense", **additional_info):
#     """Add a new transaction."""
#     transaction = {
#         'id': len(self.transactions) + 1,
#         'date': str(datetime.date.today()),
#         'amount': float(amount),
#         'category': category,
#         'type': transaction_type,
#         'description': description,
#         **additional_info
#     }
#     self.transactions.append(transaction)
#     self.categories.add(category)
#     return transaction

# Example of using lambda functions:
# expensive_transactions = list(filter(lambda t: t['amount'] > 100, self.transactions))
# sorted_by_amount = sorted(self.transactions, key=lambda t: t['amount'], reverse=True)

# Example of *args usage:
# def add_multiple_transactions(self, *transactions):
#     return [self.add_transaction(**trans) for trans in transactions]

# Example of decorator usage:
# @log_action
# @validate_input('positive_number')
# def add_transaction(self, amount, ...):

# Run the program
if __name__ == "__main__":
    main()
