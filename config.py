import os
from dotenv import load_dotenv

load_dotenv()

API_KEY: str = os.getenv("OPENAI_API_KEY", "")
MODEL: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

if not API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY не задан. Скопируйет .env.example в .env и вставь свой ключ."
    )