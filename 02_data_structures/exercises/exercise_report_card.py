"""
Exercise: Student Report Card 🎓

Objective:
Work with Python dictionaries to store, update, and display a student's grades.

Instructions:
1. Create a dictionary named 'report_card' with the following initial key-value pairs:
    - "student_name": "Christabel"
    - "math": 85
    - "science": 92

2. Print the initial state of the report card.

3. Update the report card:
    - Increase the "math" grade by 5 points (from 85 to 90).
    - Add a new subject "history" with a grade of 88.

4. Print the final state of the report card to show all updates.

Location:
Save this script as 'exercise_report_card.py' in the '02_data_structures/exercises/' folder.
"""






report_card = {
    "student_name": "Christabel",
    "math": 85,
    "science": 92
}

print(f"initial report card: {report_card}")

report_card["math"] = report_card["math"] +5

report_card["history"] = 88

print(f"Final report card: {report_card}")