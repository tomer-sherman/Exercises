from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel as BaseSchema, Field

Base = declarative_base()

# ==========================================
# 1. SQLAlchemy Database Models
# ==========================================

class StudiosModel(Base):
    __tablename__ = "studios"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    country = Column(String(50), nullable= False)


    # Relationship back to games (One studio can have many games)
    games = relationship("GamesModel", back_populates="studio")


class GamesModel(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    title = Column(String(40), nullable=False)
    genre = Column(String(30), nullable=False)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
    release_year = Column(Integer, default=0)

    # 1. Corrected Foreign Key syntax pointing to 'studios.id'
    studio_id = Column(Integer, ForeignKey("studios.id"), nullable=False)

    # 2. Relationship property to access the studio object directly
    studio = relationship("StudiosModel", back_populates="games")

    def __repr__(self):
        # Grabs the state directly without triggering property/column evaluations
        state = self.__dict__
        return str({p.name: state.get(p.name, None) for p in self.__table__.columns})


# ==========================================
# 2. Pydantic Schemas for your API
# ==========================================

class GamesSchema(BaseSchema):
    id: int | None = Field(default=None)
    title: str = Field()
    studio_id: int = Field()
    genre: str = Field()
    price: float = Field()
    rating: float = Field()
    release_year: int = Field()

    class Config:
        from_attributes = True  

class StudiosSchema(BaseSchema):
    id: int | None = Field(default=None)
    name: str = Field()
    country: str = Field()

    class Config:
        from_attributes = True  # Allows parsing directly from the database model

