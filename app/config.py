from pydantic import BaseSettings


class Settings(BaseSettings):
    database_password: str = "localhost"
    database_username: str = "root"
    secret_key: str = "123456789"


settings = Settings()
