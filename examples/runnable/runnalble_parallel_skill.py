import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

dotenv.load_dotenv()

# 1、编排prompt
joke_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话?")
poem_prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的诗?")

# 2、创建大语言模型
llm = ChatOpenAI(model="deepseek-chat", temperature=0.9)

parser = StrOutputParser()

joke_chain = joke_prompt | llm | parser
poem_chain = poem_prompt | llm | parser

map_chain = RunnableParallel(joke=joke_chain, porm=poem_chain)

res = map_chain.invoke({"subject": "机器学习"})
print(
    res
)
