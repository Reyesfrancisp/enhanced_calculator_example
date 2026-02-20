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
        self.history.add_observer(AutoSaveObserver())

    def calculate(self, op_name: str, a_str: str, b_str: str):
        try:
            a = validate_number(a_str)
            b = validate_number(b_str)
            strategy = OperationFactory.get_strategy(op_name)
            result = strategy.execute(a, b)
            self.history.add_record(op_name, a, b, result)
            display_result = int(result) if result.is_integer() else result
            print(f"  🟢 Result: {display_result}")
            
        except CalculatorException as e:
            print(f"  🔴 Error: {e}")
        except Exception as e:
            print(f"  🔴 Unexpected Error: {e}")

def repl():
    """Starts the REPL session."""
    calc = CalculatorFacade()
    
    # Modern UI Header
    print("\n" + "="*45)
    print(" 🚀  ENHANCED PROFESSIONAL CALCULATOR")
    print("="*45)
    print(" ➕➖ Math : add, subtract, multiply, divide, power, root")
    print(" 💾  Data : history, clear, undo, redo, save, load")
    print(" ❓  Misc : help, exit")
    print("-" * 45)

    while True:
        try:
            # Modern UI Prompt
            user_input = input("\n[Calculator] ➜ ").strip().lower()
        except EOFError:
            break

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0]

        if command == 'exit':
            print("  👋 Goodbye!\n")
            break
        elif command == 'help':
             print("  📌 Type an operation and two numbers (e.g., 'add 5 10')")
             print("  📌 Available commands: add, subtract, multiply, divide, power, root")
             print("  📌 Data commands: history, clear, undo, redo, save, load")
        elif command == 'history':
            calc.history.display()
        elif command == 'clear':
            calc.history.clear()
            print("  🧹 History cleared.")
        elif command == 'undo':
            if calc.history.undo():
                print("  ⏪ [Undo] Reverted to previous state.")
            else:
                print("  ⚠️  [Undo] Cannot undo. You are at the beginning of your history.")
        elif command == 'redo':
            if calc.history.redo():
                print("  ⏩ [Redo] Restored state.")
            else:
                print("  ⚠️  [Redo] Cannot redo. You are at the latest state.")
        elif command == 'save':
            if calc.history.save_history():
                print("  💾 History manually saved to CSV.")
            else:
                print("  🔴 Error saving history.")
        elif command == 'load':
            if calc.history.load_history():
                print("  📂 History manually loaded from CSV.")
            else:
                print("  ⚠️  No existing history found to load.")
        elif command in ['add', 'subtract', 'multiply', 'divide', 'power', 'root']:
            if len(parts) == 3:
                calc.calculate(command, parts[1], parts[2])
            elif len(parts) == 1:
                a = input("    ↳ Enter first number: ")
                b = input("    ↳ Enter second number: ")
                calc.calculate(command, a, b)
            else:
                print("  ⚠️  Usage: <operation> <x> <y>")
        else:
            print(f"  ❓ Unknown command '{command}'. Type 'help' for options.")

if __name__ == '__main__': # pragma: no cover
    repl()