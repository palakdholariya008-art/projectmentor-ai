import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "CapstonAI - AI Project Idea Generator and Mentor"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    
    PORT: int = int(os.getenv("PORT", "8080"))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "production")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    
    CORS_ORIGINS: list[str] = ["*"]
    RATE_LIMIT_GENERATE: str = "30/15minutes"
    RATE_LIMIT_STANDARD: str = "100/15minutes"

settings = Settings()
