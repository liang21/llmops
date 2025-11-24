#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/17 23:45
@Author  : terminator
@File    : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    app_handler: AppHandler

    def register_router(self, app: Flask):
        app_handler: AppHandler
        """
        注册路由
        :param app:
        :return:
        """
        # 1. 创建蓝图
        bp = Blueprint('llmops', __name__, url_prefix='/llmops/api/v1')
        # 2. 将url与对应的控制器方法做绑定
        bp.add_url_rule('/ping', view_func=self.app_handler.ping)
        bp.add_url_rule('/chat', methods=['POST'], view_func=self.app_handler.completion)
        # bp.add_url_rule('/app', methods=['POST'], view_func=self.app_handler.create_app)
        bp.add_url_rule('user', methods=['POST'], view_func=self.app_handler.create_user)
        # 3. 在应用上注册蓝图
        app.register_blueprint(bp)
