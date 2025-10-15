def assign_grades(score_list, passing_mark):
    result_list = []
    for score in score_list:
        if score >= passing_mark:
            result_list.append("Pass")
        else:
            result_list.append("Fail")
    return result_list            

student_scores = [88, 45, 92, 71, 59, 60, 99]


grade_result = assign_grades(student_scores, 70)

print(f"Original scores: {student_scores}")
print(f"Grade results: {grade_result}")