import os
from operator import itemgetter

import dotenv
from langchain_classic.memory import ConversationTokenBufferMemory
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from examples.chat_message_history.basic_history import history

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [("system", "你是openai开发的聊天机器人,请根据用户的提问进行回复"), ("human", "{query}")])

memory = ConversationTokenBufferMemory(return_messages=True, input_key="query", llm=ChatOpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=os.getenv("DEEPSEEK_BASE_URL")))

llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                 api_key=os.getenv("DEEPSEEK_API_KEY"))
chain = RunnablePassthrough.assign(
    history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
) | prompt | llm | StrOutputParser()
while True:
    query = input("Human:")
    if query == "exit":
        break
    chain_input = {"query": query,"language":"中文"}
    response = chain.stream(chain_input)
    print("AI:", flush=True, end=" ")
    output = ""
    for chunk in response:

        output += chunk
        print(chunk, flush=True, end="")
    memory.save_context(chain_input, {"output":output})
    print("")
    print("history:", memory.load_memory_variables({}))
