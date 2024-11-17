class Users:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def describe_user(self):
        print(f"\nThis users name is {self.first_name} {self.last_name}.")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! You are now an object to be used in any way I desire.")
        print(f"You will receive {self.age} spankings.\n")
        

first_user = Users("Jared", "Batchelor", 36)
first_user.describe_user()
first_user.greet_user()