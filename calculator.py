"""Simple calculator with intentional bugs for testing."""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def subtract_all(*numbers):
    """Subtract all numbers from the first number. Returns 0 for empty input."""
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(a, b):
    """Multiply two numbers."""
    # BUG: Missing return statement
    result = a * b

def divide(a, b):
    """Divide a by b."""
    # BUG: No zero division check
    return a / b

def greet(name):
    """Greet someone by name."""
    # BUG: Prints instead of returning
    print(f"Hello, {name}!")
