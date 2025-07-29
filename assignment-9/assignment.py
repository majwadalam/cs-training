# Assignment.py - Lesson 9: Advanced Student Management System
# Student Name: [Write your name here]
# Date: [Write today's date here]

"""
Assignment: Create an advanced data management system that processes student 
information using advanced list operations, list comprehensions, and nested lists.

Requirements:
1. Store student data in nested lists: [name, age, [grades], [subjects]]
2. Implement advanced list operations:
   - Sort students by different criteria (name, age, average grade)
   - Search for students by various criteria
   - Filter students based on conditions
3. Use list comprehensions for:
   - Calculating statistics
   - Filtering data
   - Transforming data
4. Provide comprehensive reporting features:
   - Student rankings
   - Grade analysis
   - Performance reports
5. Include data validation and error handling
6. Create an intuitive menu-driven interface

Example Student Data Structure:
[
    ["Alice", 18, [85, 92, 88, 95], ["Math", "Science", "English", "History"]],
    ["Bob", 19, [78, 85, 90, 87], ["Math", "Science", "English", "Art"]],
    ...
]

Example Output:
=== Advanced Student Management System ===

Menu Options:
1. Add new student
2. Display all students
3. Search students
4. Sort students
5. Generate reports
6. Filter students
7. Student statistics
8. Remove student
9. Update student grades
10. Quit

Choose option: 5

=== Student Reports ===
1. Top performers
2. Grade distribution
3. Subject analysis
4. Performance trends

Choose report: 1

=== Top Performers ===
Rank  Name     Average  Highest Grade
1     Alice    90.0     95
2     Carol    89.2     95  
3     Bob      85.0     90
...
"""

# TODO: Write your advanced student management system below

print("=== Advanced Student Management System ===")
print("Welcome to the Advanced Student Data Manager!")
print()

# TODO: Initialize student data structure
# students = [
#     ["Alice", 18, [85, 92, 88, 95], ["Math", "Science", "English", "History"]],
#     ["Bob", 19, [78, 85, 90, 87], ["Math", "Science", "English", "Art"]],
#     ["Carol", 18, [92, 88, 95, 90], ["Math", "Science", "English", "Music"]],
#     ["David", 20, [75, 80, 85, 82], ["Math", "Science", "PE", "Art"]],
#     ["Eve", 19, [95, 98, 92, 96], ["Math", "Science", "English", "History"]]
# ]

# TODO: Main program loop
# while True:
    # TODO: Display menu
    # TODO: Get user choice
    # TODO: Handle each option

# TODO: Helper functions using advanced list operations

def add_student(students, name, age, grades, subjects):
    """Add a new student to the system"""
    # Validate input and add student
    # students.append([name, age, grades, subjects])
    pass

def display_students(students, title="All Students"):
    """Display students in a formatted table"""
    # if not students:
    #     print("No students in the system.")
    #     return
    # 
    # print(f"=== {title} ===")
    # print(f"{'Name':<12} {'Age':<5} {'Average':<8} {'Grades'}")
    # print("-" * 50)
    # 
    # for student in students:
    #     name, age, grades, subjects = student
    #     avg = sum(grades) / len(grades) if grades else 0
    #     grades_str = ", ".join(map(str, grades))
    #     print(f"{name:<12} {age:<5} {avg:<8.1f} {grades_str}")
    pass

def calculate_average(grades):
    """Calculate average grade"""
    # return sum(grades) / len(grades) if grades else 0
    pass

def sort_students_by_average(students, reverse=True):
    """Sort students by average grade using list comprehension and sorting"""
    # return sorted(students, key=lambda s: sum(s[2]) / len(s[2]) if s[2] else 0, reverse=reverse)
    pass

def sort_students_by_name(students):
    """Sort students alphabetically by name"""
    # return sorted(students, key=lambda s: s[0])
    pass

def sort_students_by_age(students):
    """Sort students by age"""
    # return sorted(students, key=lambda s: s[1])
    pass

def search_students_by_name(students, name_query):
    """Search students by name (partial match)"""
    # return [s for s in students if name_query.lower() in s[0].lower()]
    pass

def filter_students_by_average(students, min_average):
    """Filter students with average >= min_average using list comprehension"""
    # return [s for s in students if sum(s[2]) / len(s[2]) >= min_average]
    pass

def filter_students_by_age(students, min_age, max_age):
    """Filter students by age range"""
    # return [s for s in students if min_age <= s[1] <= max_age]
    pass

