# ======================================================================================
# 📝 Flask Library Management System (CRUD) - MongoDB Version
# ======================================================================================
from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId
from datetime import datetime, timedelta

app = Flask(__name__)

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
mongo_db = client["library_management_system"]

# Collections
books_col  = mongo_db["books"]
users_col  = mongo_db["users"]
issued_col = mongo_db["issued_books"]

# Unique index on user email
users_col.create_index("email", unique=True)

# ============================================================
# 🛠️ Helpers
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
        "issued_time":   doc["issued_time"].isoformat()   if doc.get("issued_time")   else None,
        "due_date":      doc["due_date"].isoformat()      if doc.get("due_date")      else None,
        "returned_time": doc["returned_time"].isoformat() if doc.get("returned_time") else None,
        "fine_amount":   doc.get("fine_amount", 0.0),
        "status":        doc.get("status"),
    }

def to_object_id(id_str: str):
    try:
        return ObjectId(id_str)
    except (InvalidId, TypeError):
        return None

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# 🔒 GET Operators
@app.route("/api/operators", methods=["GET"])
def get_operators():
    return jsonify(["Admin", "Librarian", "Harsha Vardhan"]), 200

# 🔒 POST Login
@app.route("/api/login", methods=["POST"])
def login_operator():
    data     = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password", "")

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

    username_lower = username.strip().lower()
    if username_lower in credentials and password == credentials[username_lower]:
        return jsonify({"success": True, "user": names[username_lower]}), 200

    return jsonify({"success": False, "message": "Incorrect password or unauthorized registry."}), 401

# ------------------------------------------------------------
# ✅ 1. Add New Book
# ------------------------------------------------------------
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json() or {}
    for field in ["title", "genre", "author", "price", "total_quantity"]:
        if field not in data:
            return jsonify({"detail": f"Missing field: {field}"}), 400

    new_book = {
        "title":              data["title"],
        "genre":              data["genre"],
        "author":             data["author"],
        "price":              float(data["price"]),
        "total_quantity":     int(data["total_quantity"]),
        "available_quantity": int(data["total_quantity"]),
    }
    result = books_col.insert_one(new_book)
    new_book["_id"] = result.inserted_id
    return jsonify({"Message": "Book added successfully!", "data": book_doc(new_book)}), 200

# ------------------------------------------------------------
# ✅ 2. READ ALL Books
# ------------------------------------------------------------
@app.route("/books", methods=["GET"])
def get_all_books():
    books_list = list(books_col.find())
    return jsonify({"Count": len(books_list), "Data": [book_doc(b) for b in books_list]}), 200

# ------------------------------------------------------------
# ✅ 3. READ SINGLE Book
# ------------------------------------------------------------
@app.route("/books/<string:book_id>", methods=["GET"])
def book_by_id(book_id):
    oid = to_object_id(book_id)
    if not oid:
        return jsonify({"detail": "Invalid ID format"}), 404
    book = books_col.find_one({"_id": oid})
    if not book:
        return jsonify({"detail": "Book not found"}), 404
    return jsonify(book_doc(book)), 200

# ------------------------------------------------------------
# ✅ 4. UPDATE Book
# ------------------------------------------------------------
@app.route("/books/<string:book_id>", methods=["PUT"])
def update_book(book_id):
    oid = to_object_id(book_id)
    if not oid:
        return jsonify({"detail": "Invalid ID format"}), 404
    book = books_col.find_one({"_id": oid})
    if not book:
        return jsonify({"detail": "Book not found"}), 404

    data          = request.get_json() or {}
    new_total_qty = int(data.get("total_quantity", book["total_quantity"]))
    diff          = new_total_qty - book["total_quantity"]
    new_available = book["available_quantity"] + diff

    books_col.update_one({"_id": oid}, {"$set": {
        "title":              data.get("title",  book["title"]),
        "genre":              data.get("genre",  book["genre"]),
        "author":             data.get("author", book["author"]),
        "price":              float(data.get("price", book["price"])),
        "total_quantity":     new_total_qty,
        "available_quantity": new_available,
    }})
    updated = books_col.find_one({"_id": oid})
    return jsonify({"Message": "Book updated successfully", "data": book_doc(updated)}), 200

# ------------------------------------------------------------
# ✅ 5. DELETE Book
# ------------------------------------------------------------
@app.route("/books/<string:book_id>", methods=["DELETE"])
def delete_book(book_id):
    oid = to_object_id(book_id)
    if not oid:
        return jsonify({"detail": "Invalid ID format"}), 404
    book = books_col.find_one({"_id": oid})
    if not book:
        return jsonify({"detail": "Book not found"}), 404
    issued_col.delete_many({"book_id": oid})
    books_col.delete_one({"_id": oid})
    return jsonify({"Message": "Book removed successfully"}), 200

