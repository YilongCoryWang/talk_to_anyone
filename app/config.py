import os
from dotenv import load_dotenv

load_dotenv()  # This will read the .env file

LLM_API_KEY = os.getenv("LLM_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")