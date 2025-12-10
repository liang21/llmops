import os

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import ConfigurableField

dotenv.load_dotenv()

prompt = PromptTemplate.from_template("请写一篇关于{subject}主题的冷笑话").configurable_fields(
    template=ConfigurableField(id="prompt_template"))

content = prompt.invoke({"subject": "程序员"},
                       config={"configurable": {"prompt_template": "请写一篇关于{subject}主题的冷笑话"}}).to_string()
print(
     content
)