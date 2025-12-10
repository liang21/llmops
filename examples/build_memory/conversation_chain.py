import os

import dotenv
from langchain_classic.chains.conversation.base import ConversationChain
from langchain_community.chat_models import ChatOpenAI

dotenv.load_dotenv()

llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                api_key=os.getenv("DEEPSEEK_API_KEY"))

chain = ConversationChain(llm=llm)

content = chain.invoke({"input": "你好，我是慕小课，我喜欢打篮球还有游泳，你喜欢什么运动呢？"})

print(content)

content = chain.invoke({"input": "根据上下文信息，请统计一下我的运动爱好有什么?"})

print(content)