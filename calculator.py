"""Simple calculator with intentional bugs for testing."""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    # Fixed: Added missing return statement
    result = a * b
    return result

def divide(a, b):
    """Divide a by b."""
    # BUG: No zero division check
    return a / b

def greet(name):
    """Greet someone by name."""
    # BUG: Prints instead of returning
    print(f"Hello, {name}!")
