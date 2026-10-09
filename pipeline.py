from llm_client import ask
from prompts import JSON_PROMPT, SYSTEM_PROMPT, FINAL_ANSWER_PROMPTS
import json
import logging
from schemas import LLMResponse
from pydantic import ValidationError

logger = logging.getLogger(__name__)


def process_text(text: str) -> LLMResponse:
    #summary = ask(SUMMARY_PROMPT.format(text=text))
    #key_points = ask(KEY_POINTS_PROMPT.format(text=text))
    #response = ask(RESPONSE_PROMPT.format(text=text))

    #raw = "это не JSON, проверка что ничего не упадет"

    raw = ask(JSON_PROMPT.format(text=text), system=SYSTEM_PROMPT)

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        logger.error("Модель вернула невалидный JSON: %s", e)
        logger.debug("Сырой ответ модели: %r", raw)
        raise
    try:
        result = LLMResponse.model_validate(data)
    except ValidationError as e:
        logger.error("JSON не прошёл валидацию схемы: %s", e)
        logger.debug("Разобранные данные: %r", data)
        raise

    answer_prompt = FINAL_ANSWER_PROMPTS.get(result.category)
    if answer_prompt is None:
        logger.warning("Неизвестная категория: %s", result.category)
        return result

    logger.info("Категория: %s | intent: %s", result.category, result.intent)

    result.final_answer = ask(
        answer_prompt.format(text=text),
        system=SYSTEM_PROMPT,
    )

    

