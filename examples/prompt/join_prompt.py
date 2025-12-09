from langchain_core.prompts import ChatPromptTemplate

system_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是openai开发的聊天机器人,请根据用户的提问进行回复,我叫{username}")
    ]
)

human_template = ChatPromptTemplate.from_messages(
    [
        ("human","{question}"),
    ]
)
prompt = system_template + human_template
print(prompt)
print(prompt.format(username="小王",question="请讲一个关于机器学习的冷笑话?"))