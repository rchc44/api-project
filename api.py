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

# class with optional fields, so when put method, only update necessary
class UpdateStudent(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    year: Optional[str]=None


class CreateStudent(BaseModel):
    birthday:str
    emergencyContact:str
    firstName:str
    grade:int
    lastName:str
    school:str
    username:str
    


@app.get("/")
def index():
    return {"name":"Test Data"}


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







