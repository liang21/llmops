from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话?")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

ai_messages = llm.batch([prompt.format(subject="程序员"), prompt.format(subject="Python"), ])

for message in ai_messages:
    print(message.content)

