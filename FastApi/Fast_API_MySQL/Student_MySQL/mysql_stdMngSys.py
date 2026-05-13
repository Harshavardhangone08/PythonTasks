# ======================================================================================
# 📝 FastAPI Student Management System (CRUD) - SQLite Database Version
# ======================================================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
# ------------------------------------------------------------
# 🚀 Create FastAPI Application
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/student_db"

engine=create_engine(DATABASE_URL)

Sessionlocal=sessionmaker(bind=engine)
Base=declarative_base()

# ------------------------------------------------------------
# 🧱 Database Model (Table)
# ------------------------------------------------------------
class Students_DB(Base):
    __tablename__="Students"
    
    id= Column(Integer,primary_key=True,index=True)
    name= Column(String(255))
    age= Column(Integer)
    Course= Column(String(255))
    marks= Column(Float)
    
Base.metadata.create_all(bind=engine)
    
# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class std(BaseModel):
    id: int
    name: str
    age: int
    Course: str
    marks: float
    class Config:
        form_attributes = True

# ------------------------------------------------------------
# 🔌 Dependency (DB Session)
# ------------------------------------------------------------
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------

@app.get("/")
def home():
    return {"message":"Student Management System with DataBase"}


# ------------------------------------------------------------
# ✅ 1. Add Student Data
# ------------------------------------------------------------
@app.post("/Students")
def add_std(s_info :std,db: Session=Depends(get_db)):
    existing=db.query(Students_DB).filter(Students_DB.id==s_info.id).first()
    if existing:
                raise HTTPException(status_code=400, detail="ID already exists")
    
    new_std=Students_DB(
        id=s_info.id,
        name= s_info.name,
        age= s_info.age,
        Course= s_info.Course,
        marks= s_info.marks
    )
    
    db.add(new_std)
    db.commit()
    db.refresh(new_std)

    return {"message":"Student Data Added","data":new_std}

# ------------------------------------------------------------
# ✅ 2. READ ALL Students Data
# ------------------------------------------------------------
@app.get("/Students")
def display_all_std(db:Session=Depends(get_db)):
    Students=db.query(Students_DB).all()
    
    return {"count":len(Students),"data":Students}


# ------------------------------------------------------------
# ✅ 3. READ SINGLE Student Data
# ------------------------------------------------------------
@app.get("/Students/{S_id}")
def std_by_id(S_id:int, db:Session=Depends(get_db)):
    s_info=db.query(Students_DB).filter(Students_DB.id==S_id).first()
    
    if not s_info:
        raise HTTPException(status_code=404, detail="ID not found")
    return s_info

# ------------------------------------------------------------
# ✅ 4. UPDATE TODO
# ------------------------------------------------------------
@app.put("/Students/{S_id}")
def update_stu(S_id:int,updated:std,db: Session = Depends(get_db)):
    s_info = db.query(Students_DB).filter(Students_DB.id == S_id).first()
    
    if not s_info:
        raise HTTPException(status_code=404, detail="Student not found")
    
    s_info.name=updated.name
    s_info.age=updated.age
    s_info.Course=updated.Course
    s_info.marks=updated.marks
    
    db.commit()
    db.refresh(s_info)
    
    return {"message": "Student data updated successfully", "data": s_info}

# ------------------------------------------------------------
# ✅ 5. DELETE Student
# ------------------------------------------------------------
@app.delete("/Students/{S_id}")
def del_stu(S_id:int,db: Session = Depends(get_db)):
    s_info=db.query(Students_DB).filter(Students_DB.id == S_id).first()
    
    if not s_info:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(s_info)
    db.commit()

    return {"message":"Student Data Deleted Successfully"}

