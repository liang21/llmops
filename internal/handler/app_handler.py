#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/17 23:42
@Author  : terminator
@File    : app_handler.py
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv
from flask import request
from injector import inject
from openai import OpenAI

from internal.extension import FailException
from internal.schema import CompletionReq
from internal.service.user_service import UserService
from pkg.response import success_json, validate_error_json

load_dotenv()


@inject
@dataclass
class AppHandler:
    # app_service: AppService
    user_service: UserService

    # def create_app(self):
    #     """
    #     创建app
    #     :return:
    #     """
    #     app = self.app_service.create_app()
    #     return success_message(f"应用已经成功创建,id为{app.id}")

    def create_user(self):
        """
        创建用户
        :return:
        """
        user = self.user_service.create_user()
        return "ok"

    def completion(self):
        """
        处理用户请求
        :return:
        """
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        query = request.json.get("query")

        client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL"),
        )
        completion = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query},
            ]
        )
        content = completion.choices[0].message.content
        return success_json({"content": content})

    def ping(self):
        raise FailException("fail")
        # return {"ping": "pong"}
