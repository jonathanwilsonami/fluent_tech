"""
# Def: mutable data structures that allow you to store key-value pairs. Ordered by the when they are inserted. 
# Use Cases: Storing config settings, mapping user data, storing inventory data, presenting a graph, 

"""

student = {
    "name": "John",
    "age": 21,
    "courses": ["Math", "CompSci"]
}

# Bracket access vs get access
# The get method provides a way to access dictionary values more safely. If the key does not exist, it returns None (or a specified default value) instead of raising an error.

student["grade"] = "A"
del student["courses"]
student.clear()

for key, value in student.items():
    print(key, value)

# Graphs 
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

keys = ['a', 'b', 'c']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# Objects are first class objects. Using lambda functions. 
def format_value(value, format_type):
    formats = {
        "uppercase": lambda x: str(x).upper(),
        "lowercase": lambda x: str(x).lower(),
        "titlecase": lambda x: str(x).title(),
        "reverse": lambda x: str(x)[::-1],
        "hex": lambda x: hex(int(x)),
        "binary": lambda x: bin(int(x)),
        "octal": lambda x: oct(int(x)),
        "float": lambda x: f"{float(x):.2f}",
        "currency": lambda x: f"${float(x):.2f}",
        "percentage": lambda x: f"{float(x) * 100:.2f}%"
    }

    if format_type in formats:
        return formats[format_type](value)
    else:
        return "Invalid format type"

# Questions
"""
Medium:
How do you merge two dictionaries?
How do you use dictionary comprehension to create a dictionary?
How do you sort a dictionary by keys?
How do you sort a dictionary by values?
Explain the defaultdict from the collections module.
What is the setdefault method used for?
How do you invert a dictionary (swap keys and values)?
How can you safely remove a key from a dictionary without causing a KeyError?
What is the difference between items(), keys(), and values() methods?
How do you use the pop method with dictionaries?
How can you combine multiple dictionaries into one dictionary?
What are dictionary views and how do they differ from lists?
Explain how hash functions are used in dictionaries.
How do you handle missing keys when accessing dictionary values?
Describe how dictionaries are implemented in Python (e.g., hash tables).

Hard:
How can you merge two dictionaries such that the values of overlapping keys are combined into a list?
How can you merge two dictionaries and sum the values of overlapping keys?
Write a function to merge multiple dictionaries where the values of overlapping keys are concatenated strings.
How do you merge dictionaries stored in a list and handle overlapping keys by storing values in a set to avoid duplicates?
How can you merge dictionaries and create a new dictionary where the keys are the same and the values are lists of all values associated with those keys in the original dictionaries?
How would you merge two dictionaries by recursively merging nested dictionaries and summing the values of overlapping keys?
Write a function that merges a list of dictionaries where the keys are the same, and the values are combined into a list of unique values.
How can you merge dictionaries with keys representing dates and aggregate their values, assuming the values are numerical?
Write a function to merge dictionaries where the values are sets of elements, ensuring the merged dictionary has combined sets without duplicates.
How can you merge dictionaries by concatenating the string values of overlapping keys and retaining unique values for non-overlapping keys?
Explain the concept of dictionary views and how they differ from lists.
How do you handle nested dictionaries in Python?
What are some ways to improve the performance of dictionary operations?
Describe the time complexity of common dictionary operations.
How do you implement a multi-level dictionary update?
What is the ChainMap class from the collections module and how is it used?
Explain how to perform deep copying of dictionaries.
How can you flatten a nested dictionary structure?
How would you implement a dictionary-like class with additional functionality?
What are some common pitfalls and best practices when working with dictionaries in Python?
"""


