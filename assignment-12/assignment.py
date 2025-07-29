# Assignment.py - Lesson 12: Final Project - Student Management System
# Student Name: [Write your name here]
# Date: [Write today's date here]

"""
FINAL PROJECT: Student Management System

This is your capstone project that integrates ALL concepts learned throughout the course.
Your task is to create a comprehensive Student Management System that demonstrates
mastery of Python fundamentals and advanced programming concepts.

COURSE CONCEPT INTEGRATION:
✓ Assignment 1-2: Variables, data types, print statements, comments
✓ Assignment 3-4: User input, conditionals, comparison operators  
✓ Assignment 5-6: Loops (while/for), range function, loop control
✓ Assignment 7-9: String manipulation, list operations, advanced data structures
✓ Assignment 10: Function definition, parameters, return values, scope
✓ Assignment 11: Advanced functions, file handling, decorators, error handling
✓ Assignment 12: Complete application integration and project management

PROJECT REQUIREMENTS:
1. Student Management (add, edit, remove, search students)
2. Course Management (course catalog, enrollment, capacity management)
3. Grade Management (record grades, calculate GPA, track progress)
4. Data Persistence (save/load from JSON files, backup system)
5. Reporting (transcripts, enrollment reports, grade statistics)
6. User Interface (menu-driven, input validation, error handling)

ADVANCED FEATURES (BONUS):
- Advanced search with multiple criteria
- Data export to CSV format
- Grade analytics and statistics
- Automated backup system
- Comprehensive error handling
- User-friendly interface design

DELIVERABLES:
- Complete Python application (this file)
- Sample data files (students.json, courses.json, grades.json)
- Documentation (README, user guide, technical documentation)
- Test cases and demonstration examples
"""

import json
import csv
import os
import datetime
from functools import wraps
import re

# ===== GLOBAL CONSTANTS AND CONFIGURATION =====

# File paths and directories
DATA_DIR = "data"
REPORTS_DIR = "reports"
EXPORTS_DIR = "exports"
LOGS_DIR = "logs"

# System configuration
DEFAULT_COURSE_CAPACITY = 30
DEFAULT_COURSE_CREDITS = 3
BACKUP_RETENTION_DAYS = 30

# Grade scale configuration
GRADE_SCALE = {
    'A': {'min': 90, 'points': 4.0},
    'B': {'min': 80, 'points': 3.0},
    'C': {'min': 70, 'points': 2.0},
    'D': {'min': 60, 'points': 1.0},
    'F': {'min': 0, 'points': 0.0}
}

# ===== UTILITY FUNCTIONS AND DECORATORS =====

