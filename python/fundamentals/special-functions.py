"""
Enumerate
"""
fruits = ["apple", "banana", "cherry"]
products = {}
for index, fruit in enumerate(fruits):
    products[index] = fruit
# {0: 'apple', 1: 'banana', 2: 'cherry'}

# Using enumerate with a custom start index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=100):
    print(index, fruit)

indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]


"""
Zip(s, t) - combines iterables s and t into an iterable of tuples stopping with the shortest of s and t if they are of unequal len
"""
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
"""
(1, 'a')
(2, 'b')
(3, 'c')
"""

# Unzipping a list of tuples
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*zipped)
"""
(1, 2, 3)
('a', 'b', 'c')
"""

# Creating a dictionary with zip
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
dictionary = dict(zip(keys, values))
"""
{'name': 'Alice', 'age': 25, 'city': 'New York'}
"""
