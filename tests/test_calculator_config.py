import pytest
from app.calculator_config import Config

@pytest.mark.parametrize("invalid_file", [123, None, "history.txt", "", "   "])
def test_config_validation_invalid_file(invalid_file):
    original_file = Config.HISTORY_FILE
    Config.HISTORY_FILE = invalid_file
    Config.validate()
    assert Config.HISTORY_FILE == "data/history.csv"
    Config.HISTORY_FILE = original_file  

@pytest.mark.parametrize("invalid_level", ["SUPER_DEBUG", "TRACE", "123", "", "info "])
def test_config_validation_invalid_log_level(invalid_level):
    original_log = Config.LOG_LEVEL
    Config.LOG_LEVEL = invalid_level
    Config.validate()
    assert Config.LOG_LEVEL == "INFO"
    Config.LOG_LEVEL = original_log