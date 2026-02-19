"""Configuration management."""
import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

class Config:
    HISTORY_FILE = os.getenv("HISTORY_FILE", "data/history.csv")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")