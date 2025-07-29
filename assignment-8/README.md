# Assignment 8: Lists - Introduction and Basic Operations

## Learning Objectives
- Understand lists as collections of items
- Learn list creation and manipulation
- Practice accessing and modifying list elements
- Use lists with loops

## Topics Covered
- What are lists and why use them?
- Creating lists and accessing elements
- List methods: .append(), .insert(), .remove(), .pop()
- List slicing
- Lists and for loops
- len() function with lists

## Files in this Assignment

### 1. example.py
This file contains example code that demonstrates all the concepts we'll cover in class about lists and basic list operations. Study this code carefully and make sure you understand how each part works.

### 2. assignment.py
This is where you'll write your own code to complete the assignment. Follow the instructions in the comments within the file.

## Assignment Task
**Assignment 7:** Create a simple to-do list manager where users can add, remove, and display tasks.

## Instructions
1. Open `example.py` first to see how lists and list methods work
2. Then open `assignment.py` and follow the instructions
3. Run your program to make sure it works correctly
4. Make sure your code includes:
   - List creation and initialization
   - Adding items with .append() and .insert()
   - Removing items with .remove() and .pop()
   - List indexing and slicing
   - Iterating through lists with for loops
   - Using len() function with lists
   - Menu-driven interface for user interaction
   - Comments explaining your list operations

## Key Concepts to Practice
- **List Creation**: `[]`, `list()`, creating with initial values
- **List Access**: Using index `list[0]`, negative indexing `list[-1]`
- **List Modification**:
  - `.append(item)` - Add to end
  - `.insert(index, item)` - Add at specific position
  - `.remove(item)` - Remove first occurrence
  - `.pop()` - Remove and return last item
  - `.pop(index)` - Remove and return item at index
- **List Properties**: `len(list)`, checking if item exists with `in`
- **List Slicing**: `list[start:end]`, `list[::step]`
- **Lists with Loops**: Iterating through items

## To-Do List Manager Requirements
- Display a menu with options (add, remove, display, quit)
- Add new tasks to the list
- Remove tasks by name or index
- Display all current tasks with numbers
- Show task count and status
- Handle empty list situations
- Validate user input appropriately
- Allow marking tasks as complete (optional)

## How to Run Your Code
1. Open a terminal/command prompt
2. Navigate to this folder
3. Run: `python assignment.py`
4. Use the menu to manage your to-do list

## Getting Help
- Review the example.py file if you're stuck
- Ask questions during class
- Test your program with different list operations
- Practice list method combinations
- Check for edge cases (empty lists, invalid indices)

## Submission
Make sure your `assignment.py` file runs without errors and creates a functional to-do list manager with all required list operations and user interface features.