# ------------------------------------------------------------
# ✅ 6. Add User
# ------------------------------------------------------------
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json() or {}
    if "name" not in data or "email" not in data:
        return jsonify({"detail": "Name and Email are required"}), 400

    if users_col.find_one({"email": data["email"]}):
        return jsonify({"detail": "Email already exists"}), 400

    new_user = {"name": data["name"], "email": data["email"]}
    result   = users_col.insert_one(new_user)
    new_user["_id"] = result.inserted_id
    return jsonify({"message": "User added Successfully", "data": user_doc(new_user)}), 200

# ------------------------------------------------------------
# ✅ 7. Get All Users
# ------------------------------------------------------------
@app.route("/users", methods=["GET"])
def get_users():
    users_list = list(users_col.find())
    return jsonify({"Count": len(users_list), "data": [user_doc(u) for u in users_list]}), 200

# ------------------------------------------------------------
# ✅ 8. ISSUE Book
# ------------------------------------------------------------
@app.route("/issue-book/<string:book_id>/<string:user_id>", methods=["POST"])
def issue_book(book_id, user_id):
    book_oid = to_object_id(book_id)
    user_oid = to_object_id(user_id)

    if not book_oid or not user_oid:
        return jsonify({"detail": "Invalid ID format"}), 404

    book = books_col.find_one({"_id": book_oid})
    if not book:
        return jsonify({"detail": "Book not found"}), 404
    if book["available_quantity"] <= 0:
        return jsonify({"detail": "No copies available"}), 400

    user = users_col.find_one({"_id": user_oid})
    if not user:
        return jsonify({"detail": "User not found"}), 404

    json_body = request.get_json(silent=True) or {}
    days      = int(request.args.get("days", json_body.get("days", 14)))
    issued_by = request.args.get("issued_by", json_body.get("issued_by", "Librarian"))

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

    return jsonify({
        "Message":       "Book issued successfully",
        "book":          book["title"],
        "issued to":     user["name"],
        "issued by":     issued_by,
        "issued time":   current_time.isoformat(),
        "return before": due_date.isoformat(),
    }), 200

# ------------------------------------------------------------
# ✅ 9. RETURN Book
# ------------------------------------------------------------
@app.route("/return-book/<string:book_id>", methods=["POST"])
def return_book(book_id):
    book_oid = to_object_id(book_id)
    if not book_oid:
        return jsonify({"detail": "Invalid ID format"}), 404

    issue = issued_col.find_one({"book_id": book_oid, "status": "Issued"})
    if not issue:
        return jsonify({"detail": "Issue record not found"}), 404

    book          = books_col.find_one({"_id": book_oid})
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

    return jsonify({
        "Message":       "Book returned successfully",
        "book":          book["title"],
        "returned_time": returned_time.isoformat(),
        "status":        status,
        "fine amount":   fine,
    }), 200

# ------------------------------------------------------------
# ✅ 10. AVAILABLE Books
# ------------------------------------------------------------
@app.route("/available-books", methods=["GET"])
def available_books():
    books_list = list(books_col.find({"available_quantity": {"$gt": 0}}))
    return jsonify({"count": len(books_list), "data": [book_doc(b) for b in books_list]}), 200

# ------------------------------------------------------------
# ✅ 11. Currently ISSUED Books
# ------------------------------------------------------------
@app.route("/issued-books", methods=["GET"])
def issued_books():
    issued_list = list(issued_col.find({"status": "Issued"}))
    return jsonify({"Count": len(issued_list), "data": [issue_doc(i) for i in issued_list]}), 200

# ------------------------------------------------------------
# ✅ 12. Full Issue History
# ------------------------------------------------------------
@app.route("/issue-history", methods=["GET"])
def issue_history():
    history_list = list(issued_col.find())
    return jsonify({"Count": len(history_list), "data": [issue_doc(i) for i in history_list]}), 200

# ------------------------------------------------------------
# ✅ 13. SEARCH Book By Title
# ------------------------------------------------------------
@app.route("/search-book/<string:title>", methods=["GET"])
def search_book(title):
    books_list = list(books_col.find({"title": {"$regex": title, "$options": "i"}}))
    if not books_list:
        return jsonify({"detail": "No books found"}), 404
    return jsonify({"Count": len(books_list), "data": [book_doc(b) for b in books_list]}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)