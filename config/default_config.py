#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/23 21:25
@Author  : terminator
@File    : default_config.py
"""
DEFAULT_CONFIG = {
    # wtf 配置
    "WTF_CSRF_ENABLED": "False",
    # SQLAlchemy 数据库配置
    'SQLALCHEMY_DATABASE_URI': "",
    'SQLALCHEMY_POOL_SIZE': 30,
    "SQLALCHEMY_POOL_RECYCLE": 3600,
    "SQLALCHEMY_ECHO": "True"
}