def log_action(func):
    """
    Decorator to log system actions.
    
    TODO: Implement logging functionality that:
    1. Records function calls with timestamp
    2. Logs parameters and return values
    3. Handles and logs any exceptions
    4. Writes to log files in the logs directory
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Implement logging decorator
        # Log format: [TIMESTAMP] FUNCTION_NAME: success/error details
        pass
    return wrapper

def validate_email(email):
    """
    Validate email format using regular expressions.
    
    TODO: Implement email validation that:
    1. Checks for proper email format (user@domain.com)
    2. Returns True if valid, False if invalid
    3. Use regex pattern matching
    """
    # TODO: Use re module to validate email format
    pass

def validate_date(date_string):
    """
    Validate date format (YYYY-MM-DD).
    
    TODO: Implement date validation that:
    1. Checks for YYYY-MM-DD format
    2. Validates actual date (not 2024-13-45)
    3. Returns True if valid, False if invalid
    """
    # TODO: Parse and validate date string
    pass

def generate_id(prefix, existing_ids, start_num=1):
    """
    Generate unique ID with given prefix.
    
    TODO: Implement ID generation that:
    1. Creates IDs like STU001, COU001, etc.
    2. Ensures uniqueness by checking existing_ids
    3. Returns next available ID
    
    Parameters:
    prefix (str): ID prefix (e.g., 'STU', 'COU')
    existing_ids (list): List of existing IDs to avoid duplicates
    start_num (int): Starting number for ID sequence
    """
    # TODO: Generate unique ID with proper formatting
    pass

def create_directories():
    """
    Create necessary directories for the application.
    
    TODO: Create directories:
    - data/ (for JSON files)
    - reports/ (for generated reports)
    - exports/ (for CSV exports)
    - logs/ (for system logs)
    - data/backups/ (for data backups)
    """
    # TODO: Use os.makedirs() to create directory structure
    pass

# ===== DATA CLASSES =====

class Student:
    """
    Student record class representing a student in the system.
    
    TODO: Implement Student class with:
    1. Constructor (__init__) accepting all student attributes
    2. Methods for data manipulation and validation
    3. String representation (__str__) for display
    4. Dictionary conversion methods for JSON serialization
    """
    
    def __init__(self, student_id, first_name, last_name, email, **kwargs):
        """
        Initialize a new student record.
        
        Required Parameters:
        student_id (str): Unique student identifier
        first_name (str): Student's first name
        last_name (str): Student's last name
        email (str): Student's email address
        
        Optional Parameters (**kwargs):
        phone (str): Phone number
        date_of_birth (str): Birth date (YYYY-MM-DD)
        enrollment_date (str): Enrollment date (YYYY-MM-DD)
        status (str): Student status ('active', 'inactive', 'graduated')
        major (str): Academic major
        gpa (float): Grade point average
        credits_completed (int): Number of credits completed
        """
        # TODO: Initialize all student attributes
        # Required attributes
        # Optional attributes with defaults
        pass
    
    def full_name(self):
        """Return student's full name."""
        # TODO: Return formatted full name
        pass
    
    def age(self):
        """Calculate and return student's age."""
        # TODO: Calculate age from date_of_birth
        pass
    
    def is_active(self):
        """Check if student is active."""
        # TODO: Return True if status is 'active'
        pass
    
    def update_gpa(self, new_gpa):
        """Update student's GPA with validation."""
        # TODO: Validate GPA range (0.0-4.0) and update
        pass
    
    def add_credits(self, credits):
        """Add completed credits."""
        # TODO: Add credits to total completed
        pass
    
    def to_dict(self):
        """Convert student to dictionary for JSON serialization."""
        # TODO: Return dictionary with all student attributes
        pass
    
    @classmethod
    def from_dict(cls, data):
        """Create student instance from dictionary."""
        # TODO: Create Student object from dictionary data
        pass
    
    def __str__(self):
        """String representation of student."""
        # TODO: Return formatted string for display
        pass

class Course:
    """
    Course record class representing a course in the system.
    
    TODO: Implement Course class similar to Student class
    """
    
    def __init__(self, course_id, course_name, **kwargs):
        """
        Initialize a new course record.
        
        Required Parameters:
        course_id (str): Unique course identifier (e.g., 'CS101')
        course_name (str): Course name
        
        Optional Parameters:
        description (str): Course description
        credits (int): Credit hours
        instructor (str): Instructor name
        prerequisites (list): List of prerequisite course IDs
        capacity (int): Maximum enrollment
        schedule (dict): Class schedule information
        semester (str): Semester (Fall, Spring, Summer)
        year (int): Academic year
        """
        # TODO: Initialize all course attributes
        pass
    
    def available_spots(self):
        """Calculate available enrollment spots."""
        # TODO: Return capacity - current enrollment
        pass
    
    def is_full(self):
        """Check if course is at capacity."""
        # TODO: Return True if no available spots
        pass
    
    def add_student(self, student_id):
        """Add student to course enrollment."""
        # TODO: Add student if capacity allows
        pass
    
    def remove_student(self, student_id):
        """Remove student from course enrollment."""
        # TODO: Remove student from enrolled list
        pass
    
    def to_dict(self):
        """Convert course to dictionary."""
        # TODO: Return dictionary representation
        pass
    
    @classmethod
    def from_dict(cls, data):
        """Create course from dictionary."""
        # TODO: Create Course object from data
        pass
    
    def __str__(self):
        """String representation of course."""
        # TODO: Return formatted string
        pass

