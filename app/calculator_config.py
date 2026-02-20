"""Configuration management."""
import os
import logging
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

class Config:
    HISTORY_FILE = os.getenv("HISTORY_FILE", "data/history.csv")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls):
        """Validates configuration settings and handles errors gracefully."""
        if not isinstance(cls.HISTORY_FILE, str) or not cls.HISTORY_FILE.endswith('.csv'):
            print("  [Config Warning] Invalid HISTORY_FILE path. Defaulting to 'data/history.csv'")
            cls.HISTORY_FILE = "data/history.csv"
            
        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if cls.LOG_LEVEL.upper() not in valid_log_levels:
            print(f"  [Config Warning] Invalid LOG_LEVEL '{cls.LOG_LEVEL}'. Defaulting to 'INFO'")
            cls.LOG_LEVEL = "INFO"

# Run validation on startup
Config.validate()