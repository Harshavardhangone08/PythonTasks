# ============================================================
# 📝 FastAPI TODO App (CRUD) - MySQL Version + JWT Auth
# pip install fastapi uvicorn sqlalchemy pymysql python-jose
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app = FastAPI()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

SECRET_KEY = "@Harsha08#"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=20)

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/todo_token_db"

'''
mysql+pymysql://root:1234@localhost:3306/todo_db
│      │         │    │    │         │    │
│      │         │    │    │         │    └── Database name
│      │         │    │    │         └────── Port
│      │         │    │    └──────────────── Hostname
│      │         │    └───────────────────── Password
│      │         └────────────────────────── Username
│      └──────────────────────────────────── Driver
└─────────────────────────────────────────── Database type
'''

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# ------------------------------------------------------------
# 🧱 Table Model
# ------------------------------------------------------------
class TodoDB(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    title = Column(String(255))
    completed = Column(Boolean, default=False)

# Create table
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Schema (Pydantic)
# ------------------------------------------------------------
class Todo(BaseModel):
    id: Optional[int]= None
    title: str
    completed: bool = False

    class Config:
        orm_mode = True

# ------------------------------------------------------------
# 🔐 Login Schema
# ------------------------------------------------------------
class Login(BaseModel):
    username: str
    password: str

# ------------------------------------------------------------
# 🔌 DB Dependency
# ------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Token expired or invalid")

# ------------------------------------------------------------
# 🏠 Home
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "FastAPI + MySQL + JWT TODO 🚀"}
users={"admin": "admin123","user1": "1_user","user2": "2_user"}

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(user: Login):
    '''
    Dummy Login
    Username = admin
    Password = admin123
    '''
    if user.username not in users or user.password != users[user.username]:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "20 minutes"
    }

# ------------------------------------------------------------
# ✅ CREATE
# ------------------------------------------------------------
@app.post("/todos")
def create_todo(todo: Todo, db: Session = Depends(get_db), user: str = Depends(verify_token)):
    existing = db.query(TodoDB).filter(TodoDB.id == todo.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="ID already exists")

    new_todo = TodoDB(
        id=todo.id,
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return {"message": "Created", "data": new_todo}

# ------------------------------------------------------------
# ✅ READ ALL
# ------------------------------------------------------------
@app.get("/todos")
def get_all(db: Session = Depends(get_db), user: str = Depends(verify_token)):
    todos = db.query(TodoDB).all()
    return {"count": len(todos), "data": todos}

# ------------------------------------------------------------
# ✅ READ ONE
# ------------------------------------------------------------
@app.get("/todos/{todo_id}")
def get_one(todo_id: int, db: Session = Depends(get_db), user: str = Depends(verify_token)):
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Not found")

    return todo

# ------------------------------------------------------------
# ✅ UPDATE
# ------------------------------------------------------------
@app.put("/todos/{todo_id}")
def update(todo_id: int, updated: Todo, db: Session = Depends(get_db), user: str = Depends(verify_token)):
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Not found")

    todo.title = updated.title
    todo.completed = updated.completed

    db.commit()
    db.refresh(todo)

    return {"message": "Updated", "data": todo}

# ------------------------------------------------------------
# ✅ DELETE
# ------------------------------------------------------------
@app.delete("/todos/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db), user: str = Depends(verify_token)):
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(todo)
    db.commit()

    return {"message": "Deleted"}