class Grade:
    """
    Grade record class representing a single grade entry.
    
    TODO: Implement Grade class for individual assignments/exams
    """
    
    def __init__(self, student_id, course_id, assignment_name, points_earned, points_possible, **kwargs):
        """
        Initialize a grade record.
        
        Parameters:
        student_id (str): Student identifier
        course_id (str): Course identifier
        assignment_name (str): Name of assignment/exam
        points_earned (float): Points earned by student
        points_possible (float): Maximum possible points
        **kwargs: Additional grade information
        """
        # TODO: Initialize grade attributes
        # Calculate percentage and letter grade
        pass
    
    def calculate_percentage(self):
        """Calculate grade percentage."""
        # TODO: Calculate (points_earned / points_possible) * 100
        pass
    
    def calculate_letter_grade(self):
        """Determine letter grade from percentage."""
        # TODO: Use GRADE_SCALE to determine letter grade
        pass
    
    def to_dict(self):
        """Convert grade to dictionary."""
        # TODO: Return dictionary representation
        pass
    
    @classmethod
    def from_dict(cls, data):
        """Create grade from dictionary."""
        # TODO: Create Grade object from data
        pass

# ===== MAIN SYSTEM CLASS =====

class StudentManagementSystem:
    """
    Main system class coordinating all functionality.
    
    This class should integrate all the concepts learned throughout the course:
    - Data management with lists and dictionaries
    - File operations for data persistence
    - User interface with menus and input validation
    - Error handling and logging
    - Advanced functions and features
    """
    
    def __init__(self):
        """
        Initialize the Student Management System.
        
        TODO: Initialize system by:
        1. Creating necessary directories
        2. Loading existing data from files
        3. Setting up system state
        4. Logging system startup
        """
        # TODO: Initialize system attributes
        self.students = {}  # {student_id: Student object}
        self.courses = {}   # {course_id: Course object}
        self.grades = {}    # {student_id: {course_id: [Grade objects]}}
        
        # TODO: Create directories and load data
        pass
    
    # ===== FILE OPERATIONS =====
    
    @log_action
    def save_data(self, data_type="all"):
        """
        Save system data to JSON files.
        
        TODO: Implement data saving that:
        1. Saves students, courses, and grades to separate JSON files
        2. Creates backups before overwriting
        3. Handles file write errors gracefully
        4. Logs save operations
        
        Parameters:
        data_type (str): Type of data to save ('students', 'courses', 'grades', 'all')
        """
        # TODO: Save data to JSON files with error handling
        pass
    
    def load_data(self):
        """
        Load system data from JSON files.
        
        TODO: Load existing data or create default empty data
        1. Load students.json, courses.json, grades.json
        2. Handle missing files gracefully
        3. Validate loaded data
        4. Log load operations
        """
        # TODO: Load data from files with error handling
        pass
    
    def create_backup(self):
        """
        Create timestamped backup of all data.
        
        TODO: Create backup files with timestamp:
        - students_backup_YYYY-MM-DD_HH-MM-SS.json
        - courses_backup_YYYY-MM-DD_HH-MM-SS.json
        - grades_backup_YYYY-MM-DD_HH-MM-SS.json
        """
        # TODO: Create timestamped backup files
        pass
    
    def cleanup_old_backups(self):
        """Remove backup files older than retention period."""
        # TODO: Remove backups older than BACKUP_RETENTION_DAYS
        pass
    
    # ===== STUDENT MANAGEMENT =====
    
    @log_action
    def add_student(self, first_name, last_name, email, **kwargs):
        """
        Add a new student to the system.
        
        TODO: Implement student creation with:
        1. Input validation (email format, required fields)
        2. Unique ID generation
        3. Student object creation
        4. Data persistence
        
        Parameters:
        first_name (str): Student's first name
        last_name (str): Student's last name
        email (str): Student's email address
        **kwargs: Additional student information
        
        Returns:
        str: Generated student ID or None if failed
        """
        # TODO: Validate inputs
        # TODO: Generate unique student ID
        # TODO: Create Student object
        # TODO: Add to system and save
        pass
    
    def edit_student(self, student_id, **updates):
        """
        Edit existing student information.
        
        TODO: Update student with validation:
        1. Verify student exists
        2. Validate new information
        3. Update student object
        4. Save changes
        """
        # TODO: Find student and update with validation
        pass
    
    def remove_student(self, student_id):
        """
        Remove student from system.
        
        TODO: Remove student with cleanup:
        1. Remove from courses
        2. Remove grade records
        3. Remove from system
        4. Save changes
        """
        # TODO: Remove student and clean up related data
        pass
    
    def search_students(self, **criteria):
        """
        Search students with multiple criteria.
        
        TODO: Implement flexible search supporting:
        - name (partial match in first/last name)
        - email (partial match)
        - major (exact or partial match)
        - status (exact match)
        - gpa_min, gpa_max (range search)
        - enrollment_year (year of enrollment)
        
        Use lambda functions for filtering and sorting.
        """
        # TODO: Filter students based on criteria using lambda functions
        pass
    
    def get_student(self, student_id):
        """Get student by ID."""
        # TODO: Return student object or None
        pass
    
    def list_all_students(self, sort_by="last_name"):
        """
        List all students with sorting options.
        
        TODO: Return sorted list of students
        Sort options: 'last_name', 'first_name', 'student_id', 'gpa', 'enrollment_date'
        """
        # TODO: Return sorted student list
        pass
    
    # ===== COURSE MANAGEMENT =====
    
    @log_action
    def add_course(self, course_id, course_name, **kwargs):
        """
        Add a new course to the system.
        
        TODO: Implement course creation with:
        1. Course ID validation (format check)
        2. Uniqueness verification
        3. Course object creation
        4. Data persistence
        """
        # TODO: Validate and create course
        pass
    
    def edit_course(self, course_id, **updates):
        """Edit existing course information."""
        # TODO: Update course with validation
        pass
    
    def remove_course(self, course_id):
        """
        Remove course from system.
        
        TODO: Remove course with cleanup:
        1. Remove students from course
        2. Remove grade records
        3. Handle prerequisite dependencies
        4. Update student records
        """
        # TODO: Remove course and clean up dependencies
        pass
    
    def enroll_student(self, student_id, course_id):
        """
        Enroll student in course.
        
        TODO: Handle enrollment with validation:
        1. Verify student and course exist
        2. Check course capacity
        3. Verify prerequisites
        4. Check for conflicts
        5. Add student to course
        6. Update records
        """
        # TODO: Enroll student with all validations
        pass
    
    def drop_student(self, student_id, course_id):
        """Drop student from course."""
        # TODO: Remove student from course and update records
        pass
    
    def get_course_roster(self, course_id):
        """Get list of students enrolled in course."""
        # TODO: Return list of enrolled students
        pass
    
    def get_student_schedule(self, student_id):
        """Get student's current course schedule."""
        # TODO: Return list of courses student is enrolled in
        pass
    
    # ===== GRADE MANAGEMENT =====
    
    @log_action
    def add_grade(self, student_id, course_id, assignment_name, points_earned, points_possible, **kwargs):
        """
        Add a grade record.
        
        TODO: Implement grade entry with:
        1. Validation of student enrollment in course
        2. Points validation (earned <= possible)
        3. Grade calculation
        4. Update student GPA
        5. Data persistence
        """
        # TODO: Add grade with validation and GPA update
        pass
    
    def edit_grade(self, student_id, course_id, assignment_name, **updates):
        """Edit existing grade record."""
        # TODO: Find and update grade record
        pass
    
    def remove_grade(self, student_id, course_id, assignment_name):
        """Remove grade record."""
        # TODO: Remove grade and recalculate GPA
        pass
    
    def calculate_course_average(self, student_id, course_id):
        """Calculate student's average in a course."""
        # TODO: Calculate weighted average of all grades in course
        pass
    
    def calculate_student_gpa(self, student_id):
        """
        Calculate student's overall GPA.
        
        TODO: Calculate GPA using:
        1. Course averages
        2. Credit hours weighting
        3. Grade point scale
        4. Update student record
        """
        # TODO: Calculate weighted GPA across all courses
        pass
    
    def get_student_grades(self, student_id, course_id=None):
        """Get grades for student (all courses or specific course)."""
        # TODO: Return grade records for student
        pass
    
    def get_course_grades(self, course_id):
        """Get all grades for a course."""
        # TODO: Return all student grades for course
        pass
    
    # ===== REPORTING AND ANALYTICS =====
    
    def generate_transcript(self, student_id):
        """
        Generate official transcript for student.
        
        TODO: Create comprehensive transcript including:
        1. Student information
        2. Course history with grades
        3. GPA calculation
        4. Credits completed
        5. Academic standing
        """
        # TODO: Generate formatted transcript
        pass
    
    def generate_course_report(self, course_id):
        """
        Generate course enrollment and performance report.
        
        TODO: Include:
        1. Course information
        2. Enrollment statistics
        3. Grade distribution
        4. Student roster
        """
        # TODO: Generate course report
        pass
    
    def generate_grade_statistics(self):
        """
        Generate system-wide grade statistics.
        
        TODO: Calculate:
        1. Overall grade distribution
        2. Average GPA by major
        3. Course difficulty analysis
        4. Performance trends
        """
        # TODO: Generate statistical analysis
        pass
    
    def generate_enrollment_report(self):
        """Generate enrollment statistics report."""
        # TODO: Create enrollment summary
        pass
    
    # ===== DATA EXPORT =====
    
    def export_students_csv(self, filename=None):
        """
        Export student data to CSV file.
        
        TODO: Export with columns:
        - student_id, first_name, last_name, email, phone
        - major, gpa, credits_completed, status, enrollment_date
        """
        # TODO: Export students to CSV
        pass
    
    def export_courses_csv(self, filename=None):
        """Export course data to CSV file."""
        # TODO: Export courses to CSV
        pass
    
    def export_grades_csv(self, filename=None):
        """Export grade data to CSV file."""
        # TODO: Export grades to CSV with student/course names
        pass
    
    def export_transcripts(self, student_ids=None):
        """Export transcripts for specified students (or all)."""
        # TODO: Generate and save transcript files
        pass
    
    # ===== DATA IMPORT =====
    
    def import_students_csv(self, filename):
        """
        Import student data from CSV file.
        
        TODO: Import students with:
        1. Data validation
        2. Duplicate checking
        3. Error reporting
        4. Batch processing
        """
        # TODO: Import and validate student data
        pass
    
    def import_courses_csv(self, filename):
        """Import course data from CSV file."""
        # TODO: Import and validate course data
        pass
    
    def import_grades_csv(self, filename):
        """Import grade data from CSV file."""
        # TODO: Import and validate grade data
        pass
    
    # ===== USER INTERFACE =====
    
    def display_main_menu(self):
        """
        Display main system menu.
        
        TODO: Show clear menu with options:
        1. Student Management
        2. Course Management
        3. Grade Management
        4. Reports and Analytics
        5. Data Import/Export
        6. System Administration
        7. Help
        8. Exit
        """
        # TODO: Display formatted main menu
        pass
    
    def get_user_input(self, prompt, input_type="string", required=True, validation_func=None):
        """
        Get validated user input.
        
        TODO: Handle different input types:
        - string: text input with optional validation
        - int: integer input with range checking
        - float: decimal input with range checking
        - date: date input with format validation
        - email: email input with format validation
        - choice: menu choice validation
        """
        # TODO: Get and validate user input
        pass
    
    def display_students(self, students=None, page_size=10):
        """Display student list with pagination."""
        # TODO: Display students in formatted table with pagination
        pass
    
    def display_courses(self, courses=None, page_size=10):
        """Display course list with pagination."""
        # TODO: Display courses in formatted table
        pass
    
    def confirm_action(self, message):
        """Get user confirmation for important actions."""
        # TODO: Get yes/no confirmation
        pass
    
    # ===== INTERACTIVE MENUS =====
    
    def student_management_menu(self):
        """
        Student management submenu.
        
        TODO: Handle student operations:
        1. Add new student
        2. Edit student
        3. Remove student
        4. Search students
        5. View all students
        6. Generate transcript
        7. Back to main menu
        """
        # TODO: Implement student management menu loop
        pass
    
    def course_management_menu(self):
        """
        Course management submenu.
        
        TODO: Handle course operations:
        1. Add new course
        2. Edit course
        3. Remove course
        4. View course roster
        5. Enroll student
        6. Drop student
        7. View all courses
        8. Back to main menu
        """
        # TODO: Implement course management menu loop
        pass
    
    def grade_management_menu(self):
        """
        Grade management submenu.
        
        TODO: Handle grade operations:
        1. Add grade
        2. Edit grade
        3. Remove grade
        4. View student grades
        5. View course grades
        6. Calculate GPA
        7. Back to main menu
        """
        # TODO: Implement grade management menu loop
        pass
    
    def reports_menu(self):
        """
        Reports and analytics submenu.
        
        TODO: Handle reporting:
        1. Student transcript
        2. Course report
        3. Grade statistics
        4. Enrollment report
        5. Custom reports
        6. Back to main menu
        """
        # TODO: Implement reports menu loop
        pass
    
    def import_export_menu(self):
        """
        Data import/export submenu.
        
        TODO: Handle data operations:
        1. Export students to CSV
        2. Export courses to CSV
        3. Export grades to CSV
        4. Import students from CSV
        5. Import courses from CSV
        6. Import grades from CSV
        7. Backup data
        8. Back to main menu
        """
        # TODO: Implement import/export menu loop
        pass
    
    def system_admin_menu(self):
        """
        System administration submenu.
        
        TODO: Handle admin tasks:
        1. View system statistics
        2. Manage backups
        3. Clean up old data
        4. System settings
        5. View logs
        6. Database maintenance
        7. Back to main menu
        """
        # TODO: Implement admin menu loop
        pass
    
    def run(self):
        """
        Main application loop.
        
        TODO: Implement main program flow:
        1. Display welcome message
        2. Show main menu
        3. Handle user choices
        4. Call appropriate submenu functions
        5. Handle errors gracefully
        6. Save data on exit
        """
        # TODO: Main application loop with error handling
        pass
    
    # ===== DEMO AND TESTING FUNCTIONS =====
    
    def create_sample_data(self):
        """
        Create sample data for testing and demonstration.
        
        TODO: Create realistic sample data:
        1. Add 10-15 sample students with varied information
        2. Add 5-8 sample courses with different attributes
        3. Enroll students in courses
        4. Add sample grades and assignments
        5. Demonstrate all system features
        """
        # TODO: Create comprehensive sample data
        pass
    
    def run_demo(self):
        """
        Run system demonstration showing all features.
        
        TODO: Demonstrate:
        1. Student management operations
        2. Course management operations
        3. Grade entry and calculation
        4. Report generation
        5. Data export functionality
        6. Search and filtering capabilities
        """
        # TODO: Run comprehensive demo
        pass
    
    def test_system(self):
        """
        Run comprehensive system tests.
        
        TODO: Test all major functions:
        1. Data validation
        2. Error handling
        3. File operations
        4. Calculations
        5. Edge cases
        """
        # TODO: Implement system testing
        pass

