"""🧩 Exercise: Even and Odd Number Analyzer
🎯 Goal:

Write a Python program that:

1. Asks the user to enter any number of values (until they type “done”).
2. Stores all the numbers in a list.
3. Separates the numbers into even and odd lists.
4. Calculates and prints:
5. The total count of numbers entered
6. The sum of even numbers
7. The sum of odd numbers """


numbers = []
evens = []
odds = []

while True:
    value = input("Enter a number (or type 'done' to finish): ")
    if value.lower() == "done":
        break
    numbers.append(int(value))

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print("\nTotal numbers entered:", len(numbers))
print("Even numbers:", evens)
print("Odd numbers:", odds)
print("Sum of even numbers:", sum(evens))
print("Sum of odd numbers:", sum(odds))