#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/20 00:11
@Author  : terminator
@File    : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    query = StringField(
        "query",
        validators=[
            DataRequired(message="query is required"),
            Length(min=1, max=1024, message="query length must be between 1 and 1024"),
        ]
    )
