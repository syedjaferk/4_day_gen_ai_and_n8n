import json

from fastmcp import Client
from groq_client import call_groq
from tools_desc import tools


async def chat(user_input, tools):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant",
        },
        {
            "role": "user",
            "content": user_input,
        },
    ]

    response = call_groq(messages, tools)

    tool_calls = response.get("tool_calls")

    if tool_calls:
        tool_call = tool_calls[0]

        function_name = tool_call["function"]["name"]

        arguments = json.loads(tool_call["function"]["arguments"])

        print("\nTool Call:", function_name)
        print("Arguments:", arguments)

        async with Client("mcp_server.py") as client:
            list_tools = await client.list_tools()
            for tool in list_tools:
                print(tool)
            input("wait .....")

            result = await client.call_tool(
                function_name,
                arguments,
            )

        tool_result = result.data

        print("\nTool Result:", str(tool_result), type(tool_result))
        input("..............")

        messages.append(response)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "content": json.dumps(tool_result),
            }
        )

        final_response = call_groq(
            messages,
            tools,
        )

        return final_response["content"]

    return response["content"]


if __name__ == "__main__":
    import asyncio

    while True:
        query = input("\nYou: ")

        if query.lower() == "exit":
            break

        answer = asyncio.run(chat(query, tools))

        print("\nAssistant:", answer)
