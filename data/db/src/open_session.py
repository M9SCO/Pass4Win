from sqlalchemy.orm import sessionmaker

from data.db.src.create_session_maker import create_session_maker


def open_session(session_maker: sessionmaker = None):
    session = session_maker or create_session_maker()
    with session() as session:
        return session
