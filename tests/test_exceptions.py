import pytest
from app.exceptions import CalculatorException, InvalidOperationError, DivisionByZeroError, InvalidInputError

@pytest.mark.parametrize("exception_class, message", [
    (CalculatorException, "Base error"),
    (InvalidOperationError, "Invalid operation requested"),
    (DivisionByZeroError, "Cannot divide by zero"),
    (InvalidInputError, "Invalid input provided")
])
def test_exceptions_raise(exception_class, message):
    with pytest.raises(exception_class, match=message):
        raise exception_class(message)