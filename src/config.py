from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SMPT_USER: str
    SECRET_AUTH: str
    SMPT_PASSWORD: str
    ROOT_EMAIL: str
    ROOT_PASSWORD: str
    FIRST_NAME: str
    SECOND_NAME: str
    ROOT_PHONE: str
    SUPER_USER: bool

    
    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file="../.env")
    
settings = Settings()



