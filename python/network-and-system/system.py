#### System #####
import sys
sys.argv[0] # Get name of program running 

# atexit - is a module in Python that provides a simple way to register functions that need to be executed upon the program's termination. 
# These functions are executed in the reverse order of their registration. This module is useful for cleanup activities, such as closing files, releasing resources, or saving state.
import atexit

def cleanup_function():
    print("Cleaning up before exiting...")

def save_state():
    print("Saving state...")

atexit.register(cleanup_function)
atexit.register(save_state)
db_connection = connect_to_database()
atexit.register(db_connection.close)
def notify_users():
    print("Application is exiting...")
atexit.register(notify_users)


# Questions 
"""
What is sys.argv in Python?
How do you import sys to use argv?
How can you print all the command-line arguments passed to a Python script?
How do you access the first command-line argument in a Python script?
How can you count the number of command-line arguments passed to a Python script?
Write a Python script that takes two command-line arguments and prints their sum.
How would you handle the case where no command-line arguments are passed to a Python script?
How can you convert command-line arguments to integers before performing arithmetic operations on them?
Write a Python script that takes a list of numbers as command-line arguments and prints the largest number.
Write a Python script that takes a filename as a command-line argument and prints the number of lines in the file.

What is the purpose of the sys module in Python?
How do you import the sys module in a Python script?
How can you access the command-line arguments using the sys module?
How do you use the sys.exit() function?
How can you find out the Python version being used to run a script using the sys module?
How do you get the path of the Python interpreter using the sys module?
Write a Python script using the sys module to print the current recursion limit.
How can you modify the system path to include a new directory using the sys module?
Write a Python script that uses the sys module to print the standard input, output, and error file objects.
How do you capture and handle exceptions using the sys module to print a custom error message and exit the program?

"""
