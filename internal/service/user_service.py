#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/24 23:04
@Author  : terminator
@File    : user_service.py
"""
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import User


@inject
@dataclass
class UserService:
    db: SQLAlchemy

    def create_user(self) -> User:
        """
        创建用户
        :return:
        """
        user = User(username="terminator", email="")
        self.db.session.add(user)
        self.db.session.commit()
        return user
