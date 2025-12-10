import os

import dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url=os.getenv("DEEPSEEK_BASE_URL"))

message_history = FileChatMessageHistory("memory.txt")

while True:
    query = input("Human:")
    if query == "exit":
        break
    print("AI:", flush=True, end=" ")
    system_prompt = (
        "你是OpenAI开发的ChatGPT聊天机器人，可以根据相应的上下文回复用户信息，上下文里存放的是人类与你对话的信息列表。\n\n"
        f"<context>{message_history}</context>\n\n"
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        stream=True,
    )
    ai_content = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break
        ai_content += content
        print(content, flush=True, end="")
    message_history.add_user_message(query)
    message_history.add_ai_message(ai_content)
    print("")
