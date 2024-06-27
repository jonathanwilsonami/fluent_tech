##### File input and output ##### 
# Questions
"""
How do you open a file for reading in Python?
How do you open a file for writing in Python?
What is the difference between the r and w modes when opening a file?
How can you read the entire content of a file into a string?
How can you write a string to a file?
How do you read a file line by line in Python?
How can you append to an existing file without overwriting its content?
Write a Python script to count the number of lines in a file.
How do you handle file exceptions using try-except in Python?
Write a Python script to read a file and print its content in reverse order.
"""

# with handles file and resource mang i.e. closes the file after it exits the with block. 
with open('data.txt') as file:
  for line in file:
    print(line, end="") #end omits the extra newline 
    
# Reading large file in chunks 
while(chunk := file.read(10000)):
  print(chunk, end='')
