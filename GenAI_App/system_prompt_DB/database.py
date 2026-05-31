from sqlalchemy import create_engine, Column, Integer, String, Float

from sqlalchemy.orm import declarative_base, sessionmaker

from dotenv import load_dotenv
import os

# =====================================================================
# Load Environment Variables
# =====================================================================
load_dotenv()

DB_URL=os.getenv("DB_URL")

# =====================================================================
# Database Connection
# =====================================================================
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()

# =====================================================================
# Books Table
# =====================================================================
class Book(Base):
    
    __tablename__="books"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(225))
    genre = Column(String(225))
    author = Column(String(225))
    price = Column(Float)
    total_quantity = Column(Integer)
    available_quantity = Column(Integer)
    
# =====================================================================
# Users Table
# =====================================================================
class User(Base):
    
    __tablename__="users"
    
    id=Column(Integer, primary_key=True)
    name = Column(String(225))
    email = Column(String(225))

# =====================================================================
# Issued books Table
# =====================================================================

class IssuedBook(Base):
    
    __tablename__="issued_books"
    
    id = Column(Integer, primary_key=True)
    status = Column(String(50))
    fine_amount = Column(Float)
    