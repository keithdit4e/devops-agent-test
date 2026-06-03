"""Simple calculator with intentional bugs for testing."""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a + b  # BUG: Wrong operator - should be a - b

def multiply(a, b):
    """Multiply two numbers."""
    result = a * b
    return result

def divide(a, b):
    """Divide a by b."""
    return a / b  # BUG: No zero division check

def greet(name):
    """Greet someone by name."""
    return f"Hello, {name}!"
