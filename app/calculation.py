"""Strategy and Factory design patterns for calculations."""
from app.operations import add, subtract, multiply, divide, power, root
from app.exceptions import InvalidOperationError

class CalculationStrategy:
    """Strategy context for executing operations."""
    def __init__(self, operation_func):
        self.operation_func = operation_func

    def execute(self, a: float, b: float) -> float:
        return self.operation_func(a, b)

class OperationFactory:
    """Factory to instantiate strategies."""
    _operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'power': power,
        'root': root
    }

    @classmethod
    def get_strategy(cls, operation_name: str) -> CalculationStrategy:
        if operation_name not in cls._operations:
            raise InvalidOperationError(f"Unknown operation: {operation_name}")
        return CalculationStrategy(cls._operations[operation_name])