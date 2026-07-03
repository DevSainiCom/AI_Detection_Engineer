from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """
    Application configuration.
    """

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gpt-5-mini",
    )

    APP_NAME = os.getenv(
        "APP_NAME",
        "AI Detection Engineer",
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )


settings = Settings()