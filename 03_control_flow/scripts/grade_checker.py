# Get a score from the user

score_str = input("Enter the test score (0-100): ")
score = int(score_str)

# Decide the grade using the if/elif/else structure

# DEcide the grade using the if/elif/else structure

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
    
print(f"A score of {score} gets a grade of: {grade}")