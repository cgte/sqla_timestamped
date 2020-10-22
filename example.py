import sqlalchemy

db_uri = "sqlite:///:memory:"
echo = True

engine = sqlalchemy.create_engine(db_uri, echo=echo)

conn = engine.connect()  # Just for checking

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemt import Column, Integer, String


class reprmixin:
    def __repr__(self):
        return f"{self.__class__.__name}({self.__dict__})"


class User(Base, reprmixin):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


from pprint import pprint as print
