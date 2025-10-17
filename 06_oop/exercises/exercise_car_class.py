"""Car Class Exercise: Creating and Managing Car Objects 🚗

Description:
    This program demonstrates object-oriented programming by implementing a Car class
    that serves as a blueprint for creating car objects with specific attributes.

Class Structure:
    - Class Name: Car (using PascalCase convention)
    - Attributes: brand, model, year
    - Methods: __init__(brand_param, model_param, year_param)

Usage:
    1. Create Car objects with:
       - Brand (string)
       - Model (string)
       - Year (integer)
    2. Access object attributes using dot notation
    3. Print car details in formatted strings

Example Output:
    Car 1 is a 2021 Toyota Camry
    Car 2 is a 2022 Honda Civic
    
"""

class Car:
    def __init__(self, brand_param, model_param, year_param):
            
        self.brand = brand_param
        self.model = model_param
        self.year = year_param
        
car1 = Car("Toyota", "Camry", 2021)
car2 = Car("Honda", "Civic", 2022)

print(f"Car 1 is a {car1.year} {car1.brand} {car1.model}")
print(f"Car 2 is a {car2.year} {car2.brand} {car2.model}")