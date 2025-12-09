from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话?")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

resp = llm.stream(prompt.invoke({"subject": "机器学习"}))

for chunk in resp:
    print(chunk)
