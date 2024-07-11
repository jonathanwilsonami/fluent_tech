"""
Def: Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions 
and are not unconditionally fatal [1].

Suggestions & Recomendations 
- You should only catch exceptions from which your code can actually recover. If recovery is not possible then it's often better to let the exception propagate. 
- Don't catch exceptions that can't be handle at that specific location in the code. 
- Make exceptions as specific as possible 
- Make your own exceptions as needed 
"""

# Arrtibutes 
e.args # A tuple of arguments given to the exception constructor. This is typically a single string describing the error.
e.__traceback__ # This attribute holds the traceback object, which contains the stack trace at the point where the exception was raised.
e.__cause__ # This attribute stores the direct cause of the exception if it was raised using the raise ... from ... syntax.
e.__context__ # This attribute stores the previous exception if another exception was raised while handling it.
e.details # Gives you a dict with the offending variable name as key and the value of the variable as the item value i.e. Error details: {'value': -1}

# Using multiple exceptions: 
try:
    # Code that may raise multiple exceptions
    result = 10 / 0  # This will raise a ZeroDivisionError
    my_list = [1, 2, 3]
    print(my_list[10])  # This will raise an IndexError
except (ZeroDivisionError, IndexError) as e:
    print(f"An error occurred: {e}")
  
# Can use else and finally to run code no matter what exception is caught 
# try:
# except:
# else:
# finally:

# Eception Hierarchy (built-in exception classes): 
"""
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
"""

# Custom Exception
class CustomError(Exception):
    
    def __init__(self, message, code, details=None, timestamp=None):
        super().__init__(message)
        self.code = code
        self.details = details
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.__class__.__name__}: {self.args[0]} (code: {self.code}, details: {self.details}, timestamp: {self.timestamp})"
      
# Raise the Custom Exception
from datetime import datetime

def check_value(value):
    if value < 0:
        raise CustomError(
            "Negative value error", 
            400, 
            details={"value": value}, 
            timestamp=datetime.now().isoformat()
        )
      
# Handle the Custom Exception
try:
    check_value(-1)
except CustomError as e:
    print(f"Custom error occurred: {e}")
    print(f"Error code: {e.code}")
    print(f"Error details: {e.details}")
    print(f"Error timestamp: {e.timestamp}")
    print(f"Error args: {e.args}")
    print(f"Traceback: {e.__traceback__}")
