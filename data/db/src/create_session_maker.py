from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from data.db.src.create_engine import create_engine


def create_session_maker(engine: Engine = None) -> sessionmaker:
    return sessionmaker(engine or create_engine(), expire_on_commit=False)
