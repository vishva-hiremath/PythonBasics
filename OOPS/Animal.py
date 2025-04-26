# class definition: The blueprint for creating Animals
class Animal:
    # The __init__ method is a special 'constructor' method.
    # It runs automatically when you create a new object from this class.
    # 'self' refers to the specific object being created.
    def __init__(self, species, name, age):
        print(f"Creating a new Animal: {name}")
        self.species = species # Attribute: data associated with the object
        self.name = name       # Attribute
        self.age = age         # Attribute
        self.is_awake = True   # Default attribute

    # Method: A function defined inside a class (behavior)
    def eat(self, food):
        print(f"{self.name} the {self.species} is eating {food}.")

    # Method
    def sleep(self):
        self.is_awake = False
        print(f"{self.name} is now sleeping.")

    # Method
    def wake_up(self):
        self.is_awake = True
        print(f"{self.name} woke up!")

# Creating objects (instances) of the Animal class
lion = Animal(species="Lion", name="Leo", age=5)
penguin = Animal(species="Penguin", name="Pingu", age=2)

# Now we have two distinct Animal objects
print(f"{lion.name} is {lion.age} years old.") # Accessing attributes
print(f"{penguin.name}'s species is {penguin.species}.")

# Calling methods on the objects
lion.eat("a zebra")
penguin.sleep()

print(f"Is Leo awake? {lion.is_awake}")   # Output: True
print(f"Is Pingu awake? {penguin.is_awake}") # Output: False