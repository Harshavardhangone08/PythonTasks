# ======================================================================================
# 📚 Flask Library Management System - MySQL Version
# ======================================================================================

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

# ======================================================================================
# 🚀 Flask App
# ======================================================================================

app = Flask(__name__)
app.secret_key = "library_secret_key"

# ======================================================================================
# 🗄️ MySQL Configuration
# ======================================================================================

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/library_db_fl'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ======================================================================================
# 📚 Book Model
# ======================================================================================

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    author = db.Column(db.String(255))
    price = db.Column(db.Float)
    total_quantity = db.Column(db.Integer)
    available_quantity = db.Column(db.Integer)

# ======================================================================================
# 👤 User Model
# ======================================================================================

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)

# ======================================================================================
# 📖 Issued Book Model
# ======================================================================================

class IssuedBook(db.Model):
    __tablename__ = "issued_books"

    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    issued_by = db.Column(db.String(255))
    issued_to = db.Column(db.String(255))

    issued_time = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)

    returned_time = db.Column(db.DateTime, nullable=True)

    fine_amount = db.Column(db.Float, default=0)

    status = db.Column(db.String(50), default="Issued")

# ======================================================================================
# 🏠 Dashboard
# ======================================================================================

@app.route("/")
def dashboard():

    total_books = Book.query.count()
    total_users = User.query.count()
    issued_books = IssuedBook.query.filter_by(status="Issued").count()

    return render_template(
        "dashboard.html",
        total_books=total_books,
        total_users=total_users,
        issued_books=issued_books
    )

# ======================================================================================
# 📚 View Books
# ======================================================================================

@app.route("/books")
def books():

    all_books = Book.query.all()

    return render_template("books.html", books=all_books)

# ======================================================================================
# ➕ Add Book
# ======================================================================================

@app.route("/add-book", methods=["GET", "POST"])
def add_book():

    if request.method == "POST":

        title = request.form["title"]
        genre = request.form["genre"]
        author = request.form["author"]
        price = request.form["price"]
        total_quantity = request.form["total_quantity"]

        new_book = Book(
            title=title,
            genre=genre,
            author=author,
            price=price,
            total_quantity=total_quantity,
            available_quantity=total_quantity
        )

        db.session.add(new_book)
        db.session.commit()

        flash("Book Added Successfully!")

        return redirect(url_for("books"))

    return render_template("add_book.html")

# ======================================================================================
# ❌ Delete Book
# ======================================================================================

@app.route("/delete-book/<int:id>")
def delete_book(id):

    # Get book
    book = db.session.get(Book, id)

    if not book:

        flash("Book not found!")

        return redirect(url_for("books"))

    # Check active issued books
    active_issue = IssuedBook.query.filter_by(
        book_id=id,
        status="Issued"
    ).first()

    # Prevent deleting active issued books
    if active_issue:

        flash(
            "Cannot delete book because it is currently issued!"
        )

        return redirect(url_for("books"))

    try:

        # Delete old history rows first
        IssuedBook.query.filter_by(book_id=id).delete()

        # Commit history deletion
        db.session.commit()

        # Delete book
        db.session.delete(book)

        # Commit book deletion
        db.session.commit()

        flash("Book Deleted Successfully!")

    except Exception as e:

        db.session.rollback()

        flash(f"Error deleting book: {str(e)}")

    return redirect(url_for("books"))

# ======================================================================================
# 👤 Users Page
# ======================================================================================

@app.route("/users")
def users():

    all_users = User.query.all()

    return render_template("users.html", users=all_users)

# ======================================================================================
# ➕ Add User
# ======================================================================================

@app.route("/add-user", methods=["GET", "POST"])
def add_user():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already exists!")
            return redirect(url_for("add_user"))

        new_user = User(name=name, email=email)

        db.session.add(new_user)
        db.session.commit()

        flash("User Added Successfully!")

        return redirect(url_for("users"))

    return render_template("add_user.html")

# ======================================================================================
# 📖 Issue Book
# ======================================================================================

@app.route("/issue-book", methods=["GET", "POST"])
def issue_book():

    books = Book.query.all()
    users = User.query.all()

    if request.method == "POST":

        book_id = request.form["book_id"]
        user_id = request.form["user_id"]
        issued_by = request.form["issued_by"]
        days = int(request.form["days"])

        book = Book.query.get(book_id)
        user = User.query.get(user_id)

        if book.available_quantity <= 0:
            flash("No Books Available!")
            return redirect(url_for("issue_book"))

        current_time = datetime.utcnow()
        due_date = current_time + timedelta(days=days)

        issue = IssuedBook(
            book_id=book.id,
            user_id=user.id,
            issued_by=issued_by,
            issued_to=user.name,
            issued_time=current_time,
            due_date=due_date,
            status="Issued"
        )

        book.available_quantity -= 1

        db.session.add(issue)
        db.session.commit()

        flash("Book Issued Successfully!")

        return redirect(url_for("issued_books"))

    return render_template("issue_book.html", books=books, users=users)

# ======================================================================================
# 📚 Issued Books
# ======================================================================================

@app.route("/issued-books")
def issued_books():

    books = IssuedBook.query.all()

    return render_template("issued_books.html", books=books)

# ======================================================================================
# 🔄 Return Book
# ======================================================================================

@app.route("/return-book/<int:id>")
def return_book(id):

    issue = IssuedBook.query.get(id)

    if issue.status == "Issued":

        issue.returned_time = datetime.utcnow()

        book = Book.query.get(issue.book_id)

        book.available_quantity += 1

        if issue.returned_time > issue.due_date:

            late_days = (issue.returned_time - issue.due_date).days

            fine = late_days * 10

            issue.fine_amount = fine

            issue.status = "Late Return"

        else:
            issue.status = "Returned"

        db.session.commit()

        flash("Book Returned Successfully!")

    return redirect(url_for("issued_books"))

# ======================================================================================
# 📜 History
# ======================================================================================

@app.route("/history")
def history():

    history = IssuedBook.query.all()

    return render_template("history.html", history=history)

# ======================================================================================
# 📜 Search Book
# ======================================================================================
@app.route("/search")
def search_book():

    query = request.args.get("query")

    books = Book.query.filter(
        Book.title.ilike(f"%{query}%")
    ).all()

    return render_template(
        "books.html",
        books=books
    )

# ======================================================================================
# ▶️ Run Server
# ======================================================================================

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)