import os

import dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_community.chat_models import ChatOpenAI
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory

dotenv.load_dotenv()

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = FileChatMessageHistory(f"chat_history_{session_id}.txt")

    return store[session_id]


prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个强大的聊天机器人，请根据用户的需求回复问题。"), MessagesPlaceholder("history"),
     ("human", "{query}"), ])
llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                 api_key=os.getenv("DEEPSEEK_API_KEY")
                 )

chain = prompt | llm | StrOutputParser()

with_message_chain = RunnableWithMessageHistory(chain, get_session_history, input_messages_key="query",
                                                history_messages_key="history", )

while True:
    query = input("Human：")
    if query == "exit":
        break

    response = with_message_chain.stream({"query": query}, config={"configurable": {"session_id": "muxiaoke"}})
    print("AI：", flush=True, end="")
    for chunk in response:
        print(chunk, flush=True, end="")
    print("")
