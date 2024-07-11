"""
Def: A context manager in Python is an object that is used to manage resources, such as file handling, network connections, and database connections. 
It provides a way to allocate and release resources automatically when they are no longer needed, ensuring proper cleanup and preventing resource leaks.

"""
# Example 3: Database Connection
import sqlite3

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO example (name) VALUES (?)', ('Alice',))
    conn.commit()

# Custom context manager:
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Enter the context")
    yield
    print("Exit the context")

# Custom Context Manager
with my_context_manager():
    print("Inside the context")

# File Handling example
"""
The contextlib module provides a simpler way to create context managers using the @contextmanager decorator. 

"""
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type is not None:
            print(f"Exception: {exc_val}")
        return False

# Using the custom file manager
with FileManager('example.txt', 'w') as file:
    file.write('Hello, World!')

# With contextlib
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Using the custom file manager
with file_manager('example.txt', 'w') as file:
    file.write('Hello, World!')
