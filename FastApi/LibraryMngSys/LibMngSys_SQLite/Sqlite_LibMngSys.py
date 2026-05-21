# ======================================================================================
# 📝 FastAPI Library Management System (CRUD) - SQLite Version
# ======================================================================================
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, String, Float, Boolean, Column, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, relationship
from datetime import datetime, timedelta

# ------------------------------------------------------------
# 🚀 Create FastAPI Application
# ------------------------------------------------------------
app=FastAPI()

# ------------------------------------------------------------
# 🗄️ SQLite Configuration
# ------------------------------------------------------------

DB_URL="sqlite:///./library_db"

engine=create_engine(DB_URL)
LocalSession=sessionmaker(bind=engine)
Base=declarative_base()

# ============================================================
# 🧱 Database Model (Table)
# ============================================================

# ------------------------------------------------------------
# 📚 Books Table
# ------------------------------------------------------------
class Book(Base):
    __tablename__="books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    genre = Column(String(255))
    author=Column(String(255))
    price = Column(Float)
    total_quantity=Column(Integer)
    available_quantity=Column(Integer)
    
    #Relationship
    issued_books = relationship("IssuedBook", back_populates="book")

# ------------------------------------------------------------
# 👤 Users Table
# ------------------------------------------------------------
class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    
    #Relationship
    issued_books=relationship("IssuedBook", back_populates="user")

# ------------------------------------------------------------
# 📖 Issued Books Table
# ------------------------------------------------------------
class IssuedBook(Base):
    __tablename__="issued_books"
    
    id=Column(Integer, primary_key=True, index=True)
    #Foreign Keys
    book_id=Column(Integer, ForeignKey("books.id"))
    user_id=Column(Integer, ForeignKey("users.id"))
    
    #Issue details
    issued_by=Column(String(255))
    issued_to=Column(String(255))
    
    #Time
    issued_time=Column(DateTime, default=datetime.utcnow)
    
    due_date=Column(DateTime)
    
    returned_time=Column(DateTime, nullable=True)
    
    #Fine
    fine_amount=Column(Float, default=0)
    
    #Status
    status=Column(String(50), default="Issued")
    
    #Relationship
    book=relationship("Book", back_populates="issued_books")
    user=relationship("User", back_populates="issued_books")
# ------------------------------------------------------------
# Create all Tables
# ------------------------------------------------------------
Base.metadata.create_all(bind=engine)

# ============================================================
# 🧾 Pydantic Schema
# ============================================================

# ------------------------------------------------------------
# Book Schema 
# ------------------------------------------------------------
class CreateBook(BaseModel):
    title: str
    genre: str
    author:str
    price: float
    total_quantity: int 

