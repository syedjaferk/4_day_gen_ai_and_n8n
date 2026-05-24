import requests
from fastmcp import FastMCP

mcp = FastMCP("Weather Calculator MCP")


@mcp.tool()
def get_weather(city: str):
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": "0bbdc6d295d9e112eb3046697cb8f7d8",
            "units": "metric",
        }

        response = requests.get(
            url,
            params=params,
            timeout=5,
        )

        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }

    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def calculate(expression: str):
    try:
        result = eval(expression)

        return {
            "expression": expression,
            "result": result,
        }

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
