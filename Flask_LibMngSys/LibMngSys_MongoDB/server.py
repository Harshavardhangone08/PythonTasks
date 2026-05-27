# ======================================================================================
# 📝 FastAPI Library Management System (CRUD) - MongoDB Version
# ======================================================================================
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId
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
# 🗄️ Database Configuration (MongoDB)
# ------------------------------------------------------------

MONGO_URL = "mongodb+srv://harshavardhangone08_db_user:Harsha1432@mongodb.g8bfg4r.mongodb.net/library_management_system?retryWrites=true&w=majority"

'''
mongodb+srv://username:password@clustername.xxxxx.mongodb.net/todo_db?retryWrites=true&w=majority
│              │        │        │                              │
│              │        │        │                              └── Database name
│              │        │        └──────────────────────────────── Cluster URL
│              │        └───────────────────────────────────────── Password
│              └────────────────────────────────────────────────── Username
└───────────────────────────────────────────────────────────────── MongoDB protocol
'''
client = MongoClient(MONGO_URL)
db = client["library_management_system"]

# Collections
books_col      = db["books"]
users_col      = db["users"]
issued_col     = db["issued_books"]

# Unique index on user email
users_col.create_index("email", unique=True)

# ============================================================
# 🛠️ Helper: Convert MongoDB doc → JSON-safe dict
# ============================================================
def book_doc(doc: dict) -> dict:
    return {
        "id":                 str(doc["_id"]),
        "title":              doc.get("title"),
        "genre":              doc.get("genre"),
        "author":             doc.get("author"),
        "price":              doc.get("price"),
        "total_quantity":     doc.get("total_quantity"),
        "available_quantity": doc.get("available_quantity"),
    }

def user_doc(doc: dict) -> dict:
    return {
        "id":    str(doc["_id"]),
        "name":  doc.get("name"),
        "email": doc.get("email"),
    }

def issue_doc(doc: dict) -> dict:
    return {
        "id":            str(doc["_id"]),
        "book_id":       str(doc.get("book_id")),
        "user_id":       str(doc.get("user_id")),
        "issued_by":     doc.get("issued_by"),
        "issued_to":     doc.get("issued_to"),
        "issued_time":   doc["issued_time"].isoformat()  if doc.get("issued_time")   else None,
        "due_date":      doc["due_date"].isoformat()     if doc.get("due_date")      else None,
        "returned_time": doc["returned_time"].isoformat() if doc.get("returned_time") else None,
        "fine_amount":   doc.get("fine_amount", 0.0),
        "status":        doc.get("status"),
    }

def to_object_id(id_str: str):
    """Safely convert string → ObjectId, raise 404 on failure."""
    try:
        return ObjectId(id_str)
    except (InvalidId, TypeError):
        raise HTTPException(status_code=404, detail="Invalid ID format")

# ============================================================
# 🧾 Pydantic Schemas
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

