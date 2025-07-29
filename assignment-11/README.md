# Assignment 11: Functions - Advanced and File Handling

## Learning Objectives
By the end of this lesson, students will be able to:

1. **Advanced Function Concepts**
   - Create functions with default parameters and keyword arguments
   - Use *args and **kwargs for variable arguments
   - Understand and implement recursive functions
   - Create and use lambda functions (anonymous functions)
   - Implement function decorators (basic understanding)

2. **File Handling Operations**
   - Open, read, write, and close files
   - Handle different file modes (read, write, append)
   - Process text files line by line
   - Handle CSV files and structured data
   - Implement proper error handling for file operations

3. **Practical Applications**
   - Create a personal expense tracker that saves/loads data
   - Build a student grade management system
   - Implement data backup and recovery functions
   - Process log files and generate reports

## Assignment Description

**Project: Personal Finance Manager**

Create a comprehensive personal finance management system that uses advanced functions and file handling to:

1. **Income/Expense Tracking**: Record and categorize financial transactions
2. **Data Persistence**: Save data to files and load on program start
3. **Report Generation**: Create monthly summaries and category breakdowns
4. **Data Import/Export**: Handle CSV files for bulk data operations
5. **Budget Management**: Set and track budget limits with alerts

### Requirements

#### Part 1: Advanced Function Features (40 points)
- Use default parameters for optional settings
- Implement *args/**kwargs for flexible function calls
- Create at least one recursive function (e.g., category tree navigation)
- Use lambda functions for data sorting and filtering
- Implement function decorators for logging user actions

#### Part 2: File Operations (40 points)
- Save transaction data to text/JSON files
- Load existing data on program startup
- Export reports to CSV format
- Handle file errors gracefully (file not found, permissions, etc.)
- Implement data backup functionality

#### Part 3: User Interface and Features (20 points)
- Menu-driven interface with clear options
- Input validation and error handling
- Help system and user guidance
- Data visualization (text-based charts/summaries)

### Technical Specifications

#### Data Structure
```
Transaction: {
    'id': unique_identifier,
    'date': 'YYYY-MM-DD',
    'amount': float,
    'category': string,
    'type': 'income' or 'expense',
    'description': string,
    'tags': [list of strings]
}

Budget: {
    'category': string,
    'monthly_limit': float,
    'current_spent': float,
    'alert_threshold': 0.8  # Alert at 80%
}
```

#### File Structure
```
data/
├── transactions.json        # All transaction data
├── budgets.json            # Budget definitions
├── settings.json           # User preferences
├── backups/                # Automated backups
│   ├── transactions_2024-01-15.json
│   └── transactions_2024-01-01.json
└── reports/                # Generated reports
    ├── monthly_2024-01.csv
    └── category_summary.txt
```

### Sample Program Flow

```
=== Personal Finance Manager ===
Loading data from files...
Found 45 transactions, 8 budget categories

Main Menu:
1. Add Transaction
2. View Transactions
3. Generate Reports
4. Manage Budgets
5. Import/Export Data
6. Settings
7. Exit

Choose option (1-7): 1

=== Add Transaction ===
Enter amount: 50.00
Select type (1=Income, 2=Expense): 2
Select category:
1. Food & Dining
2. Transportation
3. Entertainment
4. Utilities
5. Healthcare
6. Add new category
Choose category (1-6): 1

Description: Lunch at restaurant
Tags (comma-separated, optional): dining, weekend
Transaction added successfully!

Budget Alert: Food & Dining category is at 85% of monthly limit ($425/$500)
```

### Functions to Implement

#### Core Functions
1. `add_transaction(*args, **kwargs)` - Flexible transaction creation
2. `load_data(filename, default_value=None)` - Load data with defaults
3. `save_data(data, filename, backup=True)` - Save with backup option
4. `generate_report(start_date, end_date, format='text')` - Flexible reporting
5. `calculate_category_totals(transactions, category_filter=None)` - Analysis

#### Advanced Functions
1. `search_transactions(lambda_filter)` - Use lambda for custom searches
2. `recursive_category_tree(categories, parent=None)` - Navigate category hierarchy
3. `@log_action` decorator - Log all user actions to file
4. `backup_data(auto=True, **options)` - Flexible backup system
5. `import_csv(filename, mapping_function=None)` - CSV import with custom mapping

### Bonus Challenges (+10 points each)
1. **Data Encryption**: Encrypt sensitive financial data in files
2. **Email Reports**: Send monthly reports via email (simulated)
3. **Data Visualization**: Create ASCII charts for spending trends
4. **Multi-currency Support**: Handle different currencies with conversion
5. **Audit Trail**: Track all data changes with timestamps and user info

### Submission Requirements
1. Complete Python file with all required functions
2. Sample data files demonstrating functionality
3. Test cases showing error handling
4. Documentation explaining advanced features used
5. README with setup and usage instructions

### Grading Rubric
- **Advanced Functions (40%)**: Proper use of default parameters, *args/**kwargs, recursion, lambda, decorators
- **File Handling (40%)**: Correct file operations, error handling, data persistence
- **Code Quality (20%)**: Clean code, documentation, testing, user experience

### Tips for Success
1. Start with basic file operations before adding advanced features
2. Test file operations with different scenarios (missing files, corrupted data)
3. Use try/except blocks for robust error handling
4. Plan your data structure before writing functions
5. Implement one feature at a time and test thoroughly
6. Use descriptive function names and add docstrings
7. Consider edge cases (empty files, invalid data, permission errors)

### Resources
- Python Documentation: File I/O
- JSON module documentation
- CSV module documentation
- Exception handling best practices
- Function parameter techniques (*args, **kwargs)

---

**Due Date**: [Set by instructor]  
**Estimated Time**: 6-8 hours  
**Difficulty**: Advanced  
**Prerequisites**: Completed assignments 1-10, understanding of functions and basic file operations
