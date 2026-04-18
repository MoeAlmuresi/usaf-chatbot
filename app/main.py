from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from openai import OpenAI

app = FastAPI()

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat(input: ChatRequest):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for USAF Construction LLC, a construction company based in Dearborn, MI. They offer new construction and remodeling services for residential and commercial properties. The owner is Usaf and can be reached at (313) 333-5790. Always be helpful, professional, and try to collect the customer's name and phone number so Usaf can follow up."},
            {"role": "user", "content": input.message}
        ]
    )

    return {"response": response.choices[0].message.content}




