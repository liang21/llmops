import os

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import ConfigurableField

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                 api_key=os.getenv("DEEPSEEK_API_KEY")).configurable_fields(
    ConfigurableField(id="llm"),
    default_key="gpt-3.5",
    gpt4=ChatOpenAI(model="gpt-4"),
    wenxin=QianfanLLMEndpoint(),
)

chain = prompt | llm | StrOutputParser()

content = chain.invoke({"query": "请讲一个关于机器学习的冷笑话?"}, config={"configurable": {"llm": "wenxin"}})

print(content)
