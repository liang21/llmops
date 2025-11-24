#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/23 00:57
@Author  : terminator
@File    : conftest.py
"""
import pytest
from app.app import app
@pytest.fixture
def client():
    app.config["TESTING"] =  True
    with app.test_client() as client:
        yield client