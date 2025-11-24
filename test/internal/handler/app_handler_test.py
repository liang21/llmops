#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/22 23:08
@Author  : terminator
@File    : app_handler_test.py
"""


class TestHandler(object):
    def test_completion(self,client):
        """
        测试completion
        :return:
        """
        resp = client.post("/llmops/api/v1/chat",json={"query":"None"})
        print(resp.json)
        assert resp.status_code == 200
        assert resp.json.get("code") == "success"
