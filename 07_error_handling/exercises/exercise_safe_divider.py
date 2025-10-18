"""Safe Divider Program: Division with Error Handling

Description:
This program performs division of two numbers with error handling for zero division.
It demonstrates proper use of try-except blocks for handling arithmetic errors.

Program Flow:
1. User inputs a numerator (top number)
2. User inputs a denominator (bottom number)
3. Program attempts division
4. Handles potential zero division error

Expected Input:
- Numerator: Any integer
- Denominator: Any non-zero integer

Example Usage:
Success case:
    Input:  10 (numerator), 2 (denominator)
    Output: Result: 5.0

Error case:
    Input:  10 (numerator), 0 (denominator)
    Output: Error: You cannot divide by zero!

Note: Both inputs must be valid integers.
"""

num_numerator = int(input("Enter a numerator (the number on top): "))
num_denominator = int(input(" Enter a denominator (the number on the bottom): "))

try:
    num_numerator = int(input("Enter a numerator (the number on top): "))
    num_denominator = int(input("Enter a denominator (the number on the bottom): "))
    result = num_numerator / num_denominator
    print(f"Result: {result}")
    
except ZeroDivisionError:
    print(f"Error: You cannot divide by zero!")
    
except ValueError:
    # This catches if the input wasn't a number
    print("Error: You must enter a valid number!")
    