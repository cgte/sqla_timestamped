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

    def __str__(self):
        data = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return f"{self.__class__.__name__}({data})"


class User(Base, reprmixin):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


from sqlalchemy.schema import FetchedValue
from sqlalchemy import TIMESTAMP
from sqlalchemy import func

from datetime import datetime

now = datetime.now

tz = True


class Change(Base, reprmixin):
    __tablename__ = "changes"

    change_id = Column(Integer, primary_key=True)
    name = Column(String)
    if tz:
        srv_def_ts = Column(TIMESTAMP, default=now)
        srv_upd_ts = Column(TIMESTAMP, onupdate=now)
    else:
        srv_def_ts = Column(TIMESTAMP, default=func.now())
        srv_upd_ts = Column(TIMESTAMP, onupdate=func.now())


from pprint import pprint as print

print(User.__table__)


# Create the schema

Base.metadata.create_all(engine)

colin = User(name="Colin", fullname="Colin Goutte", nickname="Chouchou")

change = Change(name="debut")
# print(repr(colin))
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

session.add(change)
session.flush()
session.commit()
session.close()

s = Session()
gg = s.query(Change).first()

from time import sleep

print(gg)

sleep(2)
gg.name = "modif"
s.add(gg)
s.commit()
session.close()

gg = Session().query(Change).first()
print(gg)
