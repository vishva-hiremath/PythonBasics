# Dog class inherits from Animal
from OOPS.Animal import Animal


class Dog(Animal): # Specify the base class in parentheses
    def __init__(self, name, age, breed):
        # Call the __init__ method of the parent class (Animal)
        # to handle the common attributes (species, name, age)
        super().__init__(species="Dog", name=name, age=age)
        self.breed = breed # Add an attribute specific to Dog

    # Add a method specific to Dog
    def bark(self):
        print(f"{self.name} says Woof!")
    def speak(self):
        print(f"{self.name} says Woof!")
    # We can also override methods from the parent class
    def eat(self, food="dog food"): # Provide a default food for dogs
        print(f"{self.name} the {self.breed} is happily eating {food}.")

# Create a Dog object
my_dog = Dog(name="Buddy", age=3, breed="Golden Retriever")

# Access inherited attributes and methods
print(f"{my_dog.name} is a {my_dog.species}.") # species is inherited
my_dog.sleep()                                 # sleep() is inherited

# Access new attributes and methods
print(f"Buddy's breed is {my_dog.breed}.")
my_dog.bark()

# Call the overridden method
my_dog.eat()
my_dog.eat("a bone") # Can still pass specific food