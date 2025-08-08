from database import Base # pyright: ignore [reportAny]
from sqlalchemy import Column, Integer, String

class Movies(Base): # pyright: ignore [reportAny]
    __tablename__ = "movies" # pyright: ignore [reportUnannotatedClassAttribute]
    
    id = Column(Integer,primary_key=True,index=True) # pyright: ignore [reportUnannotatedClassAttribute]
    movie_name = Column(String, unique=True) # pyright: ignore [reportUnannotatedClassAttribute]
    movie_description = Column(String) # pyright: ignore [reportUnannotatedClassAttribute]
    movie_year = Column(Integer) # pyright: ignore [reportUnannotatedClassAttribute]