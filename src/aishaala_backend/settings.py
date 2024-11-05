from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='../.env', validate_default=False, extra='ignore')

    # APP Config
    DEBUG: bool = False
    API_PORT: int = 8000
    IS_USING_IMAGE_RUNTIME: bool = False

    LOG_DIR: str = '/tmp/logs'

    # DOWNLOAD_DIR on local = tmp/data/ , on server = /tmp/data/
    DOWNLOAD_DIR: str = '/tmp/data/'
    
    # GOOGLE_OAUTH2
    GOOGLE_OAUTH2_CLIENT_ID: str
    GOOGLE_OAUTH2_CLIENT_SECRET: str
    GOOGLE_OAUTH2_AUTH_URI: str
    GOOGLE_OAUTH2_REDIRECT_URI: str
    GOOGLE_OAUTH2_TOKEN_URI: str
    
    # Redis Config
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    # POSTGRESQL
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_PORT: int = 5433
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # AWS Configs
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str
    S3_BUCKET_NAME: str
    S3_BUCKET_REGION: str

    # Doc store and retrieval
    # DOC_STORE = s3 or http
    DOC_STORE: Literal['s3', 'http']

settings = Settings()  # type: ignore
