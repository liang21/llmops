import os

import dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()
# 1、编排提示模板
prompt = ChatPromptTemplate.from_template("请讲一个关于{subject}的冷笑话?")

# 2、构建大语言模型
llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),api_key=os.getenv("DEEPSEEK_API_KEY"))

# 3、创建字符串输出
parser = StrOutputParser()

# 4、调用大语言模型生成结果并解析
content = parser.invoke(llm.invoke(prompt.invoke({"subject": "你好,你是?"})))

print(content)