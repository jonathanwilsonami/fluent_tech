"""
Def: Assertions in Python are statements that allow you to test assumptions made by your program. An assertion is a sanity check that you can turn on 
or turn off when you’re done with your testing of the program.
Usage: assert condition, message

__debug__ is a built-in constant in Python that is True by default. It is used to check if the interpreter is running in optimized mode. 
If Python is started with the -O (optimize) flag, __debug__ is set to False.

The __debug__ constant is often used in conjunction with assertions or other debugging and testing code to ensure that certain checks are only performed when the interpreter is not optimized.

Purpose:
- to check invariants that should always be true else it would be a bug
- commonly used in testing. 

Note:
- Assertions are not run when python is run in optimized mode. 
- Assertions are for debugging: They should not be used for handling runtime errors that could occur due to user input or other external factors.
- Assertions can be disabled: When Python is run with the -O (optimize) switch, all assertions are removed from the bytecode. 
  Therefore, assertions should not be used to perform essential operations in your code.
"""

def average(numbers):
    assert len(numbers) > 0, "The list is empty"
    return sum(numbers) / len(numbers)

def set_age(age):
    assert isinstance(age, int), "Age must be an integer"
    assert age > 0, "Age must be positive"

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        assert self.balance >= 0, "Initial balance must be non-negative"

    def deposit(self, amount):
        assert amount > 0, "Deposit amount must be positive"
        self.balance += amount

    def withdraw(self, amount):
        assert amount > 0, "Withdrawal amount must be positive"
        assert self.balance >= amount, "Insufficient funds"
        self.balance -= amount

# Unit testing 
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 5, "Should be 5"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
