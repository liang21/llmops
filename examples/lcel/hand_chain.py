import os
from typing import Any

from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 构建组件
prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话?")
llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),api_key=os.getenv("DEEPSEEK_API_KEY"))
parser = StrOutputParser()

class Chain:
    steps = list()

    def __init__(self,steps:list):
        self.steps = steps

    def invoke(self,input:Any) -> Any:
        for step in self.steps:
            input = step.invoke(input)
            print("步骤:",step)
            print("输出:",input)
            print("--------------------------------------------------")
        return input

chain = Chain([prompt,llm,parser])
content = chain.invoke({"subject": "机器学习"})
print(content)