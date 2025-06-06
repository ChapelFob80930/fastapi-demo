from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str 
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()
# This class inherits from BaseSettings, which allows us to read environment variables
# need to instantiate the Settings class