import pytest
from app.input_validators import validate_number
from app.exceptions import InvalidInputError

@pytest.mark.parametrize("value, expected", [
    ("5", 5.0), ("-10.5", -10.5), ("0", 0.0)
])
def test_validate_number_valid(value, expected):
    assert validate_number(value) == expected

@pytest.mark.parametrize("value", ["abc", "5a", "", "None"])
def test_validate_number_invalid(value):
    with pytest.raises(InvalidInputError):
        validate_number(value)