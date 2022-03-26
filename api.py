from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel
import pyrebase
import json


firebaseConfig = {
  'apiKey': "AIzaSyA6DcIx3J8ZwJFes3EzAztL0rD8zK9PLC8",
  'authDomain': "cosmoquizz.firebaseapp.com",
  'projectId': "cosmoquizz",
  'storageBucket': "cosmoquizz.appspot.com",
  'messagingSenderId': "529570879790",
  'appId': "1:529570879790:web:ccb089771222ca29b7c2bf",
  'measurementId': "G-FT29PHMLJE",
  'databaseURL': "https://cosmoquizz-default-rtdb.firebaseio.com/"
}


firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
auth=firebase.auth()

app=FastAPI()


class UserInfo(BaseModel):
    email:str
    pw:str

# class with optional fields, for PUT 
class UpdateStudent(BaseModel):
    birthday:Optional[str]=None
    emergencyContact:Optional[str]=None
    firstName:Optional[str]=None
    grade:Optional[int]=None
    lastName:Optional[str]=None
    school:Optional[str]=None
    username:Optional[str]=None
    email:Optional[str]=None


class CreateStudent(BaseModel):
    birthday:str
    emergencyContact:str
    firstName:str
    grade:int
    lastName:str
    school:str
    username:str
    email:str


@app.get("/")
def index():
    return {"message":"Testing"}



# signup
@app.post("/signup")
def signup(userInfo:UserInfo,createStudent:CreateStudent):
    try:
        user = auth.create_user_with_email_and_password(userInfo.email, userInfo.pw)
        
        dataStudent=createStudent.dict()
        dataStudent["email"]=userInfo.email
        db.child("students").push(dataStudent)
        return user
    except Exception as e:
        e=e.strerror
        e=json.loads(e)
        return {"code":e['error']['code'],"message":e['error']['message']}



# login
@app.post("/login")
def login(userInfo:UserInfo):
    try:
        user = auth.sign_in_with_email_and_password(userInfo.email,userInfo.pw)
        return user # important properties: refreshToken,idToken
    except Exception as e:
        e=e.strerror
        e=json.loads(e)
        return {"code":e['error']['code'],"message":e['error']['message']}


# logout 
@app.post("/logout")
def logout():
    #auth.current_user = None
    return {}




    ## Students
    
@app.get("/students")
def getStudents():
    data=db.child("students").get()
    return data
    
    '''
    dataCleaned=[]
    
    for datum in data.each():
        dataCleaned.append(datum.val())
    return dataCleaned
    '''


@app.get("/students/{username}") # get by id, username, email
def getStudent(username:str):
    data=db.child("students").order_by_child("username").equal_to(username).get()
    returnVal={}
    
    for datum in data.each():
        returnVal["data"]=datum.val()
        
    if not returnVal:
        returnVal["message"]="username not found"        
    return returnVal
    

@app.post("/students")
def createStudent(createStudent:CreateStudent):
    dataStudent=createStudent.dict()
    
    students=db.child("students").get()
    for student in students.each():
        if student.val()['username'] == dataStudent["username"]:
            return {"message":"username already exists"}
        
    returnVal = db.child("students").push(dataStudent)    
    return returnVal # returns id of student

@app.put("/students/{username}")
def updateStudent(username:str,updateStudent:UpdateStudent):
    dataStudent=updateStudent.dict()
    dataUpdate={}
    
    for key in dataStudent:
        if dataStudent[key] is not None:
            dataUpdate[key]=dataStudent[key]    
    
    students=db.child("students").get()
    for student in students.each():
        if student.val()['username'] == username:
            returnVal= db.child("students").child(student.key()).update(dataUpdate)    
            return returnVal
    
    return {"message":"username not found"}


@app.delete("/students/{username}")
def deleteStudent(username:str):
    students=db.child("students").get() # nodes of tree
    for student in students.each():
        if student.val()['username'] == username:
            db.child("students").child(student.key()).remove()  
            return {"message":"successfully removed"}
    return {"message":"username not found"}





    ## Teachers


@app.get("/teachers/{username}") # get by id, username, email
def getTeacher(username:str):
    data=db.child("teachers").order_by_child("username").equal_to(username).get()
    returnVal={}
    
    for datum in data.each():
        returnVal["data"]=datum.val()
        
    if not returnVal:
        returnVal["message"]="username not found"        
    return returnVal
    

@app.post("/teachers")
def createTeacher(createTeacher:CreateTeacher):
    dataTeacher=createTeacher.dict()
    
    teachers=db.child("teachers").get()
    for teacher in teachers.each():
        if teacher.val()['username'] == dataTeacher["username"]:
            return {"message":"username already exists"}
        
    returnVal = db.child("teachers").push(dataTeacher)    
    return returnVal # returns id of teacher


@app.put("/teachers/{username}")
def updateTeacher(username:str,updateTeacher:UpdateTeacher):
    dataTeacher=updateTeacher.dict()
    dataUpdate={}
    
    for key in dataTeacher:
        if dataTeacher[key] is not None:
            dataUpdate[key]=dataTeacher[key]    
    
    teachers=db.child("teachers").get()
    for teacher in teachers.each():
        if teacher.val()['username'] == username:
            returnVal= db.child("teachers").child(teacher.key()).update(dataUpdate)    
            return returnVal
    
    return {"message":"username not found"}


@app.delete("/teachers/{username}")
def deleteTeacher(username:str):
    teachers=db.child("teachers").get() # nodes of tree
    for teacher in teachers.each():
        if teacher.val()['username'] == username:
            db.child("teachers").child(teacher.key()).remove()  
            return {"message":"successfully removed"}
    return {"message":"username not found"}


  
  


    
  
    ## Students of Teachers



@app.get("/teachers/{username}/students") # get by id, username, email
def getAllStudentsOfTeacher(username:str):
    data=db.child("teachers").order_by_child("username").equal_to(username).get()
    returnVal={}
    
    for datum in data.each():
        if "students" in datum.val():
            returnVal["data"]=datum.val()["students"]
        else:
            returnVal["data"]={}
        
    if not returnVal:
        returnVal["message"]="teacher's username not found"    
        
    return returnVal
    

@app.put("/teachers/{teacher_username}/students/{student_username}")
def addStudentToTeacher(teacher_username:str,student_username:str):
    teachers=db.child("teachers").get()
    students=db.child("students").get()
    for teacher in teachers.each():
        if teacher.val()['username'] == teacher_username:
            for student in students.each():
                if student.val()['username'] == student_username:
                    returnVal= db.child("teachers").child(teacher.key()).child("students").update({student_username:True})    
                    return returnVal
            return {"message":"student's username not found"}
    return {"message":"teacher's username not found"}





@app.delete("/teachers/{teacher_username}/students/{student_username}")
def deleteStudentFromTeacher(teacher_username:str,student_username:str):
    teachers=db.child("teachers").get()
    for teacher in teachers.each():
        if teacher.val()['username'] == teacher_username:
            returnVal= db.child("teachers").child(teacher.key()).child("students").update({student_username:None})    
            return returnVal
    
    return {"message":"teacher's not found"}



