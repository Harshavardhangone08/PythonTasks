from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#from typing import List

#Create app
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome"}

#Creating a model
class std(BaseModel):
    id: int
    name: str
    age: int
    Course: str
    marks: float
    
Students = []
@app.get("/Students")
def display_all():
    return Students


@app.post("/Students")
def add_std(s_info :std):
    for student in Students:
        if student.id==s_info.id:
            raise HTTPException(status_code=400, detail="Student ID already exists")
    Students.append(s_info)
    return {"message":"STUDENT ADDED SUCCESSFULLY", "student":s_info}


@app.get("/Students/{id}")
def std_by_id(id:int):
    for s_info in Students:
        if s_info.id == id:
            return s_info
    raise HTTPException(status_code=404, detail="ID not found")


@app.put("/Students/{id}")
def update_by_id(id:int,s_info :std):
    for i in range(len(Students)):
        if Students[i].id == id:
            Students[i] = s_info
            return Students 
        
    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/Students/{id}")
def del_by_id(id:int):
    for info in range(len(Students)):
        if Students[info].id == id:
            del Students[info]
            return {"message":"Student Data Deleted Successfully", "Data":Students[info]}
    raise HTTPException(status_code=404, detail="Student not found")