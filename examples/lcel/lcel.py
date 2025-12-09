import os

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()
prompt = ChatPromptTemplate.from_template("{query}")
llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),api_key=os.getenv("DEEPSEEK_API_KEY"))
parser = StrOutputParser()

chain = prompt | llm | parser
content = chain.invoke({"query": "请讲一个关于机器学习的冷笑话?"})
print(content)