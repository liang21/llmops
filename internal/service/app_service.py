#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/23 23:52
@Author  : terminator
@File    : app_service.py
"""
import uuid
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import App


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self) -> App:
        """
        创建app
        :return:
        """
        app = App(name="聊天机器人", account_id=uuid.uuid4(), icon="", description="这是一个简单的聊天机器人")
        self.db.session.add(app)
        self.db.session.commit()
        return app
