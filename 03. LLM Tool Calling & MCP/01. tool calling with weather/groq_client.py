import os

import requests


def call_groq(messages, tools):
    api_key = "YOUR_GROK_API_KEY"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": messages,
        "temperature": 0.0,
        "tools": tools,
    }

    response = requests.post(url, headers=headers, json=payload)
    print("response is ", response.json())
    return response.json()["choices"][0]["message"]
