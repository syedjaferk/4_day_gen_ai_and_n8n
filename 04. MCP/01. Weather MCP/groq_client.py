import os

import requests
from dotenv import load_dotenv

load_dotenv()


def call_groq(messages, tools):
    try:
        print("Messages ", messages)
        print("#" * 30)
        print("tools", tools)
        print("#" * 40)
        input()

        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": "Bearer YOUR_GROK_API_KEY",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "openai/gpt-oss-120b",
            "messages": messages,
            "tools": tools,
            "temperature": 0,
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30,
        )

        data = response.json()

        return data["choices"][0]["message"]
    except Exception as ex:
        print(ex)
        input()
