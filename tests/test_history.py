import pytest
import os
import pandas as pd
from unittest.mock import patch
from app.history import HistoryManager, AutoSaveObserver

@pytest.mark.parametrize("ops_to_add", [
    [('add', 2, 2, 4)],
    [('add', 2, 2, 4), ('subtract', 10, 5, 5), ('multiply', 3, 3, 9)] # Multiple chained actions
])
@patch('app.history.pd.DataFrame.to_csv')
def test_history_manager_add_parameterized(mock_to_csv, ops_to_add):
    hm = HistoryManager()
    hm.add_observer(AutoSaveObserver())
    hm.clear()
    
    for op in ops_to_add:
        hm.add_record(*op)
        
    assert len(hm.df) == len(ops_to_add)
    assert hm.df.iloc[-1]['operation'] == ops_to_add[-1][0]
    assert hm.df.iloc[-1]['result'] == ops_to_add[-1][3]

@pytest.mark.parametrize("setup_ops", [
    [('add', 2, 2, 4), ('multiply', 5, 5, 25)]
])
@patch('app.history.pd.DataFrame.to_csv')
def test_history_undo_redo(mock_to_csv, setup_ops):
    hm = HistoryManager()
    hm.clear()
    for op in setup_ops:
        hm.add_record(*op)
        
    assert hm.undo() is True
    assert len(hm.df) == 1
    
    assert hm.undo() is True
    assert len(hm.df) == 0
    
    assert hm.redo() is True
    assert len(hm.df) == 1

@pytest.mark.parametrize("actions, expected_in_out", [
    ([], "History is empty."),
    ([('add', 1, 1, 2)], "add")
])
@patch('app.history.pd.DataFrame.to_csv')
def test_history_display(mock_to_csv, actions, expected_in_out, capsys):
    hm = HistoryManager()
    hm.clear()
    for action in actions:
        hm.add_record(*action)
    hm.display()
    captured = capsys.readouterr()
    assert expected_in_out in captured.out

@pytest.mark.parametrize("exists_return, expected", [
    (True, True),
    (False, False)
])
@patch('app.history.pd.read_csv')
@patch('app.history.os.path.exists')
def test_load_history(mock_exists, mock_read_csv, exists_return, expected):
    mock_exists.return_value = exists_return
    mock_read_csv.return_value = pd.DataFrame({'operation': ['add']})
    hm = HistoryManager()
    assert hm.load_history() is expected

@patch('app.history.pd.read_csv', side_effect=pd.errors.EmptyDataError)
@patch('app.history.os.path.exists', return_value=True)
def test_load_history_empty_data_error(mock_exists, mock_read_csv):
    hm = HistoryManager()
    assert hm.load_history() is False

@pytest.mark.parametrize("side_effect, expected", [
    (None, True),
    (Exception("Mock Error"), False)
])
@patch('app.history.pd.DataFrame.to_csv')
def test_save_history(mock_to_csv, side_effect, expected):
    mock_to_csv.side_effect = side_effect
    hm = HistoryManager()
    assert hm.save_history() is expected