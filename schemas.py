from pydantic import BaseModel, Field
from typing import Literal

class UserInput(BaseModel):
    query: str = Field(description="The user's research question")

class ModelOutput(BaseModel):
    answer: str = Field(description="Concise and precise answer")
    source: str = Field(description="URL or 'Internal Knowledge'")
    confidence: Literal["High", "Medium", "Low"] = Field(description="Confidence level of the answer")

    