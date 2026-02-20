"""Input validation utilities."""
import math
from app.exceptions import InvalidInputError

def validate_number(value_str: str) -> float:
    """Validates and converts a string to a float using LBYL and EAFP paradigms."""
    
    # LBYL (Look Before You Leap): Clean up common formatting issues
    clean_val = str(value_str).strip()
    if not clean_val:
        raise InvalidInputError("Input cannot be empty.")
        
    # Remove commas so things like "1,000.50" are accepted
    clean_val = clean_val.replace(',', '')

    # EAFP (Easier to Ask Forgiveness): Attempt standard float conversion
    try:
        parsed_float = float(clean_val)
    except ValueError:
        raise InvalidInputError(f"Invalid numeric input: '{value_str}'")

    # LBYL (Look Before You Leap): Prevent Python's weird math edge cases
    # Python allows float('inf') and float('nan'), but a calculator shouldn't!
    if math.isnan(parsed_float) or math.isinf(parsed_float):
        raise InvalidInputError(f"Disallowed value: '{value_str}' (Infinity/NaN not supported).")

    return parsed_float