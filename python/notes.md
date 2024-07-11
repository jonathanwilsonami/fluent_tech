# General Python Notes
__Locale__ -  Refers to the set of cultural and linguistic conventions used by a computer program to format and display data such as dates, times, numbers, and currency in a way
that is familiar to users from a particular region or language.

```python
import locale

# Set locale to US English
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Format a number according to the current locale
number = 1234567.89
formatted_number = locale.format_string("%d", number, grouping=True)
print(formatted_number)  # Output: '1,234,567'

# Set locale to German
locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
```
__Garbage Collector__ - is a part of the Python memory management system that automatically frees up memory by removing objects that are no longer needed by the program. This helps prevent memory leaks and ensures that your program doesn't use more memory than necessary. It uses a concept of reference counting. Every Python has a ref count which keeps track of how many refs point to that
object. When the ref count drops to zero the object is no longer needed and Python can safly delete it. 

__Floating-point Numbers__ - In Python they are stored as IEEE 754 double-precision (64 bit) values. 

__Digit Seperator__ - 

```python
my_num = 2_000_000 # For better readability. Underscore is not read.
print(my_num)
# Output: 2000000
```

__Expression__ - Computation that evaluates to a concrete value. Combination of literal, names, operators and function or methods.

```python
val = 2 + 3 * 5 + sqrt(6+7) + c["a"] + b[1]
```

__Reference vs Copy__ - 
```python
a = [1,2,3]
b = a
c = a.copy()
d = copy.deepcopy(a)
```
b is a reference to a so any object that gets changed is also changed in the other.
c is a new object. 

__Shallow Copy__
Creates a new object but inserts refs into it. Changes to nested objects affect both the original and the copy. 

__Deep Copy__
New object created and recursivly adds copies of objects found in the originial. Changes to the original do not affect the copy even for nested items. 

__Object Equality__
- Equal when:
  - Lists/Tuples - equal size, equal elements, same order
  - Dict - same keys and items
  - Set - same elements
if x is y - tests the identities of x and y (memory location) not their actual values.

__Unpacking Items__

```python
a = [1,2,3]
d = {}
d["a], d["b"], d["c"] = a

items = [1,2,3,4,5]
a, *extra, b = items
# a = 1
# extra = [2,3,4]
# b = 5
# Example list of 3-parameter tuples
tuples_list = [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# Unpacking the tuples in a for loop
for x, y, z in tuples_list:
    print(f"x: {x}, y: {y}, z: {z}")
```
