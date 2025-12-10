import random

import dotenv
from langchain_core.runnables import RunnableLambda

dotenv.load_dotenv()


def get_weather(location: str, unit: str, name: str) -> str:
    print("location:", location)
    print("unit:", unit)
    print("name:", name)
    return f"{location}天气为{random.randint(24, 40)}{unit}"


get_weather_runnable = RunnableLambda(get_weather).bind(unit="C", name="小慕")

content = get_weather_runnable.invoke("广州")

print(content)
