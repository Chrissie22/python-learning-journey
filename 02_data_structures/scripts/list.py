# Creating a list of strings
friends = ["Mary", "Ebere", "Jasmine"]

# You can access an item by its index(position). Python starts counting from 0!
first_friend = friends[0] # This will be "Mary"
second_friend = friends[1] # This will be "Ebere"

print(f"My friends are: {friends}")
print(f"My first friend is {first_friend}")

# You can also add a new item to the end of the list
friends.append("David")

print(f"I made a new friend! Now my friends are: {friends}")

# Let's change the name of the second friend (at index 1)

friends[1] = "Elizabeh"
print(f"After a change, the list is: {friends}")

# Now let's remove a friend by thier name
# Make sure you use a name that is actually in your list!

friends.remove("Jasmine")
print(f"After removing someone, the final list is: {friends}")
