"""Practice Exercise: Amusement Park Tickets 🎟️
Amusement Park Ticket Price Calculator 🎟️
This script prompts the user to enter their age and determines the appropriate ticket price based on the following rules:
    - Child (under 5 years): Free admission
    - Kid (5 to 12 years): $10 ticket
    - Adult (13 to 64 years): $25 ticket
    - Senior (65 years and older): $15 ticket
The program uses an if/elif/else control flow to select the correct price category and displays a clear message with the ticket price.
Usage:
    Run the script and enter your age when prompted. The ticket price will be displayed.
Example:
    Your ticket price is $25.
In this exercise, you'll write a program that determines the ticket price for a person based on their age using an if/elif/else statement.

The Goal
Your task is to ask a user for their age and then print the correct ticket price based on the rules below.

Rules
Child (under 5): Free
Kid (5 to 12): $10
Adult (13 to 64): $25
senior (65 and up): $15

Step-by-Step Instructions
Setup: In your 03_control_flow/exercises/ folder, create a new file named exercise_ticket_price.py. (You'll need to create the exercises folder inside 03_control_flow first: mkdir exercises).

Get User Input: Ask the user to enter their age and store it in a variable as an integer.

Decision Logic: Write an if/elif/else statement to check the age and set a price variable.

The first if should check if the age is less than 5.

An elif should check if the age is between 5 and 12.

Another elif should check if the age is between 13 and 64.

The final else will handle anyone 65 and older.

Print the Result: Print the final price to the user in a clear message.

Hint: To check if a number is between two other numbers, you can use the and keyword, like this: if age >= 5 and age <= 12:

Example Output
Enter your age: 10
Your ticket price is $10.
Enter your age: 30
Your ticket price is $25."""


age = int(input("Enter your age: "))
price_message = ""

if age < 5:
    price_message = "Free"
elif age >= 5 and age <= 12:
    price_message = "$10"
elif age >= 13 and age <= 64:
    price_message = "$25"
else:
    price_message = "15"

print(f"Your ticket price is {price_message}.")
    
    