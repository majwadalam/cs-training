# Example.py - Lesson 12: Student Management System Example
# This file demonstrates a complete implementation integrating all course concepts

"""
Final Project Example: Student Management System

This comprehensive example demonstrates integration of all concepts learned:

Assignments 1-6 (Fundamentals):
- Print statements, variables, data types
- User input, conditionals, loops
- String and list operations

Assignments 7-11 (Advanced):
- Advanced string/list manipulation
- Function design and implementation  
- File handling and data persistence
- Advanced function features and error handling

This serves as both a reference implementation and a foundation
for students to build upon for their final projects.
"""

import json
import csv
import os
import datetime
from functools import wraps
import re

# ===== UTILITY DECORATORS AND FUNCTIONS =====

def log_action(func):
    """Decorator to log system actions to file."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            result = func(*args, **kwargs)
            log_message = f"[{timestamp}] SUCCESS: {func.__name__} executed successfully"
            write_log(log_message)
            return result
        except Exception as e:
            log_message = f"[{timestamp}] ERROR: {func.__name__} failed - {str(e)}"
            write_log(log_message, "ERROR")
            raise
    return wrapper

def validate_input(input_type):
    """Decorator factory for input validation."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Basic validation examples
            if input_type == "student_id" and args:
                if not isinstance(args[1], str) or not args[1].startswith('STU'):
                    raise ValueError("Invalid student ID format")
            elif input_type == "email" and len(args) > 2:
                email = args[2] if len(args) > 2 else kwargs.get('email', '')
                if email and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                    raise ValueError("Invalid email format")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def write_log(message, level="INFO"):
    """Write log message to file."""
    try:
        os.makedirs("logs", exist_ok=True)
        with open("logs/system.log", "a", encoding='utf-8') as log_file:
            log_file.write(f"{level}: {message}\n")
    except Exception:
        pass  # Silent fail for logging

# ===== CORE DATA CLASSES =====

class Student:
    """Student record class demonstrating object-oriented concepts."""
    
    def __init__(self, student_id, first_name, last_name, email, **kwargs):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = kwargs.get('phone', '')
        self.date_of_birth = kwargs.get('date_of_birth', '')
        self.enrollment_date = kwargs.get('enrollment_date', str(datetime.date.today()))
        self.status = kwargs.get('status', 'active')
        self.major = kwargs.get('major', '')
        self.gpa = kwargs.get('gpa', 0.0)
        self.credits_completed = kwargs.get('credits_completed', 0)
        self.courses = kwargs.get('courses', [])
        self.grades = kwargs.get('grades', {})
    
    def to_dict(self):
        """Convert student to dictionary for JSON serialization."""
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'date_of_birth': self.date_of_birth,
            'enrollment_date': self.enrollment_date,
            'status': self.status,
            'major': self.major,
            'gpa': self.gpa,
            'credits_completed': self.credits_completed,
            'courses': self.courses,
            'grades': self.grades
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create student from dictionary."""
        return cls(**data)
    
    def full_name(self):
        """Get student's full name."""
        return f"{self.first_name} {self.last_name}"
    
    def calculate_gpa(self, grade_records):
        """Calculate GPA from grade records."""
        total_points = 0
        total_credits = 0
        
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        
        for course_id in self.courses:
            if course_id in grade_records:
                course_grades = grade_records[course_id]
                # Calculate course average and convert to letter grade
                course_avg = sum(g['percentage'] for g in course_grades) / len(course_grades)
                
                if course_avg >= 90:
                    letter_grade = 'A'
                elif course_avg >= 80:
                    letter_grade = 'B'
                elif course_avg >= 70:
                    letter_grade = 'C'
                elif course_avg >= 60:
                    letter_grade = 'D'
                else:
                    letter_grade = 'F'
                
                total_points += grade_points[letter_grade] * 3  # Assuming 3 credits per course
                total_credits += 3
        
        self.gpa = total_points / total_credits if total_credits > 0 else 0.0
        return self.gpa

