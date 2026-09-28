from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FitBuddy"
    database_url: str = "sqlite:///./fitbuddy.db"

    # Gemini
    gemini_api_key: str | None = None

    # These can be changed in .env depending on the models
    # available to your Google AI account.
    workout_model: str = "gemini-3.1-pro-preview"
    nutrition_model: str = "gemini-3.8-flash"

    # Admin protection
    admin_token: str = "change-me"

    # Feedback validation
    max_feedback_length: int = 2000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()