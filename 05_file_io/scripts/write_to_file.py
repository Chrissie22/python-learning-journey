# We use 'with open' to safely open and close the file.
# The 'w' means we're opening it in 'write' mode.

with open("journal.txt", "w") as file:
    file.write("This is my first journal entry.\n")
    file.write("I am learning about file I/o in python.\n")
    file.write("It's fun")
print("The file 'journal.txt' has been created and saved.")