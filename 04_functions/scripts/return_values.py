# This function takes two numbers and RETURNS their sum.
# It doesn'nt print anything itself

def add_numbers(num1, num2):
    total = num1 + num2
    return total


# --- Let's use our function ---

# We call the function and store the value it returns in a variable

first_result = add_numbers(10,5) # first_result will become 15

# We can now use that result in other parts of our code.
second_result = add_numbers(first_result, 3) # This will be 15 + 3

print(f"The result of the first sum is: {first_result}")
print(f"The result of the second sum is: {second_result}")

