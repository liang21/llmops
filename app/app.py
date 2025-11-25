#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/17 23:59
@Author  : terminator
@File    : app.py
"""
from injector import Injector

from app import ExtensionModule
from config import Config
from internal.router import Router
from internal.server import Server
from pkg.sqlalchemy import SQLAlchemy

injector = Injector([ExtensionModule])
conf = Config()
app = Server(__name__, conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))
if __name__ == '__main__':
    app.run(debug=True)
