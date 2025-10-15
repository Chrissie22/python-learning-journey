def filter_passing_scores(scores, pass_mark):
    passing_scores = []
    for score in scores:
        if score >= pass_mark:
            passing_scores.append(score)   
    return passing_scores


student_scores = [88, 45, 92, 71, 59, 60 ,99]

passed_students = filter_passing_scores(student_scores, 70)

print(passed_students)