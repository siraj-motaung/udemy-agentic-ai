# Persona Based Promptinh.

from dotenv import load_dotenv
from openai import OpenAI
import json


load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Siraj Motaung.
    You are acting on behalf of Siraj Motaung who is 27 years old Tech enthusiatic and
    principal engineer. Your main stack is JS and Python and you are learning GenAI these days.

    Examples:
    Q: Hey
    A: Hey, Whats up!

"""


response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Hey, who are you?"},
        ],
    )

print("Response: ", response.choices[0].message.content)