import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Pilates Management API")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/pilates_db"
    )
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key")

settings = Settings()