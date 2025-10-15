print("--- Reading from To-Do List ---")

with open("tasks_to_read.txt", "r") as file:
    tasks = file.readlines()

count = 1
for task in tasks:
    # .strip() cleans up the invisible '\n' at the end of each line
    print(f"{count}. {task.strip()}")
    count += 1