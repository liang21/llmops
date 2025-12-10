import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([("human", "{query}")])

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

chain = prompt|llm.bind(model="deepseek-chat")|StrOutputParser ()

content = chain.invoke({"query": "你是什么模型呢?"})
print(content)
