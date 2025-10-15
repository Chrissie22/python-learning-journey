numbers = [23, 44, 9, 71, 100, 52, 83]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print(f"original list: {numbers}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
        
        
    