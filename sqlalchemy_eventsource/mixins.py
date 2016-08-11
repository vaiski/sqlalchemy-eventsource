# -*- coding: utf-8 -*-

import uuid
import datetime

import sqlalchemy as sa

from .types import GUID


class PublicIdMixin(object):

    public_id = sa.Column(GUID, nullable=False, index=True,
                          default=uuid.uuid4)


class CreatedAtMixin(object):
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow,
                           nullable=False, index=True)


class UpdatedAtMixin(object):
    updated_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow,
                           onupdate=datetime.datetime.utcnow, nullable=False,
                           index=True)


class DeletedAtMixin(object):
    deleted_at = sa.Column(sa.DateTime, nullable=True, index=True)