class LoginRequest(BaseModel):
    username: str
    password: str

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    with open(os.path.join("templates", "index.html"), "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# 🔒 GET List of Authorized Operators for the Login dropdown
@app.get("/api/operators")
def get_operators():
    return ["Admin", "Librarian", "Harsha Vardhan"]

# 🔒 POST Authentication for Admin or Librarian
@app.post("/api/login")
def login(request_data: LoginRequest):
    credentials = {
        "admin":          "admin123",
        "librarian":      "librarian123",
        "harsha vardhan": "harsha123",
    }
    names = {
        "admin":          "Admin",
        "librarian":      "Librarian",
        "harsha vardhan": "Harsha Vardhan",
    }
    username_lower = request_data.username.strip().lower()
    if username_lower in credentials and request_data.password == credentials[username_lower]:
        return {"success": True, "user": names[username_lower]}
    raise HTTPException(status_code=401, detail="Incorrect password or unauthorized registry.")

# ------------------------------------------------------------
# ✅ 1. Add New Book
# ------------------------------------------------------------
@app.post("/books")
def add_book(book: CreateBook):
    new_book = {
        "title":              book.title,
        "genre":              book.genre,
        "author":             book.author,
        "price":              book.price,
        "total_quantity":     book.total_quantity,
        "available_quantity": book.total_quantity,
    }
    result = books_col.insert_one(new_book)
    new_book["_id"] = result.inserted_id
    return {"Message": "Book added successfully!", "data": book_doc(new_book)}

# ------------------------------------------------------------
# ✅ 2. READ ALL Books
# ------------------------------------------------------------
@app.get("/books")
def get_all_books():
    books_list = list(books_col.find())
    return {"Count": len(books_list), "Data": [book_doc(b) for b in books_list]}

# ------------------------------------------------------------
# ✅ 3. READ SINGLE Book
# ------------------------------------------------------------
@app.get("/books/{book_id}")
def book_by_id(book_id: str):
    book = books_col.find_one({"_id": to_object_id(book_id)})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book_doc(book)

# ------------------------------------------------------------
# ✅ 4. UPDATE Book Details
# ------------------------------------------------------------
@app.put("/books/{book_id}")
def update_book(book_id: str, updated: CreateBook):
    oid = to_object_id(book_id)
    book = books_col.find_one({"_id": oid})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    diff = updated.total_quantity - book["total_quantity"]
    new_available = book["available_quantity"] + diff

    books_col.update_one({"_id": oid}, {"$set": {
        "title":              updated.title,
        "genre":              updated.genre,
        "author":             updated.author,
        "price":              updated.price,
        "total_quantity":     updated.total_quantity,
        "available_quantity": new_available,
    }})
    updated_book = books_col.find_one({"_id": oid})
    return {"Message": "Book updated successfully", "data": book_doc(updated_book)}

# ------------------------------------------------------------
# ✅ 5. DELETE Book
# ------------------------------------------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    oid = to_object_id(book_id)
    book = books_col.find_one({"_id": oid})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    # Delete related issued records too
    issued_col.delete_many({"book_id": oid})
    books_col.delete_one({"_id": oid})
    return {"Message": "Book removed successfully"}

# ------------------------------------------------------------
# ✅ 6. Add User
# ------------------------------------------------------------
@app.post("/users")
def add_user(_user: CreateUser):
    if users_col.find_one({"email": _user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    new_user = {"name": _user.name, "email": _user.email}
    result = users_col.insert_one(new_user)
    new_user["_id"] = result.inserted_id
    return {"message": "User added Successfully", "data": user_doc(new_user)}

# ------------------------------------------------------------
# ✅ 7. Get All Users
# ------------------------------------------------------------
@app.get("/users")
def get_users():
    users_list = list(users_col.find())
    return {"Count": len(users_list), "data": [user_doc(u) for u in users_list]}

# ------------------------------------------------------------
# ✅ 8. ISSUE Book
# ------------------------------------------------------------
@app.post("/issue-book/{book_id}/{user_id}")
def issue_book(book_id: str, user_id: str, days: int, issued_by: str):
    book_oid = to_object_id(book_id)
    user_oid = to_object_id(user_id)

    book = books_col.find_one({"_id": book_oid})
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book["available_quantity"] <= 0:
        raise HTTPException(status_code=400, detail="No copies available")

    user = users_col.find_one({"_id": user_oid})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    current_time = datetime.utcnow()
    due_date     = current_time + timedelta(days=days)

    issue = {
        "book_id":       book_oid,
        "user_id":       user_oid,
        "issued_by":     issued_by,
        "issued_to":     user["name"],
        "issued_time":   current_time,
        "due_date":      due_date,
        "returned_time": None,
        "fine_amount":   0.0,
        "status":        "Issued",
    }
    issued_col.insert_one(issue)
    books_col.update_one({"_id": book_oid}, {"$inc": {"available_quantity": -1}})

    return {
        "Message":      "Book issued successfully",
        "book":         book["title"],
        "issued to":    user["name"],
        "issued by":    issued_by,
        "issued time":  current_time.isoformat(),
        "return before": due_date.isoformat(),
    }

# ------------------------------------------------------------
# ✅ 9. RETURN Book
# ------------------------------------------------------------
@app.post("/return-book/{book_id}")
def return_book(book_id: str):
    book_oid = to_object_id(book_id)

    issue = issued_col.find_one({"book_id": book_oid, "status": "Issued"})
    if not issue:
        raise HTTPException(status_code=404, detail="Issue record not found")

    book = books_col.find_one({"_id": book_oid})
    returned_time = datetime.utcnow()

    if returned_time > issue["due_date"]:
        status    = "Late Return"
        late_days = (returned_time - issue["due_date"]).days or 1
        fine      = float(late_days * 10)
    else:
        status = "Returned"
        fine   = 0.0

    issued_col.update_one({"_id": issue["_id"]}, {"$set": {
        "returned_time": returned_time,
        "status":        status,
        "fine_amount":   fine,
    }})
    books_col.update_one({"_id": book_oid}, {"$inc": {"available_quantity": 1}})

    return {
        "Message":       "Book returned successfully",
        "book":          book["title"],
        "returned_time": returned_time.isoformat(),
        "status":        status,
        "fine amount":   fine,
    }

# ------------------------------------------------------------
# ✅ 10. AVAILABLE Books
# ------------------------------------------------------------
@app.get("/available-books")
def available_books():
    books_list = list(books_col.find({"available_quantity": {"$gt": 0}}))
    return {"count": len(books_list), "data": [book_doc(b) for b in books_list]}

# ------------------------------------------------------------
# ✅ 11. Currently ISSUED Books
# ------------------------------------------------------------
@app.get("/issued-books")
def issued_books():
    issued_list = list(issued_col.find({"status": "Issued"}))
    return {"Count": len(issued_list), "data": [issue_doc(i) for i in issued_list]}

# ------------------------------------------------------------
# ✅ 12. Full Issue History
# ------------------------------------------------------------
@app.get("/issue-history")
def issue_history():
    history_list = list(issued_col.find())
    return {"Count": len(history_list), "data": [issue_doc(i) for i in history_list]}

# ------------------------------------------------------------
# ✅ 13. SEARCH Book By Title
# ------------------------------------------------------------
@app.get("/search-book/{title}")
def search_book(title: str):
    books_list = list(books_col.find({"title": {"$regex": title, "$options": "i"}}))
    if not books_list:
        raise HTTPException(status_code=404, detail="No books found")
    return {"Count": len(books_list), "data": [book_doc(b) for b in books_list]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)