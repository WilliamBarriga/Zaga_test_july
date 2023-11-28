import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    base_url: str = os.getenv("BASE_URL")
    open_api_key: str = os.getenv("OPENAI_API_KEY")
    open_gpt_model: str = os.getenv("OPENAI_GPT_MODEL")