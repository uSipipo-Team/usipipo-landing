"""Configuración de la aplicación."""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Configuración de la aplicación."""

    # Flask
    FLASK_ENV: str = os.getenv("FLASK_ENV", "development")
    FLASK_DEBUG: bool = os.getenv("FLASK_DEBUG", "true").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key")

    # Application
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Site
    SITE_URL: str = os.getenv("SITE_URL", "https://usipipo.com")
    SITE_NAME: str = os.getenv("SITE_NAME", "uSipipo VPN")


settings = Settings()
