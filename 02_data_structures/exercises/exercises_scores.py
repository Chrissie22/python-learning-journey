scores = [10, 25, 40, 5]
print(f"Here are the list of scores: {scores}")
scores.append(30)
scores[1] = 28

total_score = 0

for score in scores:
    total_score =  total_score + score

print(f"Total score is: {total_score}")
