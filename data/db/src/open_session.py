import logging
import traceback

from sqlalchemy.orm import sessionmaker

from data.db.src.create_session_maker import create_session_maker


async def open_session(session_maker: sessionmaker = None):
    try:
        async_session = session_maker or create_session_maker()
        async with async_session() as session:
            yield session
    except:
        logging.error(traceback.format_exc())
        await session.rollback()
        raise
    finally:
        await session.close()
