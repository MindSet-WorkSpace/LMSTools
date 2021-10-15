from . import Base
from sqlalchemy import Column, String, Integer, Boolean, or_, and_
from database import database_session


class Laundry(Base):
    __tablename__ = "vCategories"
    ID = Column(Integer, primary_key=True)
    CatCode = Column(Integer)
    CategoryName = Column(String)
    ParentCategory = Column(Integer)
    ParentCategoryName = Column(String)
    IsParent = Column(Boolean)
    Discontinued = Column(Boolean)

    @staticmethod
    def has_sub_category(material):
        laundry = database_session.query(Laundry).filter(Laundry.CategoryName == material)
        is_parent = any([data.IsParent for data in laundry])
        return is_parent

    @staticmethod
    def get_sub_category(material):
        laundry = database_session.query(Laundry).filter(Laundry.ParentCategoryName == material).all()
        return [sub_category.CategoryName for sub_category in laundry]
