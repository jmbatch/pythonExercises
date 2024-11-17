class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurants name is {self.restaurant_name} and has {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"This restaurant is now open!")
        
        
restaurant = Restaurant("The Bundgeon", "Hotdogs")
restaurant.describe_restaurant()
restaurant.open_restaurant()