def get_top_performers(students, n=5):
    """Get top N performers using advanced list operations"""
    # sorted_students = sort_students_by_average(students, reverse=True)
    # return sorted_students[:n]
    pass

def get_grade_statistics(students):
    """Calculate comprehensive grade statistics"""
    # all_grades = [grade for student in students for grade in student[2]]
    # 
    # if not all_grades:
    #     return None
    # 
    # stats = {
    #     'total_grades': len(all_grades),
    #     'average': sum(all_grades) / len(all_grades),
    #     'highest': max(all_grades),
    #     'lowest': min(all_grades),
    #     'above_90': len([g for g in all_grades if g >= 90]),
    #     'below_70': len([g for g in all_grades if g < 70])
    # }
    # 
    # return stats
    pass

def analyze_subject_performance(students):
    """Analyze performance by subject"""
    # subject_grades = {}
    # 
    # for student in students:
    #     name, age, grades, subjects = student
    #     for i, subject in enumerate(subjects):
    #         if i < len(grades):
    #             if subject not in subject_grades:
    #                 subject_grades[subject] = []
    #             subject_grades[subject].append(grades[i])
    # 
    # # Calculate averages for each subject
    # subject_averages = {
    #     subject: sum(grades) / len(grades) 
    #     for subject, grades in subject_grades.items()
    # }
    # 
    # return subject_averages
    pass

def generate_student_ranking(students):
    """Generate comprehensive student ranking"""
    # ranked_students = sort_students_by_average(students, reverse=True)
    # 
    # print("=== Student Rankings ===")
    # print(f"{'Rank':<6} {'Name':<12} {'Average':<8} {'Highest':<8} {'Lowest':<8}")
    # print("-" * 55)
    # 
    # for i, student in enumerate(ranked_students, 1):
    #     name, age, grades, subjects = student
    #     avg = sum(grades) / len(grades) if grades else 0
    #     highest = max(grades) if grades else 0
    #     lowest = min(grades) if grades else 0
    #     
    #     print(f"{i:<6} {name:<12} {avg:<8.1f} {highest:<8} {lowest:<8}")
    pass

def update_student_grades(students, student_name, new_grades):
    """Update grades for a specific student"""
    # for student in students:
    #     if student[0].lower() == student_name.lower():
    #         student[2] = new_grades
    #         return True
    # return False
    pass

def remove_student(students, student_name):
    """Remove a student from the system"""
    # for i, student in enumerate(students):
    #     if student[0].lower() == student_name.lower():
    #         removed = students.pop(i)
    #         return removed
    # return None
    pass

# Start your code here:

# Example structure:
# students = [
#     ["Alice", 18, [85, 92, 88, 95], ["Math", "Science", "English", "History"]],
#     ["Bob", 19, [78, 85, 90, 87], ["Math", "Science", "English", "Art"]],
#     ["Carol", 18, [92, 88, 95, 90], ["Math", "Science", "English", "Music"]],
#     ["David", 20, [75, 80, 85, 82], ["Math", "Science", "PE", "Art"]],
#     ["Eve", 19, [95, 98, 92, 96], ["Math", "Science", "English", "History"]]
# ]
# 
# while True:
#     print(f"\nCurrent students: {len(students)}")
#     print("\nMenu Options:")
#     print("1. Add new student")
#     print("2. Display all students")
#     print("3. Search students")
#     print("4. Sort students")
#     print("5. Generate reports")
#     print("6. Filter students")
#     print("7. Student statistics")
#     print("8. Remove student")
#     print("9. Update student grades")
#     print("10. Quit")
#     
#     choice = input("\nChoose option (1-10): ").strip()
#     
#     if choice == "1":
#         # Add student logic
#         name = input("Enter student name: ").strip()
#         try:
#             age = int(input("Enter student age: "))
#             grades_input = input("Enter grades (separated by commas): ")
#             grades = [int(g.strip()) for g in grades_input.split(",")]
#             subjects_input = input("Enter subjects (separated by commas): ")
#             subjects = [s.strip() for s in subjects_input.split(",")]
#             
#             students.append([name, age, grades, subjects])
#             print(f"Student {name} added successfully!")
#         except ValueError:
#             print("Invalid input! Please check your data.")
#     
#     elif choice == "2":
#         display_students(students)
#     
#     # Continue with other options...
#     
#     elif choice == "10":
#         print("Thank you for using the Advanced Student Management System!")
#         break
#     
#     else:
#         print("Invalid choice! Please choose 1-10.")
#     
#     input("\nPress Enter to continue...")  # Pause before showing menu again
