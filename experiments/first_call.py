import os

import httpx
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["GEMINI_API_KEY"]
model = "gemini-3.1-flash-lite"
url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

response = httpx.post(
    url,
    headers={"x-goog-api-key": api_key},
    json={"contents": [{"parts": [{"text": "What's the capital of India?"}]}]},
    timeout=30.0,
)
response.raise_for_status()
data = response.json()
print(data["candidates"][0]["content"]["parts"][0]["text"])