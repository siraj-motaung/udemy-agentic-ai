from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI()

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

print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉🏽 ")

message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history,
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parse_result = json.loads(raw_result)

    if parse_result.get("step") == "START":
        print("🔥", parse_result.get("content"))
        continue

    if parse_result.get("step") == "PLAN":
        print("🧠", parse_result.get("content"))
        continue

    if parse_result.get("step") == "OUTPUT":
        print("🤖", parse_result.get("content"))
        break
    

print("\n\n\n")
