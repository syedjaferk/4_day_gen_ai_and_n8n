# main.py
import json
import os

from functions import calculate, get_weather
from groq_client import call_groq
from tools import tools

available_functions = {"get_weather": get_weather, "calculate": calculate}


def chat_with_tools(user_input):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Use only text format with a-zA-Z0-9 characters",
        },
        {"role": "user", "content": user_input},
    ]

    message = call_groq(messages, tools)

    if message["tool_calls"]:
        tool_call = message["tool_calls"][0]
        function_name = tool_call["function"]["name"]
        arguments = json.loads(tool_call["function"]["arguments"])

        print(f"Tool Called: {function_name}")
        print("Arguments:", arguments)
        input("press enter")
        function_to_call = available_functions[function_name]
        function_response = function_to_call(**arguments)
        print(function_response)
        input("press enter")
        messages.append(message)
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "content": json.dumps(function_response),
            }
        )

        second_response = call_groq(messages, tools)

        return second_response
    return message["content"]


if __name__ == "__main__":
    while True:
        query = input("\nYou: ")
        answer = chat_with_tools(query)
        print("Assistant:", answer)
