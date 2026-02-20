import pytest
from app.calculation import OperationFactory, CalculationStrategy
from app.exceptions import InvalidOperationError

@pytest.mark.parametrize("op_name, a, b, expected", [
    ('add', 5.5, 4.5, 10.0),
    ('subtract', 10, 5.5, 4.5),
    ('multiply', -2, 3, -6.0),
    ('divide', 10, 4, 2.5),
    ('power', 2, -1, 0.5),
    ('root', 27, 3, 3.0)
])
def test_operation_factory_valid(op_name, a, b, expected):
    strategy = OperationFactory.get_strategy(op_name)
    assert isinstance(strategy, CalculationStrategy)
    assert strategy.execute(a, b) == expected

@pytest.mark.parametrize("invalid_op", ["modulus", "unknown", "", "   ", "ADD"])
def test_operation_factory_invalid(invalid_op):
    with pytest.raises(InvalidOperationError):
        OperationFactory.get_strategy(invalid_op)