"""
  Settings
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class Settings"""
    main_url: str


settings = Settings()
