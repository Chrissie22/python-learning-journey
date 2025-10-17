class Car:
    # The __init__ method sets up the attributes (the data)
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0 # All cars start with 0 mileage
        
    # --- This is a METHOD ---
    # It's a function inside the class that describes the car
    def get_description(self):
        # It uses 'self' to access the object's own attributes.
        return f"This car is a {self.year} {self.brand} {self.model}."
    
    # --- This is another METHOD ---
    # This one simulates driving the car, which changes an attribute.
    
    def drive(self, miles):
        print("vroom Vroom")
        self.mileage = self.mileage + miles

# --- Let's create an object and use its methods ---
my_car = Car("Honda", "Civic", 2022)

# Call the get_description method

description = my_car.get_description()
print(description)

# Check the car's initial mileage
print(f"Initial milleage: {my_car.mileage}")

# Call the drive method to add 50 miles
my_car.drive(50)

# Check the mileage again
print(f"Mileage after driving: {my_car.mileage}")
