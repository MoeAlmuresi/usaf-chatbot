from pydantic import BaseModel
from typing import Optional
from datetime import date

class ChatRequest(BaseModel):
    message: str
