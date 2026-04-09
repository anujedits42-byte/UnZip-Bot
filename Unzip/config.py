import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8274193303:AAE0-3mLMCYvZWHoz5rGf7jvKWjUHHAIddM")
    API_ID = int(os.environ.get("API_ID", 34446649))
    API_HASH = os.environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    MAX_FILE_SIZE = 2194304000
    
    
