import pytest
import pandas as pd
from app.calculator_memento import HistoryMemento, HistoryCaretaker

@pytest.mark.parametrize("data", [
    {'val': [1]},
    {'val': [1, 2, 3]},
    {'val': []}
])
def test_memento_state(data):
    df = pd.DataFrame(data)
    memento = HistoryMemento(df)
    assert memento.get_state().equals(df)

@pytest.mark.parametrize("initial_data, next_data", [
    ({'val': [1]}, {'val': [1, 2]}),
    ({'a': [10]}, {'a': [10, 20]})
])
def test_caretaker_undo_redo(initial_data, next_data):
    caretaker = HistoryCaretaker()
    df1 = pd.DataFrame(initial_data)
    df2 = pd.DataFrame(next_data)
    
    caretaker.save_state(df1)
    
    restored_df, success = caretaker.undo(df2)
    assert success is True
    assert restored_df.equals(df1)
    
    redone_df, success = caretaker.redo(restored_df)
    assert success is True
    assert redone_df.equals(df2)

@pytest.mark.parametrize("empty_data", [{'val': []}])
def test_caretaker_empty_stacks(empty_data):
    caretaker = HistoryCaretaker()
    df = pd.DataFrame(empty_data)
    
    _, success = caretaker.undo(df)
    assert success is False
    
    _, success = caretaker.redo(df)
    assert success is False