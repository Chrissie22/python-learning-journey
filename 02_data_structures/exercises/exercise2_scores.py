"""🧩 Exercise: Calculate and Analyze Numbers
📝 Goal:

1. Write a Python program that:
2. Asks the user to enter 5 numbers.
3. Stores those numbers in a list.
4. Uses a for loop to calculate:
5.The sum of all numbers
7. The average
8. The largest number"""


numbers = []

for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)
total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)

print("\nNumbers entered:", numbers)
print("Sum:", total)
print("average", average)
print("Largest Number:", largest)