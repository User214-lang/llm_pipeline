from openai import OpenAI
from config import API_KEY, MODEL, BASE_URL
from prompts import SYSTEM_PROMPT

client = OpenAI(api_key=API_KEY, base_url = BASE_URL)

def ask(prompt: str, system: str | None = None) -> str:
    messages = []
    if system:
        messages.append({"role": "system", "content": SYSTEM_PROMPT})
    messages.append({"role": "user",   "content": prompt})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )

    return response.choices[0].message.content or ""