print("trying to convert user input....")

# We put the risky code inside the 'try' block

try:
    age_str = input("What is your age? ")
    age = int(age_str)
    print(f"In one year, you will be {age + 1} years old")
    
# The block run if a valueError happens insid ethe 'try' block

except ValueError:
    print("Whoops! That was not a valid number. Please enter digits only")
    
print("\nProgram finished.")