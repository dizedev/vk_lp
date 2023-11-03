from sqlalchemy import (BigInteger, Column, Identity, Text, JSON, TIMESTAMP)
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UsersTokens(Base):
    __tablename__ = "users_tokens"

    id = Column("id", BigInteger, Identity(start=1, increment=1, minvalue=1, cycle=False, cache=1), nullable=False,
                primary_key=True)
    vkid = Column("vkid", BigInteger, nullable=False, unique=True)
    token = Column("token", Text, nullable=False)


class UsersProfile(Base):
    __tablename__ = "users_profile"

    # TODO: think about foreign_id
    id = Column("id", BigInteger, Identity(start=1, increment=1, minvalue=1, cycle=False, cache=1), nullable=False,
                primary_key=True)
    vkid = Column("vkid", BigInteger, nullable=False, unique=True)
    achievements = Column("achievements", JSON)
    trusted_ids = Column("trusted_ids", JSON)
    prefix = Column("prefix", Text)
    prefix_d = Column("prefix_d", Text)
    prefix_delete = Column("prefix_delete", Text)
    last_login = Column("last_login", TIMESTAMP)
