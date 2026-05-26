"""Simple calculator with intentional bugs for testing."""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    # BUG: Missing return statement
    result = a * b

def divide(a, b):
    """Divide a by b."""
    # BUG: No zero division check
    return a / b

def subtract_all(*args):
    """Subtract all subsequent arguments from the first argument.
    
    For empty input, returns 0 (analogous to sum() returning 0).
    
    Args:
        *args: Variable number of arguments
        
    Returns:
        int: Result of subtracting all subsequent args from first arg, or 0 if empty
    """
    if len(args) == 0:
        return 0
    
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def greet(name):
    """Greet someone by name."""
    # BUG: Prints instead of returning
    print(f"Hello, {name}!")
