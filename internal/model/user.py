#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/24 22:55
@Author  : terminator
@File    : user.py
"""
import uuid

from sqlalchemy.orm import Mapped, mapped_column

from internal.exception.database_extension import db


class User(db.Model):
    id: Mapped[str] = mapped_column(default=uuid.uuid4(), primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
