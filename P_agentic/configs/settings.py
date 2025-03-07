# configs/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

# ✅ Tavily API Key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise ValueError("⚠️ TAVILY_API_KEY is missing. Please check your .env file.")

# ✅ GROQ API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("⚠️ GROQ_API_KEY is missing. Please check your .env file.")
