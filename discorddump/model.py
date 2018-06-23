# This Python file uses the following encoding: utf-8
import os

from sqlalchemy import Column, Integer, String, create_engine, inspect, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relation
from sqlalchemy.schema import Index

debug = os.environ.get('DEBUG', False)

engine = create_engine(os.environ["DB_URL"], convert_unicode=True, pool_recycle=3600)

if debug:
    engine.echo = True

sm = sessionmaker(autocommit=False,
                  autoflush=False,
                  bind=engine)

base_session = scoped_session(sm)

Base = declarative_base()
Base.query = base_session.query_property()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)

    event_id = Column(String, nullable=False)
    event_hash = Column(String, nullable=False, unique=True)
    event_type = Column(String, nullable=False)
    event_source = Column(String)

    timestamp = Column(DateTime, nullable=False)

    blob = Column(JSONB)


# Indexes

Index("index_events_event_type", Event.event_type)
Index("index_events_timestamp", Event.timestamp)

# Relations

# Message.chat = relation(Chat)