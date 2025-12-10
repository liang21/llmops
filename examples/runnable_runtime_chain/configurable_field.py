import os

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import ConfigurableField

dotenv.load_dotenv()

prompt = PromptTemplate.from_template("请生成一个小于{x}的随机整数")

llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                 api_key=os.getenv("DEEPSEEK_API_KEY")).configurable_fields(
    temperature=ConfigurableField(
        id="llm_temperature",
        name="大语言模型的温度",
        description="大语言模型的温度，范围0-1，默认为0.9",
    )
)

chain = prompt|llm|StrOutputParser ()
content = chain.invoke({"x":1000})
print( content)

print("----------------------")