# ===== UTILITY FUNCTIONS FOR DEVELOPMENT =====

def format_currency(amount):
    """Format number as currency."""
    # TODO: Format as $X,XXX.XX
    pass

def format_date(date_obj):
    """Format date object as string."""
    # TODO: Format date as YYYY-MM-DD or readable format
    pass

def format_phone(phone):
    """Format phone number."""
    # TODO: Format as (XXX) XXX-XXXX
    pass

def calculate_age(birth_date):
    """Calculate age from birth date."""
    # TODO: Calculate age in years
    pass

def validate_gpa(gpa):
    """Validate GPA is in valid range."""
    # TODO: Check 0.0 <= GPA <= 4.0
    pass

def grade_to_points(letter_grade):
    """Convert letter grade to grade points."""
    # TODO: Use GRADE_SCALE to convert
    pass

def points_to_grade(points):
    """Convert grade points to letter grade."""
    # TODO: Use GRADE_SCALE to convert
    pass

# ===== MAIN PROGRAM =====

def main():
    """
    Main program function.
    
    TODO: This function should:
    1. Create StudentManagementSystem instance
    2. Check for command line arguments
    3. Run demo if requested
    4. Start interactive interface
    5. Handle any startup errors
    """
    
    print("=" * 60)
    print("STUDENT MANAGEMENT SYSTEM")
    print("Final Project - Python Programming Course")
    print("=" * 60)
    print()
    
    try:
        # TODO: Create system instance
        # sms = StudentManagementSystem()
        
        # TODO: Check if demo mode requested
        # if "--demo" in sys.argv:
        #     sms.create_sample_data()
        #     sms.run_demo()
        # else:
        #     sms.run()
        
        print("System starting...")
        
        # For now, create a basic instance to test
        # TODO: Remove this basic test and implement full system
        print("TODO: Implement the complete Student Management System")
        print("This is the template for your final project.")
        print("Follow the TODO comments to implement each feature.")
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    
    except Exception as e:
        print(f"\nSystem error: {e}")
        print("Please check the logs for more details.")
    
    finally:
        print("\nThank you for using the Student Management System!")

