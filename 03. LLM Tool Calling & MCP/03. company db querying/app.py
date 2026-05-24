import json

import requests
from mcp import FUNCTION_MAP, TOOLS

GROQ_API_KEY = "YOUR_GROK_API_KEY"

URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}


SYSTEM_PROMPT = f"""
You are an AI assistant.

You have access to these tools:

{json.dumps(TOOLS, indent=2)}

Rules:
1. Decide the best tool
2. Return ONLY valid JSON
3. Do not explain anything

JSON Format:

{{
    "tool_name": "tool_name",
    "arguments": {{
        "key": "value"
    }}
}}
"""


def ask_llm(user_prompt):
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0,
    }

    response = requests.post(URL, headers=HEADERS, json=payload)

    data = response.json()

    content = data["choices"][0]["message"]["content"]

    return content


def execute_tool(tool_response):
    parsed = json.loads(tool_response)

    tool_name = parsed["tool_name"]

    arguments = parsed["arguments"]

    function = FUNCTION_MAP[tool_name]

    result = function(**arguments)

    return result


while True:
    query = input("\nAsk Something: ")

    if query == "exit":
        break

    tool_response = ask_llm(query)

    print("\nTool Decision:")
    print(tool_response)

    final_result = execute_tool(tool_response)

    print("\nDatabase Result:")
    print(final_result)
