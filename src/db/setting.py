import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager


DATABASE = "mysql+pymysql://%s:%s@%s/%s?charset=utf8" % (
    os.getenv("MYSQL_USER"),
    os.environ["MYSQL_PASSWORD"],
    "mysql",
    os.getenv("MYSQL_DATABASE"),
)

ENGINE = create_engine(DATABASE, encoding="utf-8", echo=False)


def get_session():
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
    )
    return session


@contextmanager
def session_scope():
    """ """
    session = get_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
