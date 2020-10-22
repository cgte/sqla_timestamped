import sqlalchemy

db_uri = "sqlite:///:memory:"
echo = True

engine = sqlalchemy.create_engine(db_uri, echo=echo)

conn = engine.connect()  # Just for checking

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String


class reprmixin:
    def __repr__(self):
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return f"{self.__class__.__name__}({data})"


class BornMixin:
    born = Column(String, default="Unknown")


class User(Base, BornMixin, reprmixin):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


from pprint import pprint as print

print(User.__table__)


# Create the schema

Base.metadata.create_all(engine)

colin = User(name="Colin", fullname="Colin Goutte", nickname="Chouchou")

print(repr(colin))
