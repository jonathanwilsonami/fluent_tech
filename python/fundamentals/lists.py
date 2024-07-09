##### Lists #####
# Def: Mutable ordered collection of arbitrary objects. Can be heterogeneous. 

# Common Methods:
"""
append(): Add an element to the end of the list.
extend(): Add multiple elements to the end of the list.
insert(): Insert an element at a specific position.
remove(): Remove the first occurrence of an element.
pop(): Remove and return an element at a specific position.
clear(): Remove all elements.
index(): Return the index of the first occurrence of an element.
count(): Return the number of occurrences of an element.
sort(): Sort the list.
reverse(): Reverse the list in place.
copy(): Return a shallow copy of the list.
zip(): takes multiple iterable objects (like lists, tuples, etc.) and aggregates them into a single iterable of tuples.
"""

a[1][1][2] # Access nested list
even_numbers = [x for x in my_list if x % 2 == 0] # List comprehension 
length_list = len(a) 

# zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
zipped_list = list(zipped)

print(zipped_list)
# [(1, 'a'), (2, 'b'), (3, 'c')]

numbers, letters = zip(*zipped_list) # unpack
print(numbers)  # Output: (1, 2, 3)
print(letters)  # Output: ('a', 'b', 'c')

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

dictionary = dict(zip(keys, values))
print(dictionary)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Questions
"""
Easy
- How do you create an empty list in Python?
- How can you add an element to the end of a list?
- How can you remove an element from a list by its value?
- What is the difference between append() and extend() methods?
- Write a Python script to create a list of numbers from 1 to 10.
- How can you sort a list in ascending order?
- How do you reverse the elements of a list?
- Write a Python script to find the largest number in a list of integers.
- How do you check if an element exists in a list?
- How do you find the intersection of two lists?
- How can you remove duplicate elements from a list?

Hard


How do you flatten a nested list?
How can you rotate a list by n positions?
How do you find the most common element in a list?
How do you split a list into evenly sized chunks?
How can you merge two sorted lists into one sorted list?
How do you find the second largest element in a list?
How do you generate all possible pairs from two lists?
How can you find all sublists of a list?
"""

# How do you create an empty list in Python?
a = []

# How can you add an element to the end of a list?
a.append('2')

# How can you remove an element from a list by its value?
my_list.remove("a") # removes only the first occurance of a
# could add an error handler too 
if value_to_remove in my_list:
    my_list.remove(value_to_remove)
else:
    print(f"Value {value_to_remove} not found in the list.")

# Write a Python script to create a list of numbers from 1 to 10
a = [i for i in range(1,11)]

# How can you sort a list in ascending order?
sorted_list = sorted(my_list)

# Write a Python script to find the largest number in a list of integers.
numbers = [4, 2, 8, 5, 1]
largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
# Or
largest_number = max(numbers) # O(n) time complexity

# Use of index
numbers = [1, 2, 3, 4, 3, 5, 3]

# Find the first occurrence of the number 3
index = numbers.index(3)
print(index)  # Output: 2

# Find the occurrence of the number 3 starting from index 3
index = numbers.index(3, 3)
print(index)  # Output: 4

# Find the occurrence of the number 3 between index 4 and 7
index = numbers.index(3, 4, 7)
print(index)  # Output: 6

# How do you find the intersection of two lists?
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Using & operator
intersection = list(set(list1) & set(list2))
print(intersection)  # Output: [4, 5]

intersection = np.intersect1d(list1, list2)
print(intersection)  # Output: [4 5]
