from langchain_core.prompts import PromptTemplate

prompt = (PromptTemplate.from_template("请讲一个关于{subject}的冷笑话?")
          + ",让我开心下"
          + "\n 使用{language}语言."
          )
print(prompt)
print(prompt.format(subject="机器学习", language="中文"))