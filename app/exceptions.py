"""Custom exceptions for the calculator application."""

class CalculatorException(Exception):
    """Base class for all calculator exceptions."""
    pass

class InvalidOperationError(CalculatorException):
    pass

class DivisionByZeroError(CalculatorException):
    pass

class InvalidInputError(CalculatorException):
    pass