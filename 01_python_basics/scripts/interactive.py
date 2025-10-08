# Ask the user for their name
user_name = input("What is your name? ")

# Ask the user for their birth year
birth_year_str = input("What year were you born? ")

#Convert the string to an integer
birth_year = int(birth_year_str)

# Do a simple calculation

current_year = 2025
age = current_year - birth_year

# Print a message back to the user
print(f"Hello, {user_name}! You are approximately {age} years old. ")