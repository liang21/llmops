import os

import dotenv
from langchain_classic.chains.llm import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话?")

llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                api_key=os.getenv("DEEPSEEK_API_KEY"))
chain = LLMChain(llm=llm, prompt=prompt)

print(chain.invoke({"subject": "机器学习"}))