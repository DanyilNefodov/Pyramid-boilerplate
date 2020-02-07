import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    ForeignKey,
    Text,
    Boolean,
    )

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import register


DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    password = Column(Text)


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)


class UserInGroup(Base):
    __tablename__ = 'useringroup'

    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'), primary_key=True)


class Banner(Base):
    __tablename__ = 'banner'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    image_path = Column(Text, unique=True, nullable=True)
    url = Column(Text, nullable=False)
    visible = Column(Boolean, default=True)
    position = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
