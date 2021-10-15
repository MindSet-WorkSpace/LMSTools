from os.path import abspath
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy_access as sa_a  # NOQA
import sqlalchemy_access.pyodbc as sa_a_pyodbc # NOQA

Base = declarative_base()

con = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=database\POSDev.mdb;ExtendedAnsiSQL=1;"
connection_uri = f"access+pyodbc:///?odbc_connect={quote_plus(con)}"
engine = create_engine(connection_uri)
database_session = sessionmaker(bind=engine)()

from .user import User
from .laundry import Laundry
