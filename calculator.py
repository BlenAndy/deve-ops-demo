"""Simple calculator module with basic arithmetic operations."""
import logging
from typing import Union, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Numeric = Union[int, float]

def validate_numbers(a: Numeric, b: Numeric) -> None:
    """Validate inputs are numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numbers, got {type(a)} and {type(b)}")

def add(a: Numeric, b: Numeric) -> Numeric:
    """Return the sum of a and b."""
    validate_numbers(a, b)
    result = a + b
    logger.debug(f"Addition: {a} + {b} = {result}")
    return result

def subtract(a: Numeric, b: Numeric) -> Numeric:
    """Return the difference of a and b."""
    validate_numbers(a, b)
    result = a - b
    logger.debug(f"Subtraction: {a} - {b} = {result}")
    return result

def multiply(a: Numeric, b: Numeric) -> Numeric:
    """Return the product of a and b."""
    validate_numbers(a, b)
    result = a * b
    logger.debug(f"Multiplication: {a} * {b} = {result}")
    return result

def divide(a: Numeric, b: Numeric) -> float:
    """Return the division of a by b.
    
    Raises:
        ValueError: If b is zero.
        TypeError: If inputs are not numbers.
    """
    validate_numbers(a, b)
    
    if b == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")
    
    result = float(a) / float(b)
    logger.debug(f"Division: {a} / {b} = {result}")
    return result

def power(a: Numeric, b: int) -> Numeric:
    """Return a raised to the power of b.
    
    Args:
        a: Base number
        b: Exponent (limited to prevent DoS)
    
    Raises:
        ValueError: If exponent is too large (potential DoS attack)
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    
    # Security: Limit exponent to prevent DoS attacks (Bandit B605 fix)
    MAX_EXPONENT = 1000
    if isinstance(b, (int, float)) and abs(b) > MAX_EXPONENT:
        raise ValueError(f"Exponent too large (max {MAX_EXPONENT})")
    
    result = a ** b
    logger.debug(f"Power: {a} ** {b} = {result}")
    return result

def is_even(number: int) -> bool:
    """Return True if number is even.
    
    Args:
        number: Must be an integer
    
    Raises:
        TypeError: If number is not an integer
    """
    if not isinstance(number, int):
        raise TypeError(f"Number must be an integer, got {type(number)}")
    
    return number % 2 == 0