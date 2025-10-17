# This is the BLUEPRINT for creating Dog objects.

class Dog:
    # The __init__ method is called automatically when a new Dog is created.
    def __init__(self, name_param, age_param):
        print(f"A new dog is being created!")
        
        # We use 'self' to create ATTRIBUTES (data) that belong to this specific dog.
        self.name = name_param
        self.age = age_param
        
# --- Let's create some objects (instances) from our blueprint ---

# This creates a Dog object and runs the __init__ method.
# "Rex" is passed to name_param, 5 is passed to age_param.

dog1 = Dog("Rex", 5)

# Let's create a second, separate Dog object.
dog2 = Dog("Buddy", 2)

# --- Accessing the attributes of each object ---
# We use dot notation (object.attribute) to get the data.

print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old")



    