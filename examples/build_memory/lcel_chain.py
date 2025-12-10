import os

import dotenv
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.chat_models import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个强大的聊天机器人，能根据用户提供的上下文来回复用户的问题。\n\n<context>{context}</context>"),
     ("human", "{query}")])
llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                 api_key=os.getenv("DEEPSEEK_API_KEY"))

chain = create_stuff_documents_chain(prompt=prompt, llm=llm)
documents = [
    Document(page_content="小明喜欢绿色，但不喜欢黄色"),
    Document(page_content="小王喜欢粉色，也有一点喜欢红色"),
    Document(page_content="小泽喜欢蓝色，但更喜欢青色"),
]

content = chain.invoke({"query":"请帮我统计一下大家都喜欢什么颜色","context":documents})
print(content)