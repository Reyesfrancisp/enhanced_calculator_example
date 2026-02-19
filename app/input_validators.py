"""Input validation utilities."""
from app.exceptions import InvalidInputError

def validate_number(value_str: str) -> float:
    """Validates and converts a string to a float (EAFP paradigm)."""
    try:
        return float(value_str)
    except ValueError:
        raise InvalidInputError(f"Invalid numeric input: '{value_str}'")