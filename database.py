from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv() # pyright: ignore [reportUnusedCallResult]

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
dbname = os.getenv("DATABASENAME")

SQL_ALCHEMY_DATABASE_URL = "mysql+mysqlconnector://{}:{}@localhost:3306/{}".format(username,password,dbname)

engine = create_engine(SQL_ALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
sessionlocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base() # pyright: ignore [reportAny]