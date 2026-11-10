from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Float, Integer, String
from pydantic import BaseModel as BaseSchema, Field

#Product schema for the api:

class ProductSchema(BaseSchema):
    id: int | None = Field(default=None)
    name: str = Field()
    price: float= Field()
    stock: int = Field(default=0)


class ProductModel(declarative_base()):

    # The exact database table:
    __tablename__ = "products"

    id= Column(Integer, primary_key= True)
    name = Column(String(40), nullable= False)
    price = Column(Float, nullable= False)
    stock = Column(Integer, default= 0)

    def __repr__(self):
        return str({p.name: getattr(self, p.name) for p in self.__table__.columns})
