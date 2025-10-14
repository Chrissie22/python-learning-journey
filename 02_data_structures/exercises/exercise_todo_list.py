"""
Practice Exercise: To-Do List Manager ✅

This exercise introduces useful list operations in Python:
- Checking a list's size
- Removing items by position
- Sorting items alphabetically

Goal:
Build a simple program to manage a to-do list. You will:
1. Add tasks to a list
2. Remove a completed task
3. Sort the remaining tasks

Instructions:
- Create a file named exercise_todo_list.py in your 02_data_structures/exercises/ folder.
- Initialize an empty list called tasks.
- Use a for loop (range(3)) to prompt the user for three tasks, appending each to the tasks list.
- After the loop, print the full list and the number of tasks using len().
- Remove the first task (index 0) with tasks.pop(0) to mark it as complete.
- Sort the remaining tasks alphabetically with tasks.sort().
- Print the final sorted list of tasks.
"""


tasks = []

# --- STEP 1: Get all the tasks ---
# This loop's only job is to fill the 'tasks' list.
# Notice that only the input and append lines are indented here.
print("Please enter 3 tasks.")
for i in range(3):
    new_task = input("Enter a task: ")
    tasks.append(new_task)

# --- STEP 2: Print the initial list (AFTER the loop is done) ---
# Now that the loop is finished, this code runs only ONCE.
# The `\n` just adds a blank line for nice spacing.
print("\nYour tasks are:", tasks)

# The len() function gets the number of items in a list.
# We put it in an f-string to print it nicely.
print(f"You have {len(tasks)} tasks to do.")


# --- STEP 3: Complete a task ---
print("\nCompleting the first task...")
# The .pop(0) method removes the item at index 0.
tasks.pop(0)


# --- STEP 4: Sort the remaining tasks ---
# The .sort() method sorts the list alphabetically.
tasks.sort()


# --- STEP 5: Print the final list ---
print("Your final tasks are sorted:", tasks)
    
    
    
    