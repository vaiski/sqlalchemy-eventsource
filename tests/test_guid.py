# -*- coding: utf-8 -*-

import uuid
import pytest
import sqlalchemy as sa

from sqlalchemy_eventsource import GUID


@pytest.fixture
def Event(Base):
    class Event(Base):
        __tablename__ = 'events'
        id = sa.Column(sa.Integer, primary_key=True)
        external_id = sa.Column(GUID)
    return Event


class TestGUIDType(object):

    def test_return_value(self, session, Event):
        external_id = uuid.uuid4()
        event = Event(external_id=str(external_id))

        session.add(event)
        session.commit()

        event = session.query(Event).first()
        assert isinstance(event.external_id, uuid.UUID)
        assert event.external_id == external_id

    def test_literal_param(self, session, Event):
        external_id = uuid.uuid4()
        clause = Event.external_id == external_id
        compiled = str(clause.compile(compile_kwargs={'literal_binds': True}))
        assert compiled == 'events.external_id = \'{}\''.format(
            external_id.hex
        )
