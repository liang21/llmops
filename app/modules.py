#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/23 21:41
@Author  : terminator
@File    : modules.py
"""
from flask_sqlalchemy import SQLAlchemy
from injector import Module, Binder

from internal.exception.database_extension import db


class ExtensionModule(Module):
    def configure(self, binder: Binder):
        binder.bind(SQLAlchemy, to=db)
