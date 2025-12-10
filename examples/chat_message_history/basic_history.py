from langchain_core.chat_history import InMemoryChatMessageHistory

history = InMemoryChatMessageHistory()
history.add_user_message("你好")
history.add_ai_message("你好")
print(history.messages)