class Course:
    """Course record class."""
    
    def __init__(self, course_id, course_name, **kwargs):
        self.course_id = course_id
        self.course_name = course_name
        self.description = kwargs.get('description', '')
        self.credits = kwargs.get('credits', 3)
        self.prerequisites = kwargs.get('prerequisites', [])
        self.instructor = kwargs.get('instructor', '')
        self.schedule = kwargs.get('schedule', {})
        self.capacity = kwargs.get('capacity', 30)
        self.enrolled_students = kwargs.get('enrolled_students', [])
        self.semester = kwargs.get('semester', 'Fall')
        self.year = kwargs.get('year', datetime.date.today().year)
    
    def to_dict(self):
        """Convert course to dictionary."""
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'description': self.description,
            'credits': self.credits,
            'prerequisites': self.prerequisites,
            'instructor': self.instructor,
            'schedule': self.schedule,
            'capacity': self.capacity,
            'enrolled_students': self.enrolled_students,
            'semester': self.semester,
            'year': self.year
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create course from dictionary."""
        return cls(**data)
    
    def is_full(self):
        """Check if course is at capacity."""
        return len(self.enrolled_students) >= self.capacity
    
    def available_spots(self):
        """Get number of available spots."""
        return max(0, self.capacity - len(self.enrolled_students))

# ===== MAIN STUDENT MANAGEMENT SYSTEM =====

class StudentManagementSystem:
    """
    Comprehensive Student Management System integrating all course concepts.
    
    Features:
    - Student record management with full CRUD operations
    - Course catalog and enrollment management
    - Grade tracking and GPA calculation
    - Data persistence with JSON files
    - Report generation and data export
    - Advanced search and filtering capabilities
    """
    
    def __init__(self, data_dir="data"):
        """Initialize the student management system."""
        self.data_dir = data_dir
        self.students = {}  # {student_id: Student object}
        self.courses = {}   # {course_id: Course object}
        self.grades = {}    # {student_id: {course_id: [grade_records]}}
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs("reports", exist_ok=True)
        os.makedirs("exports", exist_ok=True)
        
        # Load existing data
        self.load_all_data()
        
        print("Student Management System initialized successfully!")
        print(f"Loaded: {len(self.students)} students, {len(self.courses)} courses")
    
    # ===== FILE OPERATIONS (Assignment 11 concepts) =====
    
    @log_action
    def save_all_data(self):
        """Save all system data to JSON files."""
        try:
            # Save students
            students_data = {sid: student.to_dict() for sid, student in self.students.items()}
            with open(os.path.join(self.data_dir, "students.json"), 'w') as f:
                json.dump(students_data, f, indent=2)
            
            # Save courses
            courses_data = {cid: course.to_dict() for cid, course in self.courses.items()}
            with open(os.path.join(self.data_dir, "courses.json"), 'w') as f:
                json.dump(courses_data, f, indent=2)
            
            # Save grades
            with open(os.path.join(self.data_dir, "grades.json"), 'w') as f:
                json.dump(self.grades, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_all_data(self):
        """Load all system data from JSON files."""
        try:
            # Load students
            students_file = os.path.join(self.data_dir, "students.json")
            if os.path.exists(students_file):
                with open(students_file, 'r') as f:
                    students_data = json.load(f)
                    self.students = {sid: Student.from_dict(data) for sid, data in students_data.items()}
            
            # Load courses
            courses_file = os.path.join(self.data_dir, "courses.json")
            if os.path.exists(courses_file):
                with open(courses_file, 'r') as f:
                    courses_data = json.load(f)
                    self.courses = {cid: Course.from_dict(data) for cid, data in courses_data.items()}
            
            # Load grades
            grades_file = os.path.join(self.data_dir, "grades.json")
            if os.path.exists(grades_file):
                with open(grades_file, 'r') as f:
                    self.grades = json.load(f)
            
        except Exception as e:
            print(f"Error loading data: {e}")
    
    # ===== STUDENT MANAGEMENT (Assignments 1-6 concepts) =====
    
    @log_action
    @validate_input("email")
    def add_student(self, first_name, last_name, email, **kwargs):
        """
        Add a new student to the system.
        Demonstrates: string manipulation, input validation, dictionary operations
        """
        # Generate unique student ID
        student_id = self.generate_student_id()
        
        # Create new student
        student = Student(student_id, first_name, last_name, email, **kwargs)
        
        # Add to students dictionary
        self.students[student_id] = student
        self.grades[student_id] = {}
        
        print(f"Student added successfully! ID: {student_id}")
        return student_id
    
    def generate_student_id(self):
        """Generate unique student ID. Demonstrates: string formatting, loops"""
        base_id = f"STU{len(self.students) + 1:03d}"
        
        # Ensure uniqueness
        counter = 1
        while base_id in self.students:
            base_id = f"STU{len(self.students) + counter:03d}"
            counter += 1
        
        return base_id
    
    @validate_input("student_id")
    def update_student(self, student_id, **updates):
        """
        Update student information.
        Demonstrates: dictionary operations, conditional logic, **kwargs
        """
        if student_id not in self.students:
            raise ValueError(f"Student {student_id} not found")
        
        student = self.students[student_id]
        
        # Update allowed fields
        updatable_fields = ['first_name', 'last_name', 'email', 'phone', 'major', 'status']
        
        for field, value in updates.items():
            if field in updatable_fields:
                setattr(student, field, value)
        
        print(f"Student {student_id} updated successfully!")
        return True
    
    def remove_student(self, student_id):
        """
        Remove a student from the system.
        Demonstrates: dictionary operations, conditional logic
        """
        if student_id not in self.students:
            print(f"Student {student_id} not found")
            return False
        
        # Remove from courses first
        student = self.students[student_id]
        for course_id in student.courses:
            if course_id in self.courses:
                course = self.courses[course_id]
                if student_id in course.enrolled_students:
                    course.enrolled_students.remove(student_id)
        
        # Remove student and grades
        del self.students[student_id]
        if student_id in self.grades:
            del self.grades[student_id]
        
        print(f"Student {student_id} removed successfully!")
        return True
    
    # ===== SEARCH AND FILTERING (Assignments 7-9 concepts) =====
    
    def search_students(self, **criteria):
        """
        Advanced student search with multiple criteria.
        Demonstrates: lambda functions, list comprehensions, **kwargs
        """
        results = list(self.students.values())
        
        # Apply filters based on criteria
        if 'name' in criteria:
            name_query = criteria['name'].lower()
            results = list(filter(
                lambda s: name_query in s.first_name.lower() or name_query in s.last_name.lower(),
                results
            ))
        
        if 'major' in criteria:
            major_query = criteria['major'].lower()
            results = list(filter(lambda s: major_query in s.major.lower(), results))
        
        if 'status' in criteria:
            status = criteria['status']
            results = list(filter(lambda s: s.status == status, results))
        
        if 'min_gpa' in criteria:
            min_gpa = float(criteria['min_gpa'])
            results = list(filter(lambda s: s.gpa >= min_gpa, results))
        
        if 'max_gpa' in criteria:
            max_gpa = float(criteria['max_gpa'])
            results = list(filter(lambda s: s.gpa <= max_gpa, results))
        
        # Sort results
        sort_by = criteria.get('sort_by', 'last_name')
        reverse = criteria.get('reverse', False)
        
        if sort_by == 'name':
            results.sort(key=lambda s: (s.last_name, s.first_name), reverse=reverse)
        elif sort_by == 'gpa':
            results.sort(key=lambda s: s.gpa, reverse=reverse)
        elif sort_by == 'student_id':
            results.sort(key=lambda s: s.student_id, reverse=reverse)
        
        return results
    
    def get_students_by_course(self, course_id):
        """Get all students enrolled in a specific course."""
        if course_id not in self.courses:
            return []
        
        course = self.courses[course_id]
        enrolled_students = []
        
        for student_id in course.enrolled_students:
            if student_id in self.students:
                enrolled_students.append(self.students[student_id])
        
        return enrolled_students
    
    # ===== COURSE MANAGEMENT =====
    
    @log_action
    def add_course(self, course_id, course_name, **kwargs):
        """Add a new course to the system."""
        if course_id in self.courses:
            raise ValueError(f"Course {course_id} already exists")
        
        course = Course(course_id, course_name, **kwargs)
        self.courses[course_id] = course
        
        print(f"Course {course_id} - {course_name} added successfully!")
        return course_id
    
    def enroll_student_in_course(self, student_id, course_id):
        """
        Enroll a student in a course.
        Demonstrates: conditional logic, list operations, error handling
        """
        # Validate student and course exist
        if student_id not in self.students:
            raise ValueError(f"Student {student_id} not found")
        
        if course_id not in self.courses:
            raise ValueError(f"Course {course_id} not found")
        
        student = self.students[student_id]
        course = self.courses[course_id]
        
        # Check if already enrolled
        if course_id in student.courses:
            print(f"Student {student_id} is already enrolled in {course_id}")
            return False
        
        # Check course capacity
        if course.is_full():
            print(f"Course {course_id} is at full capacity")
            return False
        
        # Check prerequisites
        for prereq in course.prerequisites:
            if prereq not in student.courses:
                print(f"Student {student_id} has not completed prerequisite: {prereq}")
                return False
        
        # Enroll student
        student.courses.append(course_id)
        course.enrolled_students.append(student_id)
        
        # Initialize grade record for this course
        if student_id not in self.grades:
            self.grades[student_id] = {}
        self.grades[student_id][course_id] = []
        
        print(f"Student {student_id} enrolled in {course_id} successfully!")
        return True
    
    # ===== GRADE MANAGEMENT =====
    
    def add_grade(self, student_id, course_id, assignment_name, points_earned, points_possible, **kwargs):
        """
        Add a grade record for a student.
        Demonstrates: dictionary operations, calculations, data validation
        """
        # Validate inputs
        if student_id not in self.students:
            raise ValueError(f"Student {student_id} not found")
        
        if course_id not in self.courses:
            raise ValueError(f"Course {course_id} not found")
        
        if course_id not in self.students[student_id].courses:
            raise ValueError(f"Student {student_id} is not enrolled in {course_id}")
        
        # Calculate percentage
        percentage = (points_earned / points_possible) * 100 if points_possible > 0 else 0
        
        # Determine letter grade
        if percentage >= 90:
            letter_grade = 'A'
        elif percentage >= 80:
            letter_grade = 'B'
        elif percentage >= 70:
            letter_grade = 'C'
        elif percentage >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        
        # Create grade record
        grade_record = {
            'assignment_name': assignment_name,
            'points_earned': points_earned,
            'points_possible': points_possible,
            'percentage': percentage,
            'letter_grade': letter_grade,
            'date_recorded': str(datetime.date.today()),
            **kwargs
        }
        
        # Add to grades
        if student_id not in self.grades:
            self.grades[student_id] = {}
        if course_id not in self.grades[student_id]:
            self.grades[student_id][course_id] = []
        
        self.grades[student_id][course_id].append(grade_record)
        
        # Update student GPA
        self.students[student_id].calculate_gpa(self.grades[student_id])
        
        print(f"Grade added: {assignment_name} - {percentage:.1f}% ({letter_grade})")
        return True
    
    def get_student_transcript(self, student_id):
        """
        Generate a complete transcript for a student.
        Demonstrates: string formatting, loops, data organization
        """
        if student_id not in self.students:
            return "Student not found"
        
        student = self.students[student_id]
        transcript = []
        
        transcript.append("=" * 50)
        transcript.append("OFFICIAL TRANSCRIPT")
        transcript.append("=" * 50)
        transcript.append(f"Student: {student.full_name()}")
        transcript.append(f"Student ID: {student.student_id}")
        transcript.append(f"Major: {student.major}")
        transcript.append(f"Enrollment Date: {student.enrollment_date}")
        transcript.append(f"Current GPA: {student.gpa:.2f}")
        transcript.append(f"Credits Completed: {student.credits_completed}")
        transcript.append("")
        
        transcript.append("COURSE HISTORY:")
        transcript.append("-" * 50)
        
        for course_id in student.courses:
            if course_id in self.courses:
                course = self.courses[course_id]
                transcript.append(f"\n{course_id}: {course.course_name}")
                transcript.append(f"Credits: {course.credits}")
                transcript.append(f"Instructor: {course.instructor}")
                
                # Show grades for this course
                if student_id in self.grades and course_id in self.grades[student_id]:
                    course_grades = self.grades[student_id][course_id]
                    if course_grades:
                        transcript.append("Assignments:")
                        for grade in course_grades:
                            transcript.append(
                                f"  {grade['assignment_name']}: "
                                f"{grade['points_earned']}/{grade['points_possible']} "
                                f"({grade['percentage']:.1f}% - {grade['letter_grade']})"
                            )
                        
                        # Calculate course average
                        avg_percentage = sum(g['percentage'] for g in course_grades) / len(course_grades)
                        transcript.append(f"Course Average: {avg_percentage:.1f}%")
        
        transcript.append("\n" + "=" * 50)
        transcript.append(f"Generated on: {datetime.date.today()}")
        
        return "\n".join(transcript)
    
    # ===== REPORTING AND ANALYTICS =====
    
    def generate_enrollment_report(self):
        """Generate course enrollment statistics."""
        report = []
        report.append("COURSE ENROLLMENT REPORT")
        report.append("=" * 40)
        
        for course_id, course in sorted(self.courses.items()):
            enrollment = len(course.enrolled_students)
            capacity = course.capacity
            percentage = (enrollment / capacity * 100) if capacity > 0 else 0
            
            report.append(f"\n{course_id}: {course.course_name}")
            report.append(f"Enrolled: {enrollment}/{capacity} ({percentage:.1f}%)")
            report.append(f"Instructor: {course.instructor}")
            
            if enrollment > 0:
                # Show student names
                enrolled_names = []
                for student_id in course.enrolled_students:
                    if student_id in self.students:
                        enrolled_names.append(self.students[student_id].full_name())
                
                report.append("Students:")
                for name in sorted(enrolled_names):
                    report.append(f"  - {name}")
        
        return "\n".join(report)
    
    def generate_grade_statistics(self):
        """Generate grade distribution statistics."""
        all_grades = []
        grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        
        # Collect all grades
        for student_id in self.grades:
            for course_id in self.grades[student_id]:
                for grade_record in self.grades[student_id][course_id]:
                    all_grades.append(grade_record['percentage'])
                    grade_counts[grade_record['letter_grade']] += 1
        
        if not all_grades:
            return "No grades recorded yet."
        
        # Calculate statistics
        avg_grade = sum(all_grades) / len(all_grades)
        min_grade = min(all_grades)
        max_grade = max(all_grades)
        
        report = []
        report.append("GRADE STATISTICS REPORT")
        report.append("=" * 30)
        report.append(f"Total Assignments: {len(all_grades)}")
        report.append(f"Average Grade: {avg_grade:.1f}%")
        report.append(f"Highest Grade: {max_grade:.1f}%")
        report.append(f"Lowest Grade: {min_grade:.1f}%")
        report.append("")
        
        report.append("Grade Distribution:")
        total_grades = sum(grade_counts.values())
        for letter, count in grade_counts.items():
            percentage = (count / total_grades * 100) if total_grades > 0 else 0
            report.append(f"  {letter}: {count} ({percentage:.1f}%)")
        
        return "\n".join(report)
    
    # ===== DATA EXPORT (Assignment 11 concepts) =====
    
    def export_students_to_csv(self, filename="students_export.csv"):
        """Export student data to CSV file."""
        try:
            filepath = os.path.join("exports", filename)
            
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'student_id', 'first_name', 'last_name', 'email', 'phone',
                    'major', 'gpa', 'credits_completed', 'status', 'enrollment_date'
                ]
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for student in self.students.values():
                    writer.writerow({
                        'student_id': student.student_id,
                        'first_name': student.first_name,
                        'last_name': student.last_name,
                        'email': student.email,
                        'phone': student.phone,
                        'major': student.major,
                        'gpa': student.gpa,
                        'credits_completed': student.credits_completed,
                        'status': student.status,
                        'enrollment_date': student.enrollment_date
                    })
            
            print(f"Student data exported to {filepath}")
            return True
        
        except Exception as e:
            print(f"Error exporting student data: {e}")
            return False
    
    def export_grades_to_csv(self, filename="grades_export.csv"):
        """Export all grades to CSV file."""
        try:
            filepath = os.path.join("exports", filename)
            
            with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'student_id', 'student_name', 'course_id', 'course_name',
                    'assignment_name', 'points_earned', 'points_possible',
                    'percentage', 'letter_grade', 'date_recorded'
                ]
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for student_id in self.grades:
                    student_name = self.students[student_id].full_name() if student_id in self.students else "Unknown"
                    
                    for course_id in self.grades[student_id]:
                        course_name = self.courses[course_id].course_name if course_id in self.courses else "Unknown"
                        
                        for grade_record in self.grades[student_id][course_id]:
                            writer.writerow({
                                'student_id': student_id,
                                'student_name': student_name,
                                'course_id': course_id,
                                'course_name': course_name,
                                'assignment_name': grade_record['assignment_name'],
                                'points_earned': grade_record['points_earned'],
                                'points_possible': grade_record['points_possible'],
                                'percentage': grade_record['percentage'],
                                'letter_grade': grade_record['letter_grade'],
                                'date_recorded': grade_record['date_recorded']
                            })
            
            print(f"Grade data exported to {filepath}")
            return True
        
        except Exception as e:
            print(f"Error exporting grade data: {e}")
            return False
    
    # ===== USER INTERFACE (Assignments 4-6 concepts) =====
    
    def display_main_menu(self):
        """Display the main system menu."""
        print("\n" + "=" * 50)
        print("STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Student Management")
        print("2. Course Management")
        print("3. Grade Management")
        print("4. Reports and Analytics")
        print("5. Data Export")
        print("6. System Administration")
        print("7. Help")
        print("8. Exit")
        print("-" * 50)
    
    def get_user_choice(self, prompt="Enter your choice: ", valid_choices=None):
        """Get validated user input."""
        while True:
            try:
                choice = input(prompt).strip()
                
                if valid_choices and choice not in valid_choices:
                    print(f"Invalid choice. Please select from: {', '.join(valid_choices)}")
                    continue
                
                return choice
            
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                return None
            except Exception as e:
                print(f"Input error: {e}")
    
    def run_interactive_demo(self):
        """Run an interactive demonstration of the system."""
        print("=== STUDENT MANAGEMENT SYSTEM DEMO ===")
        print("This demo will showcase all major features of the system.")
        print()
        
        # Demo 1: Add sample students
        print("1. Adding sample students...")
        sample_students = [
            {"first_name": "Alice", "last_name": "Johnson", "email": "alice.johnson@email.com", "major": "Computer Science"},
            {"first_name": "Bob", "last_name": "Smith", "email": "bob.smith@email.com", "major": "Mathematics"},
            {"first_name": "Carol", "last_name": "Davis", "email": "carol.davis@email.com", "major": "Physics"}
        ]
        
        for student_data in sample_students:
            student_id = self.add_student(**student_data)
        
        print(f"Added {len(sample_students)} sample students.\n")
        
        # Demo 2: Add sample courses
        print("2. Adding sample courses...")
        sample_courses = [
            {"course_id": "CS101", "course_name": "Introduction to Programming", "instructor": "Dr. Brown", "capacity": 25},
            {"course_id": "MATH201", "course_name": "Calculus I", "instructor": "Prof. Wilson", "capacity": 30},
            {"course_id": "PHYS101", "course_name": "General Physics", "instructor": "Dr. Taylor", "capacity": 20}
        ]
        
        for course_data in sample_courses:
            self.add_course(**course_data)
        
        print(f"Added {len(sample_courses)} sample courses.\n")
        
        # Demo 3: Enroll students in courses
        print("3. Enrolling students in courses...")
        enrollments = [
            ("STU001", "CS101"),
            ("STU001", "MATH201"),
            ("STU002", "MATH201"),
            ("STU002", "CS101"),
            ("STU003", "PHYS101"),
            ("STU003", "MATH201")
        ]
        
        for student_id, course_id in enrollments:
            try:
                self.enroll_student_in_course(student_id, course_id)
            except Exception as e:
                print(f"Enrollment error: {e}")
        
        print()
        
        # Demo 4: Add sample grades
        print("4. Adding sample grades...")
        sample_grades = [
            ("STU001", "CS101", "Assignment 1", 85, 100),
            ("STU001", "CS101", "Midterm Exam", 92, 100),
            ("STU001", "MATH201", "Quiz 1", 78, 100),
            ("STU002", "MATH201", "Assignment 1", 95, 100),
            ("STU002", "CS101", "Assignment 1", 88, 100),
            ("STU003", "PHYS101", "Lab Report 1", 90, 100)
        ]
        
        for grade_data in sample_grades:
            try:
                self.add_grade(*grade_data)
            except Exception as e:
                print(f"Grade entry error: {e}")
        
        print()
        
        # Demo 5: Generate reports
        print("5. Generating reports...")
        
        print("\n--- ENROLLMENT REPORT ---")
        print(self.generate_enrollment_report())
        
        print("\n--- GRADE STATISTICS ---")
        print(self.generate_grade_statistics())
        
        print("\n--- SAMPLE TRANSCRIPT ---")
        print(self.get_student_transcript("STU001"))
        
        # Demo 6: Search functionality
        print("\n6. Demonstrating search functionality...")
        
        # Search by major
        cs_students = self.search_students(major="Computer Science")
        print(f"Computer Science students: {len(cs_students)}")
        for student in cs_students:
            print(f"  - {student.full_name()} ({student.student_id})")
        
        # Search by GPA
        high_gpa_students = self.search_students(min_gpa=3.0)
        print(f"Students with GPA >= 3.0: {len(high_gpa_students)}")
        
        # Demo 7: Data export
        print("\n7. Exporting data...")
        self.export_students_to_csv("demo_students.csv")
        self.export_grades_to_csv("demo_grades.csv")
        
        # Demo 8: Save all data
        print("\n8. Saving all data...")
        self.save_all_data()
        
        print("\n=== DEMO COMPLETE ===")
        print("All features have been demonstrated successfully!")
        print("Data has been saved and exported for review.")

# ===== DEMONSTRATION AND TESTING =====

def main():
    """
    Main demonstration function showcasing all course concepts.
    
    This comprehensive example demonstrates:
    - Object-oriented programming principles
    - File handling and data persistence
    - Advanced function features
    - Error handling and validation
    - User interface design
    - Data processing and analysis
    - Real-world application development
    """
    
    print("=== FINAL PROJECT EXAMPLE ===")
    print("Student Management System")
    print("Integrating all concepts from Assignments 1-11")
    print()
    
    try:
        # Create and initialize the system
        sms = StudentManagementSystem()
        
        # Run the interactive demonstration
        sms.run_interactive_demo()
        
        print("\nExample completed successfully!")
        print("\nThis example demonstrates:")
        print("✓ Variables, data types, and operators (Assignment 1-2)")
        print("✓ User input and conditionals (Assignment 3-4)")
        print("✓ Loops and control structures (Assignment 5-6)")
        print("✓ String and list manipulation (Assignment 7-9)")
        print("✓ Function design and implementation (Assignment 10)")
        print("✓ Advanced functions and file handling (Assignment 11)")
        print("✓ Complete application integration (Assignment 12)")
        
    except Exception as e:
        print(f"Demo error: {e}")
        import traceback
        traceback.print_exc()

# Additional utility functions for teaching purposes

def demonstrate_specific_concepts():
    """Demonstrate specific programming concepts used in the project."""
    
    print("\n=== CONCEPT DEMONSTRATIONS ===\n")
    
    # 1. List comprehensions (Assignment 9)
    print("1. List Comprehensions:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # 2. Lambda functions (Assignment 11)
    print("\n2. Lambda Functions:")
    students_data = [
        {"name": "Alice", "gpa": 3.8},
        {"name": "Bob", "gpa": 3.2},
        {"name": "Carol", "gpa": 3.9}
    ]
    sorted_by_gpa = sorted(students_data, key=lambda s: s['gpa'], reverse=True)
    print("Students sorted by GPA:")
    for student in sorted_by_gpa:
        print(f"  {student['name']}: {student['gpa']}")
    
    # 3. Dictionary comprehensions
    print("\n3. Dictionary Comprehensions:")
    grade_letters = {percentage: 'A' if percentage >= 90 else 'B' if percentage >= 80 else 'C' 
                    for percentage in [95, 87, 76, 92, 84]}
    print(f"Grade mappings: {grade_letters}")
    
    # 4. Error handling patterns
    print("\n4. Error Handling:")
    def safe_divide(a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            return None
        except TypeError:
            print("Invalid input types!")
            return None
    
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    
    # 5. File operations with context managers
    print("\n5. File Operations:")
    sample_data = {"message": "Hello from the student management system!"}
    
    try:
        with open("sample_output.json", "w") as f:
            json.dump(sample_data, f, indent=2)
        print("Sample file created successfully!")
        
        with open("sample_output.json", "r") as f:
            loaded_data = json.load(f)
        print(f"Loaded data: {loaded_data}")
        
        # Clean up
        os.remove("sample_output.json")
        print("Sample file cleaned up.")
        
    except Exception as e:
        print(f"File operation error: {e}")

if __name__ == "__main__":
    # Run the main demonstration
    main()
    
    # Show additional concept demonstrations
    demonstrate_specific_concepts()
    
    print("\n" + "="*60)
    print("STUDENT MANAGEMENT SYSTEM EXAMPLE COMPLETE")
    print("="*60)
    print("\nThis example serves as a comprehensive reference for")
    print("implementing the final project assignment.")
    print("\nKey takeaways for students:")
    print("1. Break complex problems into smaller, manageable functions")
    print("2. Use appropriate data structures for different purposes")
    print("3. Implement proper error handling and input validation")
    print("4. Create user-friendly interfaces with clear feedback")
    print("5. Organize code logically with good documentation")
    print("6. Test features thoroughly with sample data")
    print("7. Save and backup data regularly")
    print("\nGood luck with your final project!")
