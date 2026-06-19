from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

EMAIL = os.getenv(
    "EMAIL"
)

APP_PASSWORD = os.getenv(
    "APP_PASSWORD"
)