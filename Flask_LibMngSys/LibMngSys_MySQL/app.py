# ======================================================================================
# 📝 Flask Library Management System (CRUD) - SQLite/SQL Database version
# ======================================================================================
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)

# ------------------------------------------------------------
# 🗄️ Database Configuration (Configured for MySQL)
# ------------------------------------------------------------

# Primary: Use local or environment-defined MySQL directly as requested
mysql_uri = "mysql+pymysql://root:root@localhost:3306/library_management_system"
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_uri

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ============================================================
# 🧱 Database Models
# ============================================================

class Book(db.Model):
    __tablename__ = "books"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    total_quantity = db.Column(db.Integer, nullable=False)
    available_quantity = db.Column(db.Integer, nullable=False)
    
    issued_books = db.relationship("IssuedBook", backref="book", cascade="all, delete-orphan", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "author": self.author,
            "price": self.price,
            "total_quantity": self.total_quantity,
            "available_quantity": self.available_quantity
        }

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    
    issued_books = db.relationship("IssuedBook", backref="user", cascade="all, delete-orphan", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

class IssuedBook(db.Model):
    __tablename__ = "issued_books"
    
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    issued_by = db.Column(db.String(255), nullable=False)
    issued_to = db.Column(db.String(255), nullable=False)
    
    issued_time = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)
    returned_time = db.Column(db.DateTime, nullable=True)
    
    fine_amount = db.Column(db.Float, default=0.0)
    status = db.Column(db.String(50), default="Issued")

    def to_dict(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "issued_by": self.issued_by,
            "issued_to": self.issued_to,
            "issued_time": self.issued_time.isoformat() if self.issued_time else None,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "returned_time": self.returned_time.isoformat() if self.returned_time else None,
            "fine_amount": self.fine_amount,
            "status": self.status
        }

# Initialize db schemas
with app.app_context():
    db.create_all()

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# 🔒 GET List of Authorized Operators for the Login dropdown
@app.route("/api/operators", methods=["GET"])
def get_operators():
    return jsonify([
        "Admin",
        "Librarian",
        "Harsha Vardhan"
    ]), 200

# 🔒 POST Authentication for Admin or Librarian
@app.route("/api/login", methods=["POST"])
def login_operator():
    data = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password", "")

    credentials = {
        "admin": "admin123",
        "librarian": "librarian123",
        "harsha vardhan": "harsha123"
    }

    username_lower = username.strip().lower()
    if username_lower in credentials:
        if password == credentials[username_lower]:
            # Retain original case name for UI badge
            names = {
                "admin": "Admin",
                "librarian": "Librarian",
                "harsha vardhan": "Harsha Vardhan"
            }
            return jsonify({"success": True, "user": names[username_lower]}), 200

    return jsonify({"success": False, "message": "Incorrect password or unauthorized registry."}), 401

# ------------------------------------------------------------
# ✅ 1. Add New Book Data
# ------------------------------------------------------------
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json() or {}
    for field in ["title", "genre", "author", "price", "total_quantity"]:
        if field not in data:
            return jsonify({"detail": f"Missing field: {field}"}), 400

    new_book = Book(
        title=data["title"],
        genre=data["genre"],
        author=data["author"],
        price=float(data["price"]),
        total_quantity=int(data["total_quantity"]),
        available_quantity=int(data["total_quantity"])
    )
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify({"Message": "Book added successfully!", "data": new_book.to_dict()}), 200

# ------------------------------------------------------------
# ✅ 2. READ ALL Books
# ------------------------------------------------------------
@app.route("/books", methods=["GET"])
def get_all_books():
    books_list = Book.query.all()
    return jsonify({
        "Count": len(books_list),
        "Data": [b.to_dict() for b in books_list]
    }), 200

# ------------------------------------------------------------
# ✅ 3. READ SINGLE Book Data
# ------------------------------------------------------------
@app.route("/books/<int:book_id>", methods=["GET"])
def book_by_id(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"detail": "Book not found"}), 404
    return jsonify(book.to_dict()), 200

# ------------------------------------------------------------
# ✅ 4. UPDATE Book Details
# ------------------------------------------------------------
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"detail": "Book not found"}), 404
    
    data = request.get_json() or {}
    book.title = data.get("title", book.title)
    book.genre = data.get("genre", book.genre)
    book.author = data.get("author", book.author)
    book.price = float(data.get("price", book.price))
    
    old_total_qty = book.total_quantity
    new_total_qty = int(data.get("total_quantity", book.total_quantity))
    diff = new_total_qty - old_total_qty
    book.total_quantity = new_total_qty
    book.available_quantity += diff
    
    db.session.commit()
    return jsonify({"Message": "Book updated successfully", "data": book.to_dict()}), 200

# ------------------------------------------------------------
# ✅ 5. DELETE Book
# ------------------------------------------------------------
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"detail": "Book not found"}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({"Message": "Book removed successfully"}), 200

# ------------------------------------------------------------
# ✅ 6. Add user
# ------------------------------------------------------------
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json() or {}
    if "name" not in data or "email" not in data:
         return jsonify({"detail": "Name and Email are required"}), 400
         
    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
         return jsonify({"detail": "Email already exists"}), 400
         
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User added Successfully", "data": new_user.to_dict()}), 200

# ------------------------------------------------------------
# ✅ 7. Get all users
# ------------------------------------------------------------
@app.route("/users", methods=["GET"])
def get_users():
    users_list = User.query.all()
    return jsonify({
        "Count": len(users_list),
        "data": [u.to_dict() for u in users_list]
    }), 200

# ------------------------------------------------------------
# ✅ DELETE User
# ------------------------------------------------------------
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"detail": "User not found"}), 404
        
    db.session.delete(user)
    db.session.commit()
    return jsonify({"Message": "User removed successfully"}), 200

# ------------------------------------------------------------
# ✅ 8. ISSUE Book
# ------------------------------------------------------------
@app.route("/issue-book/<int:book_id>/<int:user_id>", methods=["POST"])
def issue_book(book_id, user_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"detail": "Book not found"}), 404
    if book.available_quantity <= 0:
        return jsonify({"detail": "No copies available"}), 400
        
    user = User.query.get(user_id)
    if not user:
        return jsonify({"detail": "User not found"}), 404
        
    days = int(request.args.get("days", request.get_json().get("days", 14) if request.is_json else 14))
    issued_by = request.args.get("issued_by", request.get_json().get("issued_by", "Librarian") if request.is_json else "Librarian")
    
    current_time = datetime.utcnow()
    due_date = current_time + timedelta(days=days)
    
    issue = IssuedBook(
        book_id=book_id,
        user_id=user_id,
        issued_by=issued_by,
        issued_to=user.name,
        issued_time=current_time,
        due_date=due_date,
        status="Issued"
    )
    
    book.available_quantity -= 1
    db.session.add(issue)
    db.session.commit()
    
    return jsonify({
        "Message": "Book issued successfully",
        "book": book.title,
        "issued to": user.name,
        "issued by": issued_by,
        "issued time": current_time.isoformat(),
        "return before": due_date.isoformat()
    }), 200

# ------------------------------------------------------------
# ✅ 9. RETURN Book
# ------------------------------------------------------------
@app.route("/return-book/<int:book_id>", methods=["POST"])
def return_book(book_id):
    issue = IssuedBook.query.filter_by(book_id=book_id, status="Issued").first()
    if not issue:
        return jsonify({"detail": "Issue record not found"}), 404
        
    book = Book.query.get(book_id)
    book.available_quantity += 1
    
    issue.returned_time = datetime.utcnow()
    
    if issue.returned_time > issue.due_date:
        issue.status = "Late Return"
        late_days = (issue.returned_time - issue.due_date).days
        if late_days <= 0:
             late_days = 1
        issue.fine_amount = float(late_days * 10)
    else:
        issue.status = "Returned"
        issue.fine_amount = 0.0
        
    db.session.commit()
    return jsonify({
        "Message": "Book returned successfully",
        "book": book.title,
        "returned_time": issue.returned_time.isoformat(),
        "status": issue.status,
        "fine amount": issue.fine_amount
    }), 200

# ------------------------------------------------------------
# ✅ 10. AVAILABLE Books
# ------------------------------------------------------------
@app.route("/available-books", methods=["GET"])
def available_books():
    books_list = Book.query.filter(Book.available_quantity > 0).all()
    return jsonify({
        "count": len(books_list),
        "data": [b.to_dict() for b in books_list]
    }), 200

# ------------------------------------------------------------
# ✅ 11. ISSUED Books
# ------------------------------------------------------------
@app.route("/issued-books", methods=["GET"])
def issued_books():
    issued_list = IssuedBook.query.filter_by(status="Issued").all()
    return jsonify({
        "Count": len(issued_list),
        "data": [i.to_dict() for i in issued_list]
    }), 200

# ------------------------------------------------------------
# ✅ 12. ISSUED History
# ------------------------------------------------------------
@app.route("/issue-history", methods=["GET"])
def issue_history():
    history_list = IssuedBook.query.all()
    return jsonify({
        "Count": len(history_list),
        "data": [i.to_dict() for i in history_list]
    }), 200

# ------------------------------------------------------------
# ✅ 13. SEARCH Book By Title
# ------------------------------------------------------------
@app.route("/search-book/<string:title>", methods=["GET"])
def search_book(title):
    books_list = Book.query.filter(Book.title.ilike(f"%{title}%")).all()
    if not books_list:
        return jsonify({"detail": "No books found"}), 404
    return jsonify({
        "Count": len(books_list),
        "data": [b.to_dict() for b in books_list]
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
