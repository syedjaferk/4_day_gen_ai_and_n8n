import os
import json
from groq import Groq
from tools import tools
from validator import validate_sql
from db import execute_query


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_db(user_input):

    messages = [
        {"role": "system", "content": """
            You are a database assistant.
            Generate ONLY safe SELECT queries.
            Do not modify data.
        """},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        query = args["query"]

        print("\nGenerated SQL:\n", query)

        is_valid, reason = validate_sql(query)

        if not is_valid:
            return f"Query rejected: {reason}"

        result = execute_query(query)

        messages.append(message)
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })

        final_response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages
        )

        return final_response.choices[0].message.content

    return message.content


if __name__ == "__main__":
    while True:
        user_query = input("\nYou: ")
        print("Assistant:", chat_with_db(user_query))
