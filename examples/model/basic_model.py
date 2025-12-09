from datetime import datetime

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

prompt = ChatPromptTemplate.from_messages( [
    ("system","你是OpenAI开发的聊天机器人,请回答用户的问题,现在的时间是{now}"),
    ("human","{question}"),
]).partial(now = datetime.now())

llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0.9)
prompt_value = prompt.invoke("query","现在是几点,请讲一个关于程序员的冷笑话")

ai_message = llm.invoke(prompt_value)
print("content:", ai_message.content)
