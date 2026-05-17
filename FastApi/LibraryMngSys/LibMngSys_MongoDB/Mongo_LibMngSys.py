# ======================================================================================
# 📝 FastAPI Library Management System (CRUD) - MongoDB Atlas + MongoEngine
# ======================================================================================
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, FloatField, StringField, BooleanField

# ------------------------------------------------------------
# 🚀 Create FastAPI Application
# ------------------------------------------------------------
app=FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------

MONGO_URL = "mongodb+srv://harshavardhangone08_db_user:Harsha1432@mongodb.g8bfg4r.mongodb.net/library_db?retryWrites=true&w=majority"

'''
mongodb+srv://username:password@clustername.xxxxx.mongodb.net/todo_db?retryWrites=true&w=majority
│              │        │        │                              │
│              │        │        │                              └── Database name
│              │        │        └──────────────────────────────── Cluster URL
│              │        └───────────────────────────────────────── Password
│              └────────────────────────────────────────────────── Username
└───────────────────────────────────────────────────────────────── MongoDB protocol
'''

connect(host=MONGO_URL)

# ------------------------------------------------------------
# 🧱 MongoDB Model (Like SQLAlchemy Model)
# ------------------------------------------------------------

class Library_DB(Document):
    
    id = IntField(primary_key=True)
    title = StringField(required=True)
    Genre = StringField(required=True)
    author= StringField(required=True)
    price = FloatField(required=True)
    available =BooleanField(default=True)
    
    meta={"collection":"Library"}
    
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

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------

@app.get("/")
def home():
    return {"Message":"Library Management System with MongoDB"}

# ------------------------------------------------------------
# ✅ 1. Add New Book Data
# ------------------------------------------------------------
@app.post("/books")
def add_book(book:lib):
    
    existing=Library_DB.objects(id=book.id).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Book ID already exists")
    
    new_book=Library_DB(
        id=book.id,
        title=book.title,
        Genre=book.Genre,
        author=book.author,
        price=book.price,
        available=book.available
    )
    new_book.save()
    
    return {"Message":"Book added successfully!", "data":book}

# ------------------------------------------------------------
# ✅ 2. READ ALL Books
# ------------------------------------------------------------
@app.get("/books")
def get_allBooks():
    Books=Library_DB.objects()
    
    data=[]
    for book in Books:
        data.append({
            "id":book.id,
            "title":book.title,
            "Genre":book.Genre,
            "author":book.author,
            "price":book.price,
            "available":book.available
        })
    return {"Count":len(data), "Data":data}

# ------------------------------------------------------------
# ✅ 3. READ SINGLE Book Data
# ------------------------------------------------------------
@app.get("/books/{b_id}")
def book_by_ID(b_id:int):
    
    book=Library_DB.objects(id=b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return {
            "id":book.id,
            "title":book.title,
            "Genre":book.Genre,
            "author":book.author,
            "price":book.price,
            "available":book.available
    }

# ------------------------------------------------------------
# ✅ 4. UPDATE Book Details
# ------------------------------------------------------------
@app.put("/books/{b_id}")
def update_book(b_id:int, updated:lib):
    
    book=Library_DB.objects(id=b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title=updated.title
    book.Genre=updated.Genre
    book.author=updated.author
    book.price=updated.price
    book.available=updated.available
    
    book.save()
    
    return {"Message":"Book updated successfully"}

# ------------------------------------------------------------
# ✅ 5. DELETE Book
# ------------------------------------------------------------
@app.delete("/books/{b_id}")
def delete_book(b_id:int):
    
    book=Library_DB.objects(id=b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.delete()
    
    return {"Message":"Book removed successfully"}

# ------------------------------------------------------------
# ✅ 6. ISSUE Book
# ------------------------------------------------------------
@app.post("/issue-book/{b_id}")
def issue_book(b_id:int):
    
    book=Library_DB.objects(id=b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if not book.available:
        raise HTTPException(status_code=400, detail="Book already issued")
    
    book.available=False
    book.save()
    
    return {"Message":f"Book {book.title} issued successfully"}

# ------------------------------------------------------------
# ✅ 7. RETURN Book
# ------------------------------------------------------------
@app.post("/return-book/{b_id}")
def return_book(b_id:int):
    
    book=Library_DB.objects(id=b_id).first()
    
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.available:
        raise HTTPException(status_code=400, detail="Book already returned")
    
    book.available=True
    
    book.save()
    
    return {"Message":f"Book {book.title} returned successfully"}

# ------------------------------------------------------------
# ✅ 8. AVAILABLE Books
# ------------------------------------------------------------
@app.get("/available-books")
def available_books():
    
    Books=Library_DB.objects(available=True).all()
    
    data=[]
    for book in Books:
        data.append({
            "id":book.id,
            "title":book.title,
            "Genre":book.Genre,
            "author":book.author,
            "price":book.price,
            "available":book.available
        })
    return{
        "count":len(data),
        "data":data
    }
    
# ------------------------------------------------------------
# ✅ 9. ISSUED Books
# ------------------------------------------------------------
@app.get("/issued-books")
def issued_books():
    
    Books=Library_DB.objects(available=False).all()
    
    data=[]
    for book in Books:
        data.append({
            "id":book.id,
            "title":book.title,
            "Genre":book.Genre,
            "author":book.author,
            "price":book.price,
            "available":book.available
        })
    
    return{
        "Count":len(data),
        "data":data
    }
    
# ------------------------------------------------------------
# ✅ 10. SEARCH Book By Title
# ------------------------------------------------------------
@app.get("/search-book/{title}")
def search_book(title:str):
    
    Books=Library_DB.objects(title__icontains=title)

    if not Books:
        raise HTTPException(status_code=404, detail="No books found")
    
    data=[]
    for book in Books:
        data.append({
            "id":book.id,
            "title":book.title,
            "Genre":book.Genre,
            "author":book.author,
            "price":book.price,
            "available":book.available
        })
    
    return {
        "Count":len(data),
        "data":data
    }