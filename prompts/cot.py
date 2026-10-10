from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN, and OUTPUT steps.
    You will need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rule:
    - Strictly follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user)

    Output JSON format:
    {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}

    Example:
    START: Hey, can you solve 2 + 2 * 5 / 10
    PLAN: {"step": "PLAN": "content": "Seems like user is interested in the maths problem"}
    PLAN: {"step": "PLAN": "content": "Looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step": "PLAN": "content": "Yes, The BODMAS is correct this to be done here."}
    PLAN: {"step": "PLAN": "content": "First we must multiple 3 * 5 which is 15"}
    PLAN: {"step": "PLAN": "content": "Now the new equation is 2 + 15/10"}
    PLAN: {"step": "PLAN": "content": "We must perform divide that is 15/10 = 1.5"}
    PLAN: {"step": "PLAN": "content": "Now the new equation is 2 + 1.5"}
    PLAN: {"step": "PLAN": "content": "Now finally perform the addition 3.5"}
    PLAN: {"step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as an ans"}
    OUTPUT: {"step": "OUTPUT": "content": "3.5"}

"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, can you add 3 + 5(3*8)/7+14"},
        # Manually keep adding messages to History
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The user wants to solve the mathematical expression: 3 + 5(3*8)/7 + 14. I will solve this using the BODMAS/PEMDAS order of operations."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "First, I will evaluate the expression inside the parentheses: (3 * 8)."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "3 * 8 is equal to 24."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Now, substitute 24 back into the expression: 3 + 5 * 24 / 7 + 14."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Next, perform the multiplication: 5 * 24. 5 * 24 is equal to 120."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Now, the expression is: 3 + 120 / 7 + 14."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Next, perform the division: 120 / 7. 120 / 7 is approximately 17.142857..."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Next, perform the division: 120 / 7. 120 / 7 is approximately 17.142857..."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I should represent the division as a fraction or decimal. As a fraction, 120/7 is 17 and 1/7."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "Now, perform addition. The expression is 3 + 120/7 + 14. This is equal to 17 + 120/7."})},
        {"role": "assistant", "content": json.dumps({"step": "OUTPUT", "content": "The result of the expression 3 + 5(3*8)/7 + 14 is 239/7, which is approximately 34.14 (or 34 and 1/7)."})},
        

    ]
)


print(response.choices[0].message.content)
