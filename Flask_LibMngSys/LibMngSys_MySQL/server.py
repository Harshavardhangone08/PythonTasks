# ======================================================================================
# 📝 FastAPI Library Management System (CRUD) - SQL Database Version
# ======================================================================================
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
from sqlalchemy import create_engine, Integer, String, Float, Column, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, relationship
from datetime import datetime, timedelta

# ------------------------------------------------------------
# 🚀 Create FastAPI Application
# ------------------------------------------------------------
app = FastAPI(title="Libris Library Management System", version="2.4.0")

# Mount Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

allowed_origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------------
# 🗄️ Database Configuration (Configured for MySQL)
# ------------------------------------------------------------
# Support MySQL natively with PyMySQL as requested
DB_URL = "mysql+pymysql://root:root@localhost:3306/library_management_system"

engine = create_engine(DB_URL)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ============================================================
# 🧱 Database Models
# ============================================================

# ------------------------------------------------------------
# 📚 Books Table
# ------------------------------------------------------------
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    genre = Column(String(255))
    author = Column(String(255))
    price = Column(Float)
    total_quantity = Column(Integer)
    available_quantity = Column(Integer)
    
    # Relationship
    issued_books = relationship("IssuedBook", back_populates="book", cascade="all, delete-orphan")

# ------------------------------------------------------------
# 👤 Users Table
# ------------------------------------------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    
    # Relationship
    issued_books = relationship("IssuedBook", back_populates="user", cascade="all, delete-orphan")

# ------------------------------------------------------------
# 📖 Issued Books Table
# ------------------------------------------------------------
class IssuedBook(Base):
    __tablename__ = "issued_books"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign Keys
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Issue details
    issued_by = Column(String(255))
    issued_to = Column(String(255))
    
    # Time
    issued_time = Column(DateTime, default=datetime.utcnow)
    due_date = Column(DateTime)
    returned_time = Column(DateTime, nullable=True)
    
    # Fine
    fine_amount = Column(Float, default=0.0)
    
    # Status
    status = Column(String(50), default="Issued")  # "Issued", "Returned", "Late Return"
    
    # Relationship
    book = relationship("Book", back_populates="issued_books")
    user = relationship("User", back_populates="issued_books")

# ------------------------------------------------------------
# Create all Tables
# ------------------------------------------------------------
Base.metadata.create_all(bind=engine)

# ============================================================
# 🧾 Pydantic Schema
# ============================================================

class CreateBook(BaseModel):
    title: str
    genre: str
    author: str
    price: float
    total_quantity: int 

class CreateUser(BaseModel):
    name: str
    email: str

class BookResponse(BaseModel):
    id: int
    title: str
    genre: str
    author: str
    price: float
    total_quantity: int
    available_quantity: int

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True

# ------------------------------------------------------------
# 🔌 Dependency (DB Session)
# ------------------------------------------------------------
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
        
# Helper to dynamically resolve template includes
def render_template_custom(file_name: str) -> str:
    file_path = os.path.join("templates", file_name)
    if not os.path.exists(file_path):
        print(f"Template module not found: {file_path}")
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    import re
    # Match {% include 'filename' %} or {% include "filename" %}
    include_regex = re.compile(r'{%\s*include\s+[\'"]([^\'"]+)[\'"]\s*%}')
    
    def replacer(match):
        included_file = match.group(1)
        return render_template_custom(included_file)
        
    return include_regex.sub(replacer, content)

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    try:
        content = render_template_custom("index.html")
        return HTMLResponse(content=content)
    except Exception as e:
        print(f"Error rendering home template: {e}")
        return HTMLResponse(content="<h3>Internal Server Error rendering template</h3>", status_code=500)

# 🔒 GET List of Authorized Operators for the Login dropdown
@app.get("/api/operators")
def get_operators():
    return [
        "Admin",
        "Librarian",
        "Harsha Vardhan"
    ]

class LoginRequest(BaseModel):
    username: str
    password: str

# 🔒 POST Authentication for Admin or Librarian
@app.post("/api/login")
def login(request_data: LoginRequest):
    credentials = {
        "admin": "admin123",
        "librarian": "librarian123",
        "harsha vardhan": "harsha123"
    }

    username_lower = request_data.username.strip().lower()
    if username_lower in credentials:
        if request_data.password == credentials[username_lower]:
            # Retain original case name for UI badge
            names = {
                "admin": "Admin",
                "librarian": "Librarian",
                "harsha vardhan": "Harsha Vardhan"
            }
            return {"success": True, "user": names[username_lower]}
            
    raise HTTPException(status_code=401, detail="Incorrect password or unauthorized registry.")

