from pydantic import BaseModel, Field

class LLMResponse(BaseModel):

    summary: str = Field(description="Краткое summary текста")
    category: str = Field(description="Тип запроса")
    sentiment: str = Field(description="Тональность: positive/negative/neutral")
    key_points: list[str] = Field(description="3 ключевые мысли")
    final_answer: str = Field(description="Итоговый полезный ответ")