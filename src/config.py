import os

class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(24).hex())
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Loaded from .env
