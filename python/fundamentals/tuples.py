# Def: A tuple is a collection which is ordered and unchangeable. 

a = ()
b = (i,) # Single value

my_tuple = (1, 2, 3)
print(my_tuple[0])

# Unpacking a tuple into variables
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3

name, share, price = a # Tuple unpacking 
person = ("Alice", 30, "Engineer")

# Iterating over a list of tuples
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"x: {x}, y: {y}")
  
# Creating nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1][0])  # Output: 3

# Slicing a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:3])  # Output: (2, 3)

# Using count() method
my_tuple = (1, 2, 2, 3, 4)
print(my_tuple.count(2))  # Output: 2

from collections import namedtuple

# Creating a named tuple
Person = namedtuple('Person', 'name age')
p = Person(name="John", age=25)
print(p.name, p.age)  # Output: John 25


##### Questions 
"""
Medium 
How do you merge two tuples into one in Python?
Explain the immutability of tuples and how it affects their usage in Python.
How would you convert a tuple of tuples to a single flattened tuple?
Given a list of tuples, how would you sort it based on the second element of each tuple?
How can you swap two variables using tuples in Python?
How do you remove duplicate tuples from a list of tuples?
Explain how you can use tuples as dictionary keys.
How would you check if a tuple contains a certain element?
What is tuple unpacking and how is it used? Provide an example.
Given a list of tuples, how would you filter out tuples that contain a specific value?

Hard
How can you reverse a tuple in Python without converting it to a list?
Write a function that takes a tuple of integers and returns the product of all the elements.
How can you concatenate multiple tuples in Python using a single line of code?
Given a list of tuples, write a function to find the tuple with the maximum sum of elements.
How would you implement a function that converts a list of tuples into a dictionary where the first element of each tuple is the key and the second element is the value?
Explain how you would slice a tuple to obtain a subtuple from the original tuple. Provide an example.
How do you use named tuples in Python, and what are their advantages over regular tuples?
Given a list of tuples, write a function to group the tuples by the first element and sum the second elements.
How can you implement a tuple-based stack in Python, and what are the advantages of using tuples for this purpose?
Write a function that takes two tuples and returns their Cartesian product as a list of tuples.

Advanced
How would you implement a function to find the intersection of two tuples (elements common to both)?
Given a tuple of tuples, write a function to transpose the tuple (swap rows and columns).
Write a function that accepts a tuple of strings and returns a new tuple with the strings sorted in descending order of length.
Explain how you would efficiently check if two tuples contain the same elements, regardless of order.
How can you convert a tuple of integers into a single integer (concatenating the digits)?
Given a large tuple of integers, describe an efficient way to find the k most frequent elements.
Write a function that finds the longest common prefix of strings in a tuple.
Explain how you can use tuples to implement a simple immutable data structure.
How would you implement a function to find all pairs of elements in a tuple that sum up to a given target?
Given a tuple of tuples, write a function to merge the tuples by their first element, summing up the corresponding second elements.
"""
