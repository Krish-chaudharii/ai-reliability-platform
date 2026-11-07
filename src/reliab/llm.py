import os
from urllib import response

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def ask_model(question: str, model: str = "gemini-3.1-flash-lite") -> str:
    api_key = os.environ["GEMINI_API_KEY"]
    url = f"{BASE_URL}/{model}:generateContent"
    response = httpx.post(
        url,
        headers={"x-goog-api-key": api_key},
        json={"contents": [{"parts": [{"text": question}]}]},
        timeout=30.0,
    )
    response.raise_for_status()
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]