# ===== SAMPLE IMPLEMENTATION STARTER =====

# Uncomment and complete these examples to get started:

# def add_student_example():
#     """Example implementation of add_student method."""
#     def add_student(self, first_name, last_name, email, **kwargs):
#         # Validate email
#         if not validate_email(email):
#             raise ValueError("Invalid email format")
#         
#         # Generate unique ID
#         student_id = generate_id("STU", list(self.students.keys()))
#         
#         # Create student object
#         student = Student(student_id, first_name, last_name, email, **kwargs)
#         
#         # Add to system
#         self.students[student_id] = student
#         self.grades[student_id] = {}
#         
#         # Save data
#         self.save_data("students")
#         
#         return student_id

# def search_students_example():
#     """Example implementation of search_students method."""
#     def search_students(self, **criteria):
#         results = list(self.students.values())
#         
#         # Filter by name
#         if 'name' in criteria:
#             name_query = criteria['name'].lower()
#             results = list(filter(
#                 lambda s: name_query in s.first_name.lower() or 
#                          name_query in s.last_name.lower(), 
#                 results
#             ))
#         
#         # Filter by major
#         if 'major' in criteria:
#             major_query = criteria['major'].lower()
#             results = list(filter(
#                 lambda s: major_query in s.major.lower(), 
#                 results
#             ))
#         
#         # Sort results
#         sort_by = criteria.get('sort_by', 'last_name')
#         if sort_by == 'name':
#             results.sort(key=lambda s: (s.last_name, s.first_name))
#         elif sort_by == 'gpa':
#             results.sort(key=lambda s: s.gpa, reverse=True)
#         
#         return results

