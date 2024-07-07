"""

"""

# with handles file and resource mang i.e. closes the file after it exits the with block. 
with open('data.txt') as file:
  for line in file:
    print(line, end="") #end omits the extra newline 
    
# Reading large file in chunks 
while(chunk := file.read(10000)):
  print(chunk, end='')

with open('example.txt', 'w') as file:
    file.write("Hello, World!")

# Append 
with open('example.txt', 'a') as file:
    file.write("\nAppended text.")

# Copy contents of a file
with open('source.txt', 'r') as src, open('destination.txt', 'w') as dest:
    dest.write(src.read())

# Reading json
import json

with open('data.json', 'r') as file:
    data = json.load(file)
print(data)

# Write json
data = {'name': 'Alice', 'age': 30}
with open('output.json', 'w') as file:
    json.dump(data, file)

# Binary Read/Write
with open('image.jpg', 'rb') as file:
    content = file.read()
print(content[:20])  # Print first 20 bytes

data = b'\x89PNG\r\n\x1a\n'
with open('output.png', 'wb') as file:
    file.write(data)

# Serialize and Deserialize Python Objects
import pickle

data = {'name': 'Alice', 'age': 30}

# Serialize
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
print(loaded_data)

# Function to efficiently read and process lines from a file
def process_file(file_path):
    with open(file_path, 'r') as file:
        # Generator expression to read lines one by one
        lines = (line.strip() for line in file)
        
        # Process each line
        for line in lines:
            # Example processing: print lines that contain the word 'number'
            if 'number' in line:
                yield line

# Using the generator function to process the file
for processed_line in process_file('large_file.txt'):
    print(processed_line)

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

Medium Difficulty
Read a File: Write a function to read a text file and return its contents as a string.
Write to a File: Write a function that writes a given string to a text file.
Append to a File: Write a function that appends a given string to the end of a file.
Read Specific Lines: Write a function to read and return the first n lines of a file.
Copy File Contents: Write a function to copy the contents of one file to another.
Count Lines: Write a function to count the number of lines in a file.
Read CSV File: Write a function to read a CSV file and return its contents as a list of dictionaries.
Write CSV File: Write a function to write a list of dictionaries to a CSV file.
Read JSON File: Write a function to read a JSON file and return its contents as a dictionary.
Write JSON File: Write a function to write a dictionary to a JSON file.

Hard Difficulty
Read Binary File: Write a function to read a binary file and return its contents.
Write Binary File: Write a function to write binary data to a file.
Log File Analysis: Write a function to analyze a log file and return the number of occurrences of each log level (INFO, WARNING, ERROR).
File Encryption: Write a function to encrypt and decrypt a file using a simple encryption algorithm.
Merge Files: Write a function to merge the contents of multiple text files into one file.
Chunk File Reading: Write a function to read a large file in chunks and process each chunk.
File Search: Write a function to search for a specific string in a file and return the line numbers where it occurs.
File Permissions: Write a function to check and change the permissions of a file.
Temporary Files: Write a function to create and write data to a temporary file.
Data Serialization: Write a function to serialize and deserialize Python objects to and from a file using pickle.

Really Hard Difficulty
File Compression: Write a function to compress and decompress a file using gzip.
Memory-Mapped Files: Write a function to read a large file using memory-mapped file objects for efficient access.
File Locking: Write a function to implement file locking to prevent concurrent access to a file.
CSV to JSON: Write a function to convert a CSV file to a JSON file.
Generate Reports: Write a function to generate a report from a dataset and save it as a text file.
File Metadata: Write a function to read and modify file metadata (e.g., timestamps).
Directory Traversal: Write a function to traverse a directory and list all files and subdirectories.
Automated File Downloads: Write a function to download a file from a URL and save it locally.
Binary Data Processing: Write a function to read and process binary data from a file (e.g., image or audio file).
Concurrent File Access: Write a function to handle concurrent reading and writing to a file using threads or multiprocessing.
"""


