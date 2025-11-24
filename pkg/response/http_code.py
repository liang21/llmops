#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/20 00:28
@Author  : terminator
@File    : http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    """
    HTTP状态码枚举
    """
    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    VALIDATE_ERROR = "validate_error"