# ------------------------------------------------------------
# ✅ 1. Add New Book Data
# ------------------------------------------------------------
@app.post("/books")
def add_book(book: CreateBook, db: Session = Depends(get_db)):
    new_book = Book(
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
    return {"Message": "Book added successfully!", "data": new_book}

# ------------------------------------------------------------
# ✅ 2. READ ALL Books
# ------------------------------------------------------------
@app.get("/books")
def get_all_books(db: Session = Depends(get_db)):
    books_list = db.query(Book).all()
    return {"Count": len(books_list), "Data": books_list}

# ------------------------------------------------------------
# ✅ 3. READ SINGLE Book Data
# ------------------------------------------------------------
@app.get("/books/{book_id}")
def book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# ------------------------------------------------------------
# ✅ 4. UPDATE Book Details
# ------------------------------------------------------------
@app.put("/books/{book_id}")
def update_book(book_id: int, updated: CreateBook, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = updated.title
    book.genre = updated.genre
    book.author = updated.author
    book.price = updated.price
    
    diff = updated.total_quantity - book.total_quantity
    book.total_quantity = updated.total_quantity
    book.available_quantity += diff
    
    db.commit()
    db.refresh(book)
    return {"Message": "Book updated successfully", "data": book}

# ------------------------------------------------------------
# ✅ 5. DELETE Book
# ------------------------------------------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"Message": "Book removed successfully"}

# ------------------------------------------------------------
# ✅ 6. Add user
# ------------------------------------------------------------
@app.post("/users")
def add_user(_user: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == _user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists") 

    new_user = User(
        name=_user.name,
        email=_user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User added Successfully", "data": new_user}

# ------------------------------------------------------------
# ✅ 7. Get all users
# ------------------------------------------------------------
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users_list = db.query(User).all()
    return {"Count": len(users_list), "data": users_list}

# ------------------------------------------------------------
# ✅ DELETE User
# ------------------------------------------------------------
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return {"Message": "User removed successfully"}

# ------------------------------------------------------------
# ✅ 8. ISSUE Book
# ------------------------------------------------------------
@app.post("/issue-book/{book_id}/{user_id}")
def issue_book(book_id: int, user_id: int, days: int, issued_by: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.available_quantity <= 0:
        raise HTTPException(status_code=400, detail="No copies available")
    
    # Check User
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Current time
    current_time = datetime.utcnow()
    # Due date
    due_date = current_time + timedelta(days=days)
    
    # Create Issue Record
    issue = IssuedBook(
        book_id=book_id,
        user_id=user_id,
        issued_by=issued_by,
        issued_to=user.name,
        issued_time=current_time,
        due_date=due_date,
        status="Issued"
    )
    
    # Update Book Status
    book.available_quantity -= 1
    db.add(issue)
    db.commit()
    
    return {
        "Message": "Book issued successfully",
        "book": book.title,
        "issued to": user.name,
        "issued by": issued_by,
        "issued time": current_time,
        "return before": due_date
    }

# ------------------------------------------------------------
# ✅ 9. RETURN Book
# ------------------------------------------------------------
@app.post("/return-book/{book_id}")
def return_book(book_id: int, db: Session = Depends(get_db)):
    issue = db.query(IssuedBook).filter(IssuedBook.book_id == book_id, IssuedBook.status == "Issued").first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue record not found")
    
    # Find book
    book = db.query(Book).filter(Book.id == book_id).first()
    
    # Update Book status
    book.available_quantity += 1
    
    # Return Time
    issue.returned_time = datetime.utcnow()
    
    # Check for late return
    if issue.returned_time > issue.due_date:
        issue.status = "Late Return"
        late_days = (issue.returned_time - issue.due_date).days
        if late_days <= 0:
            late_days = 1  # minimum 1 day penalty once overdue
        
        # fine ₹10 per day
        fine = late_days * 10
        issue.fine_amount = fine
    else:
        issue.status = "Returned"
        issue.fine_amount = 0
    
    db.commit()
    
    return {
        "Message": "Book returned successfully",
        "book": book.title,
        "returned_time": issue.returned_time,
        "status": issue.status,
        "fine amount": issue.fine_amount
    }

# ------------------------------------------------------------
# ✅ 10. AVAILABLE Books
# ------------------------------------------------------------
@app.get("/available-books")
def available_books(db: Session = Depends(get_db)):
    books_list = db.query(Book).filter(Book.available_quantity > 0).all()
    return {
        "count": len(books_list),
        "data": books_list
    }
    
# ------------------------------------------------------------
# ✅ 11. ISSUED Books
# ------------------------------------------------------------
@app.get("/issued-books")
def issued_books(db: Session = Depends(get_db)):
    books_list = db.query(IssuedBook).filter(IssuedBook.status == "Issued").all()
    return {
        "Count": len(books_list),
        "data": books_list
    }

# ------------------------------------------------------------
# ✅ 12. ISSUED History
# ------------------------------------------------------------
@app.get("/issue-history")
def issue_history(db: Session = Depends(get_db)):
    history_list = db.query(IssuedBook).all()
    return {"Count": len(history_list), "data": history_list}

# ------------------------------------------------------------
# ✅ 13. SEARCH Book By Title
# ------------------------------------------------------------
@app.get("/search-book/{title}")
def search_book(title: str, db: Session = Depends(get_db)):
    books_list = db.query(Book).filter(Book.title.ilike(f"%{title}%")).all()
    if not books_list:
        raise HTTPException(status_code=404, detail="No books found")
    return {
        "Count": len(books_list),
        "data": books_list
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)