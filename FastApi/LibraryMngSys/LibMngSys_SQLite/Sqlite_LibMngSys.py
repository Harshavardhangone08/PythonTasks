# ======================================================================================
# 📝 FastAPI Library Management System (CRUD) - SQLite Database Version
# ======================================================================================
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, String, Float, Boolean, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# ------------------------------------------------------------
# 🚀 Create FastAPI Application
# ------------------------------------------------------------
app=FastAPI()

# ------------------------------------------------------------
# 🗄️ Database Configuration
# ------------------------------------------------------------

DB_URL="sqlite:///./library_db"

engine=create_engine(DB_URL,connect_args={"check_same_thread":False})
LocalSession=sessionmaker(bind=engine)
Base=declarative_base()

# ------------------------------------------------------------
# 🧱 Database Model (Table)
# ------------------------------------------------------------

class Library_DB(Base):
    __tablename__="Library"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    Genre = Column(String)
    author=Column(String)
    price = Column(Float)
    available = Column(Boolean, default=True)
    
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class lib(BaseModel):
    id: int
    title: str
    Genre: str
    author:str
    price: float
    available:bool
    class config:
        orm_model = True 

# ------------------------------------------------------------
# 🔌 Dependency (DB Session)
# ------------------------------------------------------------

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()
        
# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------

@app.get("/")
def home():
    return {"Message":"Library Management System"}

# ------------------------------------------------------------
# ✅ 1. Add New Book Data
# ------------------------------------------------------------
@app.post("/Library")
def add_book(book:lib, db:Session=Depends(get_db)):
    existing=db.query(Library_DB).filter(Library_DB.id==book.id).first()
    if existing:
        raise HTTPException(status_code=404, detail="Book ID already exists")
    
    new_book=Library_DB(
        id=book.id,
        title=book.title,
        Genre=book.Genre,
        author=book.author,
        price=book.price,
        available=book.available
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return {"Message":"Book added successfully!", "data":new_book}

# ------------------------------------------------------------
# ✅ 2. READ ALL Books
# ------------------------------------------------------------
@app.get("/Library")
def get_allBooks(db:Session=Depends(get_db)):
    Books=db.query(Library_DB).all()
    
    return {"Count":len(Books), "Data":Books}

# ------------------------------------------------------------
# ✅ 3. READ SINGLE Book Data
# ------------------------------------------------------------
@app.get("/Library/{b_id}")
def book_by_ID(b_id:int, db:Session=Depends(get_db)):
    book=db.query(Library_DB).filter(Library_DB.id==b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

# ------------------------------------------------------------
# ✅ 4. UPDATE Book Details
# ------------------------------------------------------------
@app.put("/Library/{b_id}")
def update_book(b_id:int, updated:lib, db:Session=Depends(get_db)):
    book=db.query(Library_DB).filter(Library_DB.id==b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title=updated.title
    book.Genre=updated.Genre
    book.author=updated.author
    book.price=updated.price
    book.available=updated.available
    
    db.commit()
    db.refresh(book)
    
    return {"Message":"Book updated successfully", "data":book}

# ------------------------------------------------------------
# ✅ 5. DELETE Book
# ------------------------------------------------------------
@app.delete("/Library/{b_id}")
def delete_book(b_id:int, db:Session=Depends(get_db)):
    book=db.query(Library_DB).filter(Library_DB.id==b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    
    return {"Message":"Book removed successfully"}

# ------------------------------------------------------------
# ✅ 6. ISSUE Book
# ------------------------------------------------------------
@app.post("/issue-book/{b_id}")
def issue_book(b_id:int, db:Session=Depends(get_db)):
    book=db.query(Library_DB).filter(Library_DB.id==b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if not book.available:
        raise HTTPException(status_code=400, detail="Book already issued")
    
    book.available=False
    db.commit()
    
    return {"Message":f"Book {book.title} issued successfully"}

# ------------------------------------------------------------
# ✅ 7. RETURN Book
# ------------------------------------------------------------
@app.post("/return-book/{b_id}")
def return_book(b_id:int, db:Session=Depends(get_db)):
    book=db.query(Library_DB).filter(Library_DB.id==b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.available:
        raise HTTPException(status_code=400, detail="Book already returned")
    
    book.available=True
    
    db.commit()
    
    return {"Message":f"Book {book.title} returned successfully"}

# ------------------------------------------------------------
# ✅ 8. AVAILABLE Books
# ------------------------------------------------------------
@app.get("/available-books")
def available_books(db:Session=Depends(get_db)):
    
    books=db.query(Library_DB).filter(Library_DB.available==True).all()
    
    return{
        "count":len(books),
        "data":books
    }
    
# ------------------------------------------------------------
# ✅ 9. ISSUED Books
# ------------------------------------------------------------
@app.get("/issued-books")
def issued_books(db:Session=Depends(get_db)):
    
    books=db.query(Library_DB).filter(Library_DB.available==False).all()
    
    return{
        "Count":len(books),
        "data":books
    }
    
# ------------------------------------------------------------
# ✅ 10. SEARCH Book By Title
# ------------------------------------------------------------
@app.get("/search-book/{title}")
def search_book(title:str, db:Session=Depends(get_db)):
    
    books=db.query(Library_DB).filter(Library_DB.title.ilike(f"%{title}%")).all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return {
        "Count":len(books),
        "data":books
    }