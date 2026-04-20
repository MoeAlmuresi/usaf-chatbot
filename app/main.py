from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

app = FastAPI()

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: list[ChatMessage] = [] # Conversation History

@app.post("/chat/")
async def chat(input: ChatRequest):
    messages=[
            #   SYSTEM PROMPT
            {"role": "system", "content": "You are a helpful assistant for USAF Construction LLC, a construction company based in Dearborn, MI. They offer new construction and remodeling services for residential and commercial properties. The owner is Usaf and can be reached at (313) 333-5790. Always be helpful, professional, and try to collect the customer's name and phone number so Usaf can follow up."},
            #{"role": "user", "content": input.message}
    ]

    for msg in input.history:
        messages.append({"role": msg.role, "content": msg.content}) # ADD PAST MESSAGES

    messages.append({"role": "user", "content": input.message}) # ADD CURRENT MESSAGE

    response = client.chat.completions.create(  # PASS TO OPENAI
        model = "gpt-4o-mini",
        messages = messages
    )
    
    return {"response": response.choices[0].message.content}