# ------------------------------------------------------------
# User Schema 
# ---------------------------------------------------------
class CreateUser(BaseModel):
    name: str
    email: str
    
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
@app.post("/books")
def add_book(book:CreateBook, db:Session=Depends(get_db)):
    
    
    new_book=Book(
        title=book.title,
        genre=book.genre,
        author=book.author,
        price=book.price,
        total_quantity=book.total_quantity,
        available_quantity=book.total_quantity
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return {"Message":"Book added successfully!", "data":new_book}

# ------------------------------------------------------------
# ✅ 2. READ ALL Books
# ------------------------------------------------------------
@app.get("/books")
def get_allBooks(db:Session=Depends(get_db)):
    books=db.query(Book).all()
    
    return {"Count":len(books), "Data":books}

# ------------------------------------------------------------
# ✅ 3. READ SINGLE Book Data
# ------------------------------------------------------------
@app.get("/books/{book_id}")
def book_by_ID(book_id:int, db:Session=Depends(get_db)):
    book=db.query(Book).filter(Book.id==book_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

# ------------------------------------------------------------
# ✅ 4. UPDATE Book Details
# ------------------------------------------------------------
@app.put("/books/{book_id}")
def update_book(book_id:int, updated:CreateBook, db:Session=Depends(get_db)):
    book=db.query(Book).filter(Book.id==book_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title=updated.title
    book.genre=updated.genre
    book.author=updated.author
    book.price=updated.price
    diff=updated.total_quantity-book.total_quantity
    book.total_quantity=updated.total_quantity
    book.available_quantity+=diff
    
    db.commit()
    db.refresh(book)
    
    return {"Message":"Book updated successfully", "data":book}

# ------------------------------------------------------------
# ✅ 5. DELETE Book
# ------------------------------------------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id:int, db:Session=Depends(get_db)):
    
    book=db.query(Book).filter(Book.id==book_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    
    return {"Message":"Book removed successfully"}
# ------------------------------------------------------------
# ✅ 6. Add user
# ------------------------------------------------------------
@app.post("/users")
def add_user(_user:CreateUser, db:Session=Depends(get_db)):
    
    existing_user=db.query(User).filter(User.email==_user.email).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists") 

    new_user=User(
        name=_user.name,
        email=_user.email
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message":"User added Successfully", "data":new_user}

# ------------------------------------------------------------
# ✅ 7. Get all users
# ------------------------------------------------------------
@app.get("/users")
def get_users(db:Session=Depends(get_db)):
    
    users=db.query(User).all()
    
    return {"Count":len(users), "data": users}

# ------------------------------------------------------------
# ✅ 8. ISSUE Book
# ------------------------------------------------------------
@app.post("/issue-book/{book_id}/{user_id}")
def issue_book(book_id:int, user_id:int, days:int, issued_by:str, db:Session=Depends(get_db)):
    
    book=db.query(Book).filter(Book.id==book_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.available_quantity<=0:
        raise HTTPException(status_code=400, detail="No copies available")
    
    #Check User
    user=db.query(User).filter(User.id==user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    #Current time
    current_time=datetime.utcnow()
    
    #Due date
    due_date=current_time+timedelta(days=days)
    
    #Create Issue Record
    issue=IssuedBook(
        book_id=book_id,
        user_id=user_id,
        
        issued_by=issued_by,
        issued_to=user.name,
        
        issued_time=current_time,
        due_date=due_date,
        
        status="Issued"
    )
    
    #Update Book Status
    book.available_quantity-=1
    db.add(issue)
    db.commit()
    
    return {"Message":"Book issued successfully",
            "book":book.title,
            "issued to":user.name,
            "issued by":issued_by,
            "issued time":current_time,
            "return before":due_date
            }

# ------------------------------------------------------------
# ✅ 9. RETURN Book
# ------------------------------------------------------------
@app.post("/return-book/{book_id}")
def return_book(book_id:int, db:Session=Depends(get_db)):
    
    issue=db.query(IssuedBook).filter(IssuedBook.book_id==book_id, IssuedBook.status=="Issued").first()
    
    if not issue:
        raise HTTPException(status_code=404, detail="Issue record not found")
    
    #Find book
    book=db.query(Book).filter(Book.id==book_id).first()
    
    #Update Book status
    book.available_quantity+=1
    
    #Return Time
    issue.returned_time=datetime.utcnow()
    
    #Check for late return
    if issue.returned_time > issue.due_date:
        issue.status="Late Return"
        late_days=(issue.returned_time-issue.due_date).days
        
        #fine ₹10  per day
        fine=late_days*10
        
        issue.fine_amount=fine
        
    else:
        issue.status="Returned"
        issue.fine_amount=0
    
    db.commit()
    
    return {"Message":"Book returned successfully",
            "book":book.title,
            "returned_time":issue.returned_time,
            "status":issue.status,
            "fine amount":issue.fine_amount
            }

# ------------------------------------------------------------
# ✅ 10. AVAILABLE Books
# ------------------------------------------------------------
@app.get("/available-books")
def available_books(db:Session=Depends(get_db)):
    
    books=db.query(Book).filter(Book.available_quantity>0).all()
    
    return{
        "count":len(books),
        "data":books
    }
    
# ------------------------------------------------------------
# ✅ 11. ISSUED Books
# ------------------------------------------------------------
@app.get("/issued-books")
def issued_books(db:Session=Depends(get_db)):
    
    books=db.query(IssuedBook).filter(IssuedBook.status=="Issued").all()
    
    return{
        "Count":len(books),
        "data":books
    }

# ------------------------------------------------------------
# ✅ 12. ISSUED History
# ------------------------------------------------------------
@app.get("/issue-history")
def issue_history(db:Session=Depends(get_db)):
    
    history=db.query(IssuedBook).all()
    
    return {"Count":len(history), "data":history}

# ------------------------------------------------------------
# ✅ 13. SEARCH Book By Title
# ------------------------------------------------------------
@app.get("/search-book/{title}")
def search_book(title:str, db:Session=Depends(get_db)):
    
    books=db.query(Book).filter(Book.title.ilike(f"%{title}%")).all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return {
        "Count":len(books),
        "data":books
    }