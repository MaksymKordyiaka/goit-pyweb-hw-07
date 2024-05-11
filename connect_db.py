from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_connection_str = "sqlite:///study.db"

engine = create_engine(db_connection_str)
Session = sessionmaker(bind=engine)
session = Session()
