import requests


def get_weather(city: str):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0bbdc6d295d9e112eb3046697cb8f7d8"
        response = requests.get(url, timeout=5)
        data = response.json()

        return data
    except Exception as e:
        return {"error": str(e)}


def calculate(expression: str):
    try:
        result = eval(expression)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
