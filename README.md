# Enhanced Professional Calculator

A robust, command-line calculator application built in Python. This project features a continuous Read-Eval-Print Loop (REPL), advanced history tracking using Pandas, and state traversal (Undo/Redo) using the Memento design pattern.

## Features & Design Patterns
* **Advanced Math:** Addition, Subtraction, Multiplication, Division, Power, and Root operations.
* **Pandas Data Management:** Calculations are saved to a Pandas DataFrame and auto-saved to a CSV file.
* **Design Patterns Used:**
  * **Facade:** Simplifies the complex subsystems into a single interface.
  * **Strategy & Factory:** Dynamically routes and executes mathematical operations.
  * **Observer:** Automatically monitors calculation events to trigger auto-saves.
  * **Memento:** Safely stores deep-copies of history state, enabling full `undo` and `redo` capabilities.
* **Robust Error Handling:** Utilizes both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission) paradigms to prevent crashes.

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/Reyesfrancisp/enhanced_calculator_example.git
cd enhanced_calculator_example
```

2. **Create and activate a virtual environment:**

```bash
# Windows
python -m venv venv
source venv/Scripts/activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```Bash
pip install -r requirements.txt
```

4. **Setup Environment Variables**:

Create a .env file in the root directory to configure the application:

```Plaintext

ENVIRONMENT=development
LOG_LEVEL=INFO
HISTORY_FILE=data/history.csv
```
5. **Usage Instructions**:

Start the application by running:

```Bash
python main.py
```

## Available Commands
Once the REPL starts, you can use the following commands:

| Command | Usage | Description |
| :--- | :--- | :--- |
| **`add`** | `add 5 10` | Adds two numbers. |
| **`subtract`** | `subtract 10 4` | Subtracts the second number from the first. |
| **`multiply`** | `multiply 6 7` | Multiplies two numbers. |
| **`divide`** | `divide 8 2` | Divides the first number by the second. |
| **`power`** | `power 2 3` | Raises the first number to the power of the second. |
| **`root`** | `root 9 2` | Calculates the nth root of the first number. |
| **`history`** | `history` | Shows a pandas table of past calculations. |
| **`clear`** | `clear` | Clears the current calculation history session. |
| **`undo`** | `undo` | Reverts the history to the previous state. |
| **`redo`** | `redo` | Restores an undone history state. |
| **`save`** | `save` | Manually saves the current history to the CSV file. |
| **`load`** | `load` | Manually loads history from the CSV file. |
| **`help`** | `help` | Displays the available commands. |
| **`exit`** | `exit` | Exits the application. |

## Testing

This application maintains 100% test coverage. To run the tests and view the coverage report:

```Bash
python -m pytest --cov=app --cov-report=term-missing tests/
```