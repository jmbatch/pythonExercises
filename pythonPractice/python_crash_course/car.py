class Car:
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
        
    def read_odometer(self):
        """Print a statement showing the cars mileage."""
        print(f"This vehicle has {self.odometer_reading} miles on it.")
        
my_new_car = Car('toyota', 'sequoia', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()
my_new_car.odometer_reading = 50
my_new_car.read_odometer()
