from OOPS.Animal import Animal, lion
from OOPS.Dog import Dog


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(species="Cat", name=name, age=age)
        self.color = color

    def speak(self):
        print(f"{self.name} says Meow!")

    # Override eat slightly differently
    def eat(self, food="tuna"):
        print(f"{self.name} the {self.color} cat gracefully eats {food}.")

# Add a speak method to Dog as well for demonstration


# --- Polymorphism in Action ---

buddy = Dog(name="Buddy", age=3, breed="Golden Retriever")
whiskers = Cat(name="Whiskers", age=4, color="Gray")

# Create a list of different Animal objects
zoo_animals = [buddy, whiskers, lion] # lion is an Animal object from earlier

# Iterate and call the same method ('eat') on different object types
print("\n--- Feeding Time ---")
for animal in zoo_animals:
    # We don't need to know if it's a Dog, Cat, or generic Animal.
    # We just know it has an 'eat' method. Python figures out which version to run.
    if animal.__class__.__name__ == 'Animal':
        animal.eat("Animal Food") # Each object executes its own version of eat()
    else:
        animal.eat()

# Another example with a method ('speak') that only exists in subclasses
print("\n--- Speaking Time ---")
for animal in zoo_animals:
    # We should check if the method exists before calling it
    if hasattr(animal, 'speak'):
        animal.speak() # Only Dog and Cat objects will speak
    else:
        print(f"{animal.name} the {animal.species} doesn't have a specific 'speak' method.")
