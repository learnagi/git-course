import os
from pathlib import Path

# API Configuration
BASE_URL = "http://localhost:8000"

# Login Credentials
LOGIN_CREDENTIALS = {
    "email": "admin@agi01.com",
    "password": "agi01agi01"
}

# Cache Configuration
CACHE_DIR = Path(os.path.expanduser("~/.cache/git-tutorial"))
TOKEN_CACHE_FILE = CACHE_DIR / "token.json"

# Retry Configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

# Logging Configuration
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = os.path.join(os.path.dirname(__file__), "tutorial_sync.log") 