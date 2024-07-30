import os

class Settings:
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
    MYSQL_DB = os.getenv("MYSQL_DB", "price_alert_db")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "db")
    MYSQL_PORT = os.getenv("MYSQL_PORT", 3306)
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    JWT_SECRET = os.getenv("JWT_SECRET", "your_secret_key")
    EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT = os.getenv("EMAIL_PORT", 587)
    EMAIL_USER = os.getenv("EMAIL_USER", "your_email@gmail.com")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "your_email_password")

settings = Settings()
