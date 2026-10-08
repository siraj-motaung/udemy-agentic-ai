
from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from your environment")




client = OpenAI(
    api_key= api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = (
    "You should only and only answer to the coding related questions. "
    "Do not answer anything else. Your name is Siraj. "
    "If user asks something other than coding, just say SORRY."
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you write a python function to add two numbers"}
    ]
)

print(response.choices[0].message.content)
