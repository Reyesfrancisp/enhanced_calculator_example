import pytest
from unittest.mock import patch
from app.calculator_repl import CalculatorFacade, repl

@pytest.mark.parametrize("op, a, b, expected_out", [
    ('add', '5', '5', '🟢 Result: 10.0'),
    ('divide', '10', '0', '🔴 Error: Cannot divide by zero'),
    ('add', 'a', '5', '🔴 Error: Invalid numeric input')
])
def test_facade_calculate(op, a, b, expected_out, capsys):
    facade = CalculatorFacade()
    facade.calculate(op, a, b)
    captured = capsys.readouterr()
    assert expected_out in captured.out

@pytest.mark.parametrize("inputs, expected_out", [
    (['add 5 5', 'exit'], '🟢 Result: 10.0'),
    (['add', '5', '5', 'exit'], '🟢 Result: 10.0'),
    (['bad_command', 'exit'], '❓ Unknown command'),
    (['add 5', 'exit'], '⚠️  Usage: <operation> <x> <y>'),
    (['', 'exit'], '👋 Goodbye!')
])
def test_repl_math_and_errors(inputs, expected_out, capsys):
    with patch('builtins.input', side_effect=inputs):
        repl()
        captured = capsys.readouterr()
        assert expected_out in captured.out

@pytest.mark.parametrize("command_chain, expected_out", [
    (['help', 'exit'], '📌 Available commands:'),
    (['history', 'exit'], 'History is empty.'),
    (['clear', 'exit'], '🧹 History cleared.'),
    (['undo', 'exit'], '[Undo] Cannot undo.'),
    (['redo', 'exit'], '[Redo] Cannot redo.'),
    (['save', 'exit'], 'History manually saved'),
    (['load', 'exit'], 'No existing history found to load.')
])
@patch('app.history.HistoryManager.save_history', return_value=True)
def test_repl_data_commands(mock_save, command_chain, expected_out, capsys):
    with patch('builtins.input', side_effect=command_chain):
        repl()
        captured = capsys.readouterr()
        assert expected_out in captured.out

@pytest.mark.parametrize("error", [EOFError])
@patch('builtins.input')
def test_repl_eof(mock_input, error):
    mock_input.side_effect = error
    repl()  # Should exit cleanly without throwing error