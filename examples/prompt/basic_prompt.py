import datetime

from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话?")
print(prompt.format(subject="机器学习"))

chat_prompt = ChatPromptTemplate.from_messages([
    ("system","你是openai开发的聊天机器人,请根据用户的提问进行回复,当前时间是:{now}"),
    MessagesPlaceholder("history"),
    HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话?"),
    ]).partial(now=datetime.datetime.now())
chat_prompt_value = chat_prompt.invoke({
    "subject": "机器学习",
    "history":[
        ("human","你好"),
        AIMessage("你好,我是一个AI机器人,你可以向我提问任何问题"),
    ],
})

print(chat_prompt_value)