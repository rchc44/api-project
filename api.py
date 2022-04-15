from fastapi import FastAPI,UploadFile
from typing import Optional
from pydantic import BaseModel
import pyrebase
import json
import csv
import codecs
import copy

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


class CreateStudent(BaseModel):
    birthday:str
    emergencyContact:str
    firstName:str
    grade:int
    lastName:str
    school:str
    username:str
    email:str

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


class CreateTeacher(BaseModel):
    bio:str
    birthday:str
    firstName:str
    lastName:str
    phone:str
    subject:str
    school:str
    username:str
    email:str

# class with optional fields, for PUT 
class UpdateTeacher(BaseModel):
    bio:Optional[str]=None
    birthday:Optional[str]=None
    firstName:Optional[str]=None
    lastName:Optional[str]=None
    phone:Optional[str]=None
    subject:Optional[str]=None
    school:Optional[str]=None
    username:Optional[str]=None
    email:Optional[str]=None



class CreateTest(BaseModel):
    createdBy:str
    testName:str
    


class CreateSubmission(BaseModel):
    submission:list=[]
    testName:str


class CreateGrade(BaseModel):
    grade:int
    


@app.get("/")
def index():
    return {"message":"Testing"}


'''
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


'''

    ## Students
    
@app.get("/students")
def getStudents():
    data=db.child("students").get()
    cleanedData={}
    students=[]
    cleanedData["students"]=students
    for datum in data.each():
        students.append(datum.val())
    return cleanedData  


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

@app.get("/teachers")
def getTeachers():
    data=db.child("teachers").get()
    cleanedData={}
    teachers=[]
    
    cleanedData["teachers"]=teachers
    for datum in data.each():
	students=[]
        if "students" in datum.val():
            for student in datum.val()["students"]:
                students.append(student)
        datum.val()["students"]=students
        teachers.append(datum.val())
    
                
    return cleanedData  


@app.get("/teachers/{username}") # get by id, username, email
def getTeacher(username:str):
    data=db.child("teachers").order_by_child("username").equal_to(username).get()
    returnVal={}
    
    for datum in data.each():
        returnVal["data"]=datum.val()
        students=[]
        if "students" in returnVal["data"]:
            tmp=returnVal["data"]["students"]
            for student in tmp:
                students.append(student)
                
        returnVal["data"]["students"]=students
            
        
    if not returnVal:
        returnVal["message"]="username not found" 
    
    sortedData={}
    sortedData["data"]={}
    for k, v in returnVal["data"].items():
        sortedData["data"][k]=v
        
    return sortedData
    

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
    
    students=[]
    for datum in data.each():
        if "students" in datum.val():
            for student in datum.val()["students"]:
                students.append(student)
        returnVal["data"]=students
        
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
                    
                    returnObj={}
                    for student in returnVal:
                        returnObj["student"]=student
                    
                    return returnObj
            return {"message":"student's username not found"}
    return {"message":"teacher's username not found"}



@app.delete("/teachers/{teacher_username}/students/{student_username}")
def deleteStudentFromTeacher(teacher_username:str,student_username:str):
    teachers=db.child("teachers").get()
    for teacher in teachers.each():
        if teacher.val()['username'] == teacher_username:
            returnVal= db.child("teachers").child(teacher.key()).child("students").update({student_username:None})    

            returnObj={}
            for student in returnVal:
                returnObj["student"]=student
            
            return returnObj
    return {"message":"teacher's not found"}




	## Tests


@app.get("/tests")
def getTests():
    data=db.child("tests").get()
    cleanedData={}
    tests=[]
    cleanedData["tests"]=tests
    for datum in data.each():
        tests.append(datum.val()["testName"])
    return cleanedData  

    
    
@app.get("/tests/{testName}") #get all questions of a test from db 
def getTest(testName:str):
    
    data=db.child("tests").order_by_child("testName").equal_to(testName).get()
    returnVal={}
    
    for datum in data.each():
        returnVal["data"]=datum.val()
        questions=[]
        if "questions" in returnVal["data"]:
            tmp=returnVal["data"]["questions"]
            for question in tmp:
                questions.append(returnVal["data"]["questions"][question])
        
        returnVal["data"]["questions"]=questions
        
    if not returnVal:
        returnVal["message"]="testName not found"        
    return returnVal
	 

@app.post("/tests/{createdBy}") #upload/create new test -> csv to database format conversion
async def testUpload(file:UploadFile,createdBy:str):
    if file.content_type not in ["csv","application/vnd.ms-excel","application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        return {"message":"Invalid document type"}
    
    csv_reader = csv.reader(codecs.iterdecode(file.file,'utf-8'))
    
    dataTest={}
    dataTest["createdBy"]=createdBy
    dataTest["testName"]=file.filename[:-4] # remove .csv
    
    dataQuestions={}
    
    cnt=0
    for row in csv_reader:
        if cnt==0:
            cnt+=1
            continue
        if len(row)!=5:
            return {"message":"Wrong question format"}
        dataQuestion={}
        dataQuestion["type"]=row[0]
        dataQuestion["number"]=row[1]
        dataQuestion["description"]=row[2]
        dataQuestion["answer"]=row[3]
        dataQuestion["options"]=row[4]
        
        dataQuestions[f"q{cnt}"]=dataQuestion
        cnt+=1
    dataTest["questions"]=dataQuestions
    
    returnVal = db.child("tests").push(dataTest)  
    return returnVal
    #return {"FileName":file.filename}


@app.delete("/tests/{testName}")
def deleteTest(testName:str):
    tests=db.child("tests").get() # nodes of tree
    for test in tests.each():
        if test.val()['testName'] == testName:
            db.child("tests").child(test.key()).remove()  
            return {"message":"successfully removed"}
    return {"message":"testName not found"}



    ## Submissions

@app.get("/submissions/{username}/{testName}") # get submission by student of specific test
def getSpecificSubmission(username:str,testName:str):
    submissions=db.child("submissions").get() 
    cleanedData={}
    lstConversion=[]
    for submission in submissions.each():
        if submission.val()['testName'] == testName and submission.val()["username"]==username:
            cleanedData["data"]=submission.val()
            for datum in cleanedData["data"]["submission"]:
                lstConversion.append(cleanedData["data"]["submission"][datum])
            cleanedData["data"]["submission"]=lstConversion
            return cleanedData
    return {"message":"submission not found"}    



def cleanSubmission(data):
    cleanedData=[]
    for q in data:
        cleanedData.append(data[q])
    return cleanedData

@app.get("/submissions/{username}") # get all submissions by student
def getAllSubmissions(username:str):
    submissions=db.child("submissions").get()
    cleanedData={}
    cleanedData["data"]={}
    lst=[]
    for submission in submissions.each():
        if submission.val()["username"]==username:
            cleanedSubmission=cleanSubmission(submission.val()["submission"])
            submission.val()["submission"]=cleanedSubmission
            if "grade" in submission.val():
                del submission.val()["grade"]            
            lst.append(submission.val())
    
    cleanedData["data"]=lst
    if len(lst)>0:
        return cleanedData   
    else: 
        return {"message":"no submissions found"}



@app.get("/tests/submissions/{testName}") # get all submissions of a test
def getAllSubmissionsOfTest(testName:str):
    submissions=db.child("submissions").get() 
    cleanedData={}
    cleanedData["data"]={}
    lst=[]
    for submission in submissions.each():
        if submission.val()["testName"]==testName:
            cleanedSubmission=cleanSubmission(submission.val()["submission"])
            submission.val()["submission"]=cleanedSubmission
            if "grade" in submission.val():
                del submission.val()["grade"]
            lst.append(submission.val())
            
    cleanedData["data"]=lst
    if len(lst)>0:
        return cleanedData
    else: 
        return {"message":"no submissions found"}


@app.post("/submissions/{username}")
def createSubmission(username:str,createSubmission:CreateSubmission):
    # submission list [{providedAnswer:}]
    # get test and store with submission
    tests=db.child("tests").get() 
    submissionData=createSubmission.dict()
    
    for test in tests.each():
        if test.val()['testName'] == submissionData["testName"]:
            # make sure number of submitted answers is equal to number of questions in test
            if len(test.val()["questions"])!=len(submissionData["submission"]):
                return {"message":"submission doesn't have all provided answers"}
            
            
            newData=copy.deepcopy(test.val())
            newData["username"]=username
            
            newData["submission"]=newData["questions"]
            del newData["questions"]
            
            cnt=0
            
            
            for k in newData["submission"]:
                newData["submission"][k]["providedAnswer"]=submissionData["submission"][cnt]["providedAnswer"]
                cnt+=1
            db.child("submissions").push(newData)
            
            
            return {"message":"successfully added submission"}
        
    return {"message":"testName not found"}


@app.delete("/submissions/{username}/{testName}")
def deleteSubmission(username:str,testName:str):
    submissions=db.child("submissions").get() 
    for submission in submissions.each():
        if submission.val()['testName'] == testName and submission.val()["username"]==username:
            db.child("submissions").child(submission.key()).remove()  
            return {"message":"successfully removed"}
    return {"message":"submission not found"}



    ## Grades

@app.get("/grades/{username}")
def getGrades(username:str): #all grades of all student's submissions   
    dataGrades={}
    submissions=db.child("submissions").get() 
    grades=[]
    for submission in submissions.each():
        if submission.val()["username"]==username:
            if "grade" in submission.val():
                grades.append({
                    "testName":submission.val()["testName"],
                    "grade":submission.val()["grade"]
                })
    
    
    dataGrades["grades"]=grades
    if len(grades)>0: 
        return dataGrades
    else:
        return {"message":"No grades found"}
    
@app.post("/grades/{username}/{testName}")
def createGrade(username:str,testName:str,createGrade:CreateGrade): # upload or update grade for test, in submissions
    dataGrade=createGrade.dict()    
    submissions=db.child("submissions").get() 
    for submission in submissions.each():
        if submission.val()['testName'] == testName and submission.val()["username"]==username:
            db.child("submissions").child(submission.key()).update(dataGrade)  
            return {"message":"successfully created Grade"}    
    return {"message": "username or test not found"}
   

@app.delete("/grades/{username}/{testName}")
def deleteGrade(username:str,testName:str): # delete grade for test, in submissions  
    submissions=db.child("submissions").get() 
    for submission in submissions.each():
        if submission.val()['testName'] == testName and submission.val()["username"]==username:
            db.child("submissions").child(submission.key()).update({"grade":None})  
            return {"message":"successfully deleted Grade"}    
    return {"message": "username or test not found"}
  

'''


	
PUT /submissions/{studentId}
	update student's submission


'''