# ===== PROJECT CHECKLIST =====

"""
IMPLEMENTATION CHECKLIST:

CORE REQUIREMENTS (Required for passing):
□ Student Management
  □ Add new students with validation
  □ Edit student information
  □ Remove students
  □ Search students by multiple criteria
  □ Display student information

□ Course Management
  □ Add new courses
  □ Edit course information
  □ Manage course enrollment
  □ Check prerequisites and capacity
  □ Display course information

□ Grade Management
  □ Add grades for assignments
  □ Calculate course averages
  □ Calculate student GPAs
  □ Display grade information

□ Data Persistence
  □ Save data to JSON files
  □ Load data on startup
  □ Handle file errors gracefully
  □ Create data backups

□ User Interface
  □ Menu-driven interface
  □ Input validation
  □ Error handling
  □ Clear user feedback

ADVANCED FEATURES (Bonus points):
□ Data Export
  □ Export to CSV format
  □ Generate reports
  □ Create transcripts

□ Advanced Search
  □ Multiple search criteria
  □ Sorting options
  □ Filtering capabilities

□ Analytics
  □ Grade statistics
  □ Performance analysis
  □ Enrollment reports

□ System Administration
  □ Backup management
  □ Log viewing
  □ System maintenance

DOCUMENTATION:
□ Code comments and docstrings
□ User guide
□ Technical documentation
□ README file

TESTING:
□ Sample data creation
□ Feature testing
□ Error handling testing
□ Edge case testing

Remember to:
1. Start with basic functionality
2. Test each feature as you implement it
3. Add error handling throughout
4. Document your code thoroughly
5. Create sample data for testing
6. Test edge cases and error conditions
"""

if __name__ == "__main__":
    main()
