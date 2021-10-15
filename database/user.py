from database import Base
from sqlalchemy import Column, String, Integer
from database import database_session
from sqlalchemy.exc import DBAPIError, InterfaceError


class User(Base):
    __tablename__ = "User"
    ID = Column(Integer, primary_key=True)
    UserName = Column(String)
    Password = Column(String)
    StoreNo = Column(Integer)
    Role = Column(String)

    @staticmethod
    def login_user(username, password):
        try:
            user = database_session.query(User).filter(User.UserName == username).first()
            password = database_session.query(User).filter(User.Password == password).first()
            return user, password
        except InterfaceError:
            return "Microsoft Access Engine must be installed before accessing the database"
        except DBAPIError as e:
            return "Database Not Found"

