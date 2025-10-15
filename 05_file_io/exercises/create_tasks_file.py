tasks_to_write = [
    "Buy groceries",
    "Finish Python exercise",
    "Call a friend"
]

with open("tasks_to_read.txt", "w") as file:
    for task in tasks_to_write:
        # We add '\n' to put each task on a new line
        file.write(task + "\n")

print("Successfully wrote tasks to tasks_to_read.txt")
    