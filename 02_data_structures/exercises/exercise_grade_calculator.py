"""
Grade Calculator Exercise 📝

This script combines key Python concepts: variables, user input, data type conversion, lists, loops, and conditional logic.

Goal:
- Prompt the user for the number of grades to enter.
- Collect each grade and store them in a list.
- Calculate the total and average of the grades.
- Display the grades, the average, and a result message based on the average.

Instructions:
1. Create an empty list to store grades.
2. Ask the user how many grades they want to enter (convert input to integer).
3. Use a loop to collect each grade, converting input to integer and appending to the list.
4. After collecting all grades, calculate the total and average.
5. Use conditional statements to print a result message based on the average:
    - "A - Excellent" for averages 70 and above
    - "C - Pass" for averages 50 and above
    - "F - Failed" for averages below 50

Example Interaction:
How many grades do you want to enter? 3
Enter grade: 80
Enter grade: 55
Enter grade: 92

Your grades are: [80, 55, 92]
Your average is: 75.66
Result: A - Excellent

Tip: Use the range() function to run a loop a specific number of times.
"""

grades = []
num_grades = int(input("How many grades do you want to enter?: "))

# --- STEP 1: Get all the grades ---
# This first loop's only job is to fill the 'grades' list. It's perfect.
print("--- Enter Grades ---")
for i in range(num_grades):
    grade = int(input("Enter grade: "))
    grades.append(grade)

# --- STEP 2: Calculate the total and average ---
# This part happens AFTER the first loop is finished.
# The sum() function is a great shortcut to add up every number in a list.
total = sum(grades)
average = total / len(grades)

# --- STEP 3: Print the results and make a decision ---
# I really like that you added more detailed grade conditions! Let's use them.
print("\n--- Results ---")
print(f"Your grades are: {grades}")
print(f"Your average is: {average}")

if average >= 70:
    print("Result: A - Excellent")
elif average >= 50:
    print("Result: C - Pass")
else:
    print("Result: F - Failed")