# OOP Assignment in Python

# Assignment 1: Design Your Own Class!

# Step 1: Create a class (Example: Smartphone)
class Smartphone:
    # Step 3: Constructor to initialize unique values
    def __init__(self, brand, model, battery):
        self.brand = brand          # Attribute
        self.model = model          # Attribute
        self.battery = battery      # Attribute

    # Step 2: Add methods
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}")

    def charge(self, amount):
        self.battery += amount
        print(f"{self.brand} {self.model} charged to {self.battery}%")

# Inheritance Example (Exploring polymorphism and encapsulation)
class SuperSmartphone(Smartphone):
    def __init__(self, brand, model, battery, ai_assistant):
        super().__init__(brand, model, battery)  # Inheriting from Smartphone
        self.ai_assistant = ai_assistant

    def use_ai(self):
        print(f"{self.brand} {self.model} is using AI Assistant: {self.ai_assistant}")


# Activity 2: Polymorphism Challenge!

# Base class
class Vehicle:
    def move(self):
        pass

# Subclass Car overrides move()
class Car(Vehicle):
    def move(self):
        print("Car is Driving")

# Subclass Plane overrides move()
class Plane(Vehicle):
    def move(self):
        print("Plane is Flying")

# Subclass Boat overrides move()
class Boat(Vehicle):
    def move(self):
        print("Boat is Sailing")


# --- TESTING THE CODE ---
# Create Smartphone objects
phone1 = Smartphone("Samsung", "Galaxy S24", 50)
phone1.make_call("+254700123456")
phone1.charge(30)

# Create SuperSmartphone object
super_phone = SuperSmartphone("Apple", "iPhone 15 Pro", 80, "Siri")
super_phone.make_call("+254700987654")
super_phone.use_ai()

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()

# End of Assignment
