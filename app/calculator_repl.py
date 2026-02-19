"""Facade pattern and Read-Eval-Print Loop (REPL)."""
import sys
from app.input_validators import validate_number
from app.calculation import OperationFactory
from app.history import HistoryManager, AutoSaveObserver
from app.exceptions import CalculatorException

class CalculatorFacade:
    """Facade to manage the subsystems of the calculator."""
    def __init__(self):
        self.history = HistoryManager()
        # Register the observer for auto-saving to CSV
        self.history.add_observer(AutoSaveObserver())

    def calculate(self, op_name: str, a_str: str, b_str: str):
        try:
            a = validate_number(a_str)
            b = validate_number(b_str)
            strategy = OperationFactory.get_strategy(op_name)
            result = strategy.execute(a, b)
            self.history.add_record(op_name, a, b, result)
            print(f"  = Result: {result}")
        except CalculatorException as e:
            print(f"  ! Error: {e}")
        except Exception as e:
            print(f"  ! Unexpected Error: {e}")

def repl():
    """Starts the REPL session."""
    calc = CalculatorFacade()
    print("\n--- Enhanced Calculator ---")
    print("Commands: add, subtract, multiply, divide, power, root")
    print("Options: history, clear, undo, redo, help, exit\n")

    while True:
        try:
            user_input = input("Calc> ").strip().lower()
        except EOFError:
            break

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0]

        if command == 'exit':
            print("Goodbye!")
            break
        elif command == 'help':
             print("Type an operation and two numbers (e.g., 'add 5 10')")
        elif command == 'history':
            calc.history.display()
        elif command == 'clear':
            calc.history.clear()
            print("  History cleared.")
        elif command == 'undo':
            calc.history.undo()
            print("  Undo executed.")
        elif command == 'redo':
            calc.history.redo()
            print("  Redo executed.")
        elif command in ['add', 'subtract', 'multiply', 'divide', 'power', 'root']:
            if len(parts) == 3:
                calc.calculate(command, parts[1], parts[2])
            elif len(parts) == 1:
                a = input("  > Enter first number: ")
                b = input("  > Enter second number: ")
                calc.calculate(command, a, b)
            else:
                print("  ! Usage: <operation> <x> <y>")
        else:
            print(f"  ! Unknown command '{command}'.")

if __name__ == '__main__': # pragma: no cover
    repl()