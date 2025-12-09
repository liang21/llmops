import os

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic.v1 import BaseModel,Field

dotenv.load_dotenv()

class Joke(BaseModel):
    joke:str = Field(description="回答用户的冷笑话")
    punchline:str = Field(description=" 这是个冷笑话的笑点")

parser = JsonOutputParser(pydantic_object=Joke)

# 2、构建一个提示模板
prompt = ChatPromptTemplate.from_template("请根据用户的提问进行回答。\n{format_instructions}\n{query}").partial(
    format_instructions=parser.get_format_instructions())

# 3、构建大语言模型
llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),api_key=os.getenv("DEEPSEEK_API_KEY"))

joke = parser.invoke(llm.invoke(prompt.invoke({"query": "请讲一个关于机器学习的冷笑话?"})))
print(joke)