# -*- coding: utf-8 -*-
"""
SQLAlchemy-EventSource
======================

Models and utilities for event sourcing with SQLAlchemy.

:copyright: (c) 2016 by Eemil Väisänen.
:license: MIT, see LICENSE for more details.
"""

import uuid
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID

__version__ = '0.1.0-dev'


class GUID(TypeDecorator):
    """
    Platform-independent GUID type.
    """

    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return uuid.UUID(value).hex
            else:
                return value.hex

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)
