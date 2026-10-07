from llm_client import ask

def process_text(text: str) -> dict:
    summary_prompt = f"Сделай короткое summary текста:\n\n{text}"
    summary = ask(summary_prompt)

    key_points_prompt = f"Выдели 3 ключевые мысли текста. Верни списком:\n\n{text}"
    key_points = ask(key_points_prompt)

    response_prompt = f"Дай короткий полезный ответ на текст:\n\n{text}"
    response = ask(response_prompt)

    return {
    "summary": summary + "\n\n",
    "key_points": key_points + "\n\n",
    "response": response,
}

