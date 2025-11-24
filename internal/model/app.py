#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2025/11/23 22:31
@Author  : terminator
@File    : app.py
"""
import datetime
import uuid

from sqlalchemy import UUID, PrimaryKeyConstraint

from internal.exception.database_extension import db


class App(db.Model):
    __tablename__ = "app"
    __table_args__ = (
        PrimaryKeyConstraint('id', name="id"),
    )
    id = db.Column(UUID, default=uuid.uuid4, nullable=False)
    account_id = db.Column(UUID, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    icon = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.time, onupdate=datetime.time, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.time, nullable=False)
