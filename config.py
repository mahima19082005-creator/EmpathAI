import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "EmpathAI: Emotion Drift Assisted Communication System"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Emotion Model Configuration
    # j-hartmann/emotion-english-distilroberta-base is the gold-standard 7-emotion transformer
    # Labels: anger, disgust, fear, joy, neutral, sadness, surprise
    DEFAULT_MODEL_NAME: str = (
        os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "models_cache", "emotion_distilroberta")
        if os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "models_cache", "emotion_distilroberta"))
        else "j-hartmann/emotion-english-distilroberta-base"
    )
    EMOTION_MODEL_NAME: str = os.getenv("EMOTION_MODEL_NAME", DEFAULT_MODEL_NAME)
    MODEL_CACHE_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "models_cache")
    
    # Emotion Drift Thresholds
    DRIFT_THRESHOLD_MODERATE: float = 0.30
    DRIFT_THRESHOLD_ACUTE: float = 0.55
    DRIFT_METHOD: str = "jensen_shannon"  # "jensen_shannon" or "cosine"
    
    # Generative AI Configuration
    GENERATIVE_PROVIDER: str = os.getenv("GENERATIVE_PROVIDER", "local")  # "local", "gemini", "openai"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Database
    DATABASE_URL: str = "sqlite:///./empathai.db"
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()
