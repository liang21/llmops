import os

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{subject}")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9).with_fallbacks(
    [ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                api_key=os.getenv("DEEPSEEK_API_KEY"))])

chain = prompt | llm | StrOutputParser()
content = chain.invoke({"subject": "你好,你是?"})
print(content)
