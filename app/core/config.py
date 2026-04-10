from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"
    FEATURE_DISTANCE_SEARCH: bool = False

    model_config = {
        "env_file": ".env",
        "extra": "ignore",  # Optional safety
    }


settings = Settings()