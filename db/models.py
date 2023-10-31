from sqlalchemy import (BigInteger, Column, Identity, Text)
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UsersTokens(Base):
    __tablename__ = "users_tokens"

    id = Column("id", BigInteger, Identity(start=1, increment=1, minvalue=1, cycle=False, cache=1), nullable=False,
                primary_key=True)
    vkid = Column("vkid", BigInteger, nullable=False, unique=True)
    token = Column("token", Text, nullable=False)
