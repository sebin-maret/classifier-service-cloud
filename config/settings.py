from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    port: int
    host: str = "0.0.0.0"
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')


app_settings = Settings()
