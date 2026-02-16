from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

db_url = 'mysql+pymysql://root@localhost:3306/db-blog'
engine = create_engine(db_url, echo=False)

sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()