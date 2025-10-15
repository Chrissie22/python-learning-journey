# We open the file in 'r' mode for reading
with open("journal.txt", "r") as file:
     # The .read() method reads all the text into a single string.
     contents = file.read()
     
print(" ---Redaing from journal.txt ---")
print(contents)
print("---End of file --")
    