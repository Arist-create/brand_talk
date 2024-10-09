from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Test API"
    API_V1_STR: str = "/api/v1"


class DBConfig(BaseSettings):
    """Конфиги СУБД."""
    DATABASE_URI: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

db_settings = DBConfig()

settings = Settings()