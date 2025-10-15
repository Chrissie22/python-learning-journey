"""
Area Calculator Exercise 📐

This script demonstrates how to create and use a reusable function for calculating the area of a rectangle.

Instructions:
- Define a function named `calculate_area` that takes two parameters: `width` and `height`.
- The function should multiply `width` by `height`, store the result in a variable called `area`, and return it.

Usage:
- Call `calculate_area` with different sets of dimensions to compute the area of multiple rectangles.
- Print the results for each calculation.

Expected Output:
The area of the first rectangle is: 50
The area of the second rectangle is: 600
"""


def calculate_area(width, height):
    area = width * height
    return area

area1 = calculate_area(5,10)
print(f"The area of the first rectangle is: {area1}")

area2 = calculate_area(20,30)
print(f"The area of the second rectangle is: {area2}")

