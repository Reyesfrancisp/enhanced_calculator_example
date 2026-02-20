import pytest
from unittest.mock import patch
from app.calculator_repl import CalculatorFacade, repl

@pytest.mark.parametrize("op, a, b, expected_out", [
    ('add', '1.5', '1.5', '🟢 Result: 3\n'),       # Tests the new integer formatting!
    ('add', '1.5', '1.0', '🟢 Result: 2.5\n'),     # Tests float retention
    ('divide', '10', '0', '🔴 Error: Cannot divide by zero'),
    ('add', 'a', '5', '🔴 Error: Invalid numeric input')
])
def test_facade_calculate(op, a, b, expected_out, capsys):
    facade = CalculatorFacade()
    facade.calculate(op, a, b)
    captured = capsys.readouterr()
    assert expected_out in captured.out

@patch('app.calculation.OperationFactory.get_strategy', side_effect=Exception("Generic Boom"))
def test_facade_calculate_unexpected_error(mock_strategy, capsys):
    facade = CalculatorFacade()
    facade.calculate('add', '5', '5')
    captured = capsys.readouterr()
    assert "🔴 Unexpected Error: Generic Boom" in captured.out

@pytest.mark.parametrize("inputs, expected_out", [
    (['add 5 5', 'exit'], '🟢 Result: 10'),
    (['add', '5', '5', 'exit'], '🟢 Result: 10'),
    (['bad_command', 'exit'], '❓ Unknown command'),
    (['add 5', 'exit'], '⚠️  Usage: <operation> <x> <y>'),
    (['add 2 2', 'clear', 'history', 'exit'], 'History is empty.'), # Complex chained sequence
    (['', 'exit'], '👋 Goodbye!')
])
@patch('app.history.os.path.exists', return_value=False)
def test_repl_math_and_errors(mock_exists, inputs, expected_out, capsys):
    with patch('builtins.input', side_effect=inputs):
        repl()
        captured = capsys.readouterr()
        assert expected_out in captured.out

@pytest.mark.parametrize("command_chain, expected_out", [
    (['help', 'exit'], '📌 Available commands:'),
    (['history', 'exit'], 'History is empty.'),
    (['clear', 'exit'], '🧹 History cleared.'),
    (['undo', 'exit'], '⚠️  [Undo] Cannot undo.'),
    (['redo', 'exit'], '⚠️  [Redo] Cannot redo.'),
    (['save', 'exit'], '💾 History manually saved'),
    (['load', 'exit'], '⚠️  No existing history found to load.')
])
@patch('app.history.os.path.exists', return_value=False)
@patch('app.history.HistoryManager.save_history', return_value=True)
@patch('app.history.HistoryManager.load_history', return_value=False)
def test_repl_data_commands(mock_load, mock_save, mock_exists, command_chain, expected_out, capsys):
    with patch('builtins.input', side_effect=command_chain):
        repl()
        captured = capsys.readouterr()
        assert expected_out in captured.out

@pytest.mark.parametrize("command, patch_path, expected_out", [
    (['save', 'exit'], 'app.history.HistoryManager.save_history', '🔴 Error saving history.'),
    (['load', 'exit'], 'app.history.HistoryManager.load_history', '⚠️  No existing history found to load.')
])
@patch('app.history.os.path.exists', return_value=False)
def test_repl_save_load_failures(mock_exists, command, patch_path, expected_out, capsys):
    with patch(patch_path, return_value=False):
        with patch('builtins.input', side_effect=command):
            repl()
            captured = capsys.readouterr()
            assert expected_out in captured.out

@patch('app.history.HistoryManager.undo', return_value=True)
@patch('app.history.HistoryManager.redo', return_value=True)
@patch('app.history.HistoryManager.load_history', return_value=True)
def test_repl_success_branches(mock_load, mock_redo, mock_undo, capsys):
    with patch('builtins.input', side_effect=['undo', 'redo', 'load', 'exit']):
        repl()
        captured = capsys.readouterr()
        assert "Reverted to previous state" in captured.out
        assert "Restored state" in captured.out
        assert "History manually loaded" in captured.out

@pytest.mark.parametrize("error", [EOFError])
@patch('builtins.input')
def test_repl_eof(mock_input, error):
    mock_input.side_effect = error
    repl()  # Should exit cleanly without throwing error