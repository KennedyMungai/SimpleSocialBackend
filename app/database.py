from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'mysql://root:xknightmare12873@localhost/simple_social_db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
