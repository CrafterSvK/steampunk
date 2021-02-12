from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config


class Database:
    def __init__(self):
        self.base = declarative_base()
        self.db = create_engine(config['database_string'], echo=True)


database = Database()
session = sessionmaker(database.db)()
