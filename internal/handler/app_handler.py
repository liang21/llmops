#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/17 23:42
@Author  : terminator
@File    : app_handler.py
"""

import os
from dataclasses import dataclass
from uuid import UUID

from dotenv import load_dotenv
from injector import inject
from langchain_community.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from internal.extension import FailException
from internal.schema import CompletionReq
from internal.service import AppService
from internal.service.user_service import UserService
from pkg.response import success_json, validate_error_json, success_message, fail_message

load_dotenv()


@inject
@dataclass
class AppHandler:
    app_service: AppService
    user_service: UserService

    def create_app(self):
        """
        创建app
        :return:
        """
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建,id为{app.id}")
    def get_app(self, id: UUID):
        """
        获取app
        :return:
        """
        app = self.app_service.get_app(id)
        return success_json(app)

    def update_app(self,id: UUID):
        """
        更新app
        :return:
        """

        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "更新后的应用"
            self.db.session.add(app)
        return app

    def delete_app(self, id: UUID):
        """
        删除app
        :return:
        """
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
        return app

    def completion(self, app_id: UUID):
        """
        处理用户请求
        :return:
        """
        # 1、获取接口参数
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 2、构建组件
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(model="deepseek-chat", temperature=0.9, base_url=os.getenv("DEEPSEEK_BASE_URL"),
                         api_key=os.getenv("DEEPSEEK_API_KEY"))
        parser = StrOutputParser()

        # 3、构建链
        chain = prompt | llm | parser
        content = chain.invoke({"query": req.query.data})
        return success_json({"content": content})


    def ping(self):
        raise FailException("fail")
        # return {"ping": "pong"}
