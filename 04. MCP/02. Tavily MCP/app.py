import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

MCP_URL = "https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_TAVILY_API_KEY"


async def chat():
    async with streamablehttp_client(MCP_URL) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            print("Connected to Tavily MCP")
            print("Type 'exit' to quit\n")

            while True:
                query = input("You: ")

                if query.lower() in ["exit", "quit"]:
                    print("Bye!")
                    break

                try:
                    result = await session.call_tool("search", {"query": query})

                    print("\nAssistant:\n")

                    for content in result.content:
                        print(content.text)

                    print("\n" + "-" * 60 + "\n")

                except Exception as e:
                    print("Error:", e)


if __name__ == "__main__":
    asyncio.run(chat())
