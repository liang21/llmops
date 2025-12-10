from langchain_classic.memory.chat_memory import BaseChatMemory

memory = BaseChatMemory(input_key="query", output_key="answer", return_messages=True)

memory_variables = memory.load_memory_variables({"query": "你好"})

print(memory_variables)
