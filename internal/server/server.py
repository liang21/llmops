#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/17 23:57
@Author  : terminator
@File    : server.py
"""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config
from internal.extension import CustomException
from internal.router import Router
from pkg.response import json, Response, HttpCode


class Server(Flask):
    def __init__(self, *args, conf: Config, db: SQLAlchemy, router: Router, **kwargs):
        """
        创建服务
        :param args:
        :param conf:
        :param router:
        :param kwargs:
        """
        # 初始化flask
        super().__init__(*args, **kwargs)
        # 加载配置
        self.config.from_object(conf)

        self.register_error_handler(Exception, self._register_error_handler)

        db.init_app(self)
        # 注册路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(
                Response(
                    code=error.code,
                    message=error.message,
                    data=error.data if error.data else None
                )
            )
        if self.debug or os.getenv("FLASK_ENV") == "development":
            return error
        else:
            return json(
                Response(
                    code=HttpCode.FAIL,
                    message=str(error),
                    data=None
                )
            )
