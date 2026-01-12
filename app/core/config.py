import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENWEATHER_API_KEY: str = os.getenv("OPENWEATHER_API_KEY", "")
    CACHE_TTL: int = int(os.getenv("CACHE_TTL", "600"))  # 10 минут

settings = Settings()