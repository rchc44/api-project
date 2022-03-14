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

students={
    1:{
        "name":"john",
        "age":50,
        "year":"year 12"
    }    
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class UserInfo(BaseModel):
    email:str
    pw:str

# class with optional fields, so when put method, only update necessary
class UpdateStudent(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    year: Optional[str]=None




@app.get("/") # base url, google.com
def index(): # any name for function
    return {"name":"first Data"}


@app.get("/students")
def getStudents():
    data=db.child("students").get()
    print(data)
    data=db.child("students").get()
    #print(data)
    bob=[]
    for datum in data.each():
        print(datum.val())  
        bob.append(datum.val())
    #return bob
    return data
    return {"data":"rr"}

@app.get("/students/{studentId}")
def getStudent():
    return {}


# signup
@app.post("/signup")
def signup(email:str,pw:str):
    try:
        user = auth.create_user_with_email_and_password(email, pw)
        return user
    except:
        print("could not sign up")
        return {"Error":"Could not sign up"} 

# login, post https://stackoverflow.com/questions/43965316/for-login-get-or-post
@app.post("/login")
def login(userInfo:UserInfo):
    try:
        user = auth.sign_in_with_email_and_password(userInfo.email,userInfo.pw)
        return user
    except Exception as e:
        print("could not sign in")
        return {"Error":e}
        return {"Error":"Could not sign in"}

# logout, post https://stackoverflow.com/questions/3521290/logout-get-or-post?noredirect=1&lq=1
@app.post("/logout")
def logout():
    return {}


data=db.child("students").get()
#print(data)
for datum in data.each():
    print(datum.val())


'''
try:
    user = auth.sign_in_with_email_and_password("errhg","dgr")
    print("success")
except Exception as e:
    e=str(e)
    print("could not sign in")
    print(e) 
'''
'''

	# students


GET /students/{studentId}
	get student info
POST /students
	create new student
PUT /students/{studentId}
	update existing student info
DELETE /students/{studentId}
	delete existing student


	# teachers 
	
	
GET /teachers/{teacherId}
	get teacher info
POST /teachers
	create new teacher
PUT /teachers/{teacherId}
	update existing teacher info
DELETE /users/{userId}
	delete existing teacher


	# tests


GET /tests/{testId}
	get specific test from db
POST /tests
	upload new test
PUT /tests/{testId}
	update existing test
DELETE /tests/{testId}
	delete existing test


	# grades
GET /tests/{testId}/grades/{gradeId}
	get grade for specific test
POST /tests/{testId}/grades
	upload grade for existing test
PUT /tests/{testId}/grades/{gradeId}
	update grade for existing test
DELETE /tests/{testId}/grades/{gradeId}
	delete existing grade
	

'''




