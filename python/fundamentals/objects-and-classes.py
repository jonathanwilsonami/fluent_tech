"""
Object - is an instance of a class. Objects can contain both data (known as attributes or properties) and methods (functions that belong to the object). Every object has a state and behavior.
Classes -  is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) can have.

Import - creates a new namespace or env and executes all the statements in the imported file within that namespace 
Packages - 3rd party packages are stored in site-packages directory. Find using sys.path. Ex: pandas.__file__ -> /usr/local/python3.8/site-packages/pandas/__init__.py

Encapsulation of Data and Functions: Classes are used to bundle data and functions that operate on that data together.
Inheritance: Classes can inherit attributes and methods from other classes.
Polymorphism: Allows methods to be used interchangeably among different classes.
Abstraction: Classes can hide complex details from the user.
Creating Custom Data Structures: Such as linked lists, stacks, queues, etc.
Data Modeling: Representing real-world entities (e.g., users, transactions).
Frameworks and Libraries: Many Python frameworks use classes to organize code (e.g., Django models).
"""

__repr__(self) #Great for debugging. Says how print should handle things
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        return f"Rectangle(width={self.width!r}, height={self.height!r})"

  type(self).__name___ # name of class

# data hiding 
self._a
self.__a

# Inheritance
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__('Dog')
        self.name = name
        self.age = age

    # Override 
    def make_sound(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.species)  # Output: Dog
print(my_dog.make_sound())  # Output: Woof!

# Questions
"""
Medium Difficulty
What is a class in Python, and how do you create one?
Explain the difference between a class and an instance.
What is inheritance in Python? Give an example.
How do you override a method in Python?
What is the purpose of the __init__ method?
How do you implement multiple inheritance in Python?
What is a class variable and an instance variable?
Explain method resolution order (MRO) in Python.
What is polymorphism? How can it be achieved in Python?
How do you use the super() function in Python?

Hard Difficulty
What are metaclasses in Python? How do you create and use them?
Explain the use of decorators in classes. Give an example.
What is the difference between __new__ and __init__ methods?
How do you implement the Singleton pattern in Python?
What are abstract base classes (ABCs) and how do you use them?
Explain the concept of duck typing in Python with an example.
How do you create a property in Python? What are the advantages?
What is a descriptor in Python, and how is it used?
How can you enforce type checking in a Python class?
What is the __slots__ attribute, and why would you use it?
How do you create a class decorator?
Explain the difference between @staticmethod and @classmethod.
How can you create immutable classes in Python?
What is the observer pattern, and how can it be implemented in Python?
How do you manage memory in a Python class?
What is a mixin class? Provide an example of its use.
How do you serialize and deserialize a Python object?
Explain the proxy pattern and provide an implementation in Python.
What is the difference between shallow copy and deep copy of objects?
How do you implement the Factory pattern in Python?
"""
