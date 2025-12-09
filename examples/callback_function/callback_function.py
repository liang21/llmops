import os
import time
from typing import Any
from uuid import UUID

from langchain_community.chat_models import ChatOpenAI
from langchain_core.callbacks import BaseCallbackHandler, StdOutCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.outputs import LLMResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough


class LLMOpsCallbackHandler(BaseCallbackHandler):
    def on_chat_model_start(
            self,
            serialized: dict[str, Any],
            messages: list[list[BaseMessage]],
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            tags: list[str] | None = None,
            metadata: dict[str, Any] | None = None,
            **kwargs: Any,
    ) -> Any:
        print("开始调用大语言模型")
        print("serialized:", serialized)
        print("messages:", messages)
        self.start_at = time.time()

    def on_llm_end(
            self,
            response: LLMResult,
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            **kwargs: Any,
    ) -> Any:
        ent_at = time.time()
        print("完整输出:", response)
        print("大语言模型调用结束,耗时:", ent_at - self.start_at)


prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                 api_key=os.getenv("DEEPSEEK_API_KEY"), callbacks=[LLMOpsCallbackHandler()])
parser = StrOutputParser()

chain = {"query": RunnablePassthrough()} | prompt | llm | parser

content = chain.stream("你好,你是", config={"callbacks": [LLMOpsCallbackHandler(), StdOutCallbackHandler()]})

for chunk in content:
    print(chunk)