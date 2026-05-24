import asyncio

from fastmcp import Client

client = Client("http://localhost:8000/mcp")


#
async def main():
    async with client:
        tools = await client.list_tools()
        for tool in tools:
            print(tool)

        result = await client.call_tool("add", {"a": 10, "b": 20})

        print(result)


asyncio.run(main())
