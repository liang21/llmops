import os
from operator import itemgetter

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

dotenv.load_dotenv()


def retrieve(query: str) -> str:
    print("正在检索...", query)
    return "这是检索结果"


prompt = ChatPromptTemplate.from_template("""请根据用户的问题回答，可以参考对应的上下文进行生成。

<context>
{context}
</context>

用户的提问是: {query}""")

llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                 api_key=os.getenv("DEEPSEEK_API_KEY"))
parser = StrOutputParser()

chain = RunnablePassthrough.assign(context=lambda x: retrieve(x["query"])) | prompt | llm | parser

content = chain.invoke({"query": "请讲一个关于机器学习的冷笑话?"})

print(content)
