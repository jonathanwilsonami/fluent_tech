"""
Def - concise way to create generators without needing to define a separate generator function using the yield keyword. They are similar to list comprehensions but use parentheses 
instead of square brackets. They allow you to iterate over large datasets without loading the entire dataset into memory, providing an efficient way to handle data streams.
A generator expression returns an iterator that yields items one at a time. They are memory-efficient because they generate items on-the-fly rather than storing the entire sequence in memory.

(expression for item in iterable if condition)

Use Cases:
- Processing large files line-by-line
- Lazy evaluation in data pipelines
- Many more

"""
# Process large file 
lines = (line for line in open('large_file.txt'))


# Questions 
"""
Medium Difficulty
What is a generator expression in Python, and how does it differ from a list comprehension?
Write a generator expression to find all even numbers between 1 and 100.
How can you use a generator expression to filter out lines containing a specific keyword from a large text file?
Explain how generator expressions improve memory efficiency.
Demonstrate how to sum squares of all numbers from 1 to 100 using a generator expression.
How would you use a generator expression to flatten a nested list?
Write a generator expression to read a large CSV file and extract the second column of data.
Explain how a generator expression can be used within a function to process data streams.
Write a generator expression to create a dictionary from a list of tuples.
How can generator expressions be used to perform lazy evaluation in data processing pipelines?

Hard Difficulty
Implement a generator expression to find prime numbers up to a given limit using the Sieve of Eratosthenes.
How would you use a generator expression to parse and filter JSON data from a file?
Explain the differences between yield, generator functions, and generator expressions with examples.
Write a generator expression to simulate an infinite sequence of Fibonacci numbers.
How can generator expressions be used to handle real-time event streams or logs?
Demonstrate how to create a generator expression that combines elements from two lists into pairs.
Explain how to use a generator expression to perform streaming data processing without loading the entire dataset into memory.
Write a generator expression to compute the Cartesian product of two lists.
How can generator expressions be used in conjunction with itertools for advanced iteration techniques?
Implement a generator expression to generate all possible permutations of a given string.
How would you use a generator expression to read a binary file in chunks and process each chunk?
Write a generator expression to create a set of unique elements from an iterable.
Explain how to chain multiple generator expressions together to perform complex data transformations.
How can generator expressions be utilized for building and processing HTML content dynamically?
Write a generator expression to extract all keys from a list of dictionaries where the value meets a specific condition.
Explain how to use generator expressions to create custom iterators for specific tasks.
Demonstrate the use of generator expressions for efficient logging and monitoring of system events.
Write a generator expression to generate all possible combinations of elements from a list.
How can generator expressions be used to implement efficient mathematical computations on large datasets?
Explain the benefits and limitations of using generator expressions in concurrent programming.


"""
