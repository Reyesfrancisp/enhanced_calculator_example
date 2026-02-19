"""Basic arithmetic operations."""
import math
from app.exceptions import DivisionByZeroError

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b

def power(a: float, b: float) -> float:
    return math.pow(a, b)

def root(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Root degree cannot be zero.")
    return math.pow(a, 1/b)