# A tuple is created with parentheses ()
coordinates = (10, 20, 50)

print(f"My tuple of coordinates is: {coordinates}")

# You can access items by index, just like a list
x = coordinates[0]
print(f"The x coordinate is {x}")

# --- THE BIG DIFFERENCE ---
# If you try to change an item in a tuple, it will cause an error.
# The next line is commented out, but you can test it.
coordinates[0] = 15 

print("\nTuples are immutable. You can't add, remove, or change items!")