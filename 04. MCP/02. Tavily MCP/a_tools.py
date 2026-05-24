import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

MCP_URL = f"https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_TAVILY_API_KEY"


async def chat():
    async with streamablehttp_client(MCP_URL) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools_response = await session.list_tools()

            print("\nAvailable Tools:\n")

            for tool in tools_response.tools:
                print("-", tool.name)

            tool_name = tools_response.tools[0].name

            print(f"\nUsing Tool: {tool_name}\n")

            while True:
                query = input("You: ")

                if query.lower() in ["exit", "quit"]:
                    print("Bye!")
                    break

                try:
                    result = await session.call_tool(tool_name, {"query": query})

                    print("\nAssistant:\n")
                    import json

                    for content in result.content:
                        if hasattr(content, "text"):
                            print(content.text)
                            results = json.dumps(content.text)
                        else:
                            print(content)
                            results = json.dumps(content)

                    for item in results.get("results", []):
                        print(item)
                        print("*" * 10)

                    print("\n" + "-" * 60 + "\n")

                except Exception as e:
                    print("\nError:")
                    print(e)
                    print()


if __name__ == "__main__":
    asyncio.run(chat